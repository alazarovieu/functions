import base64
import logging
import json

from dateutil import parser
import requests

from pyOutlook.core.attachment import Attachment
from pyOutlook.core.contact import Contact
from pyOutlook.core.folder import Folder
from pyOutlook.internal.utils import get_valid_filename, check_response

log = logging.getLogger('pyOutlook')

__all__ = ['Message']


class Message(object):
    """An object representing an email inside of the OutlookAccount.

        Attributes:
            message_id: A string provided by Outlook identifying this specific email
            body: The body content of the email, including HTML formatting
            body_preview: "The first 255 characters of the body"
            subject: The subject of the email
            sender: The :class:`Contact <pyOutlook.core.contact.Contact>` who sent this email. You can set this
                before sending an email to change which account the email comes from (so long as the
                :class:`OutlookAccount <pyOutlook.core.main.OutlookAccount>` specified has access to the email.
            to: A list of :class:`Contacts <pyOutlook.core.contact.Contact>`. You can also provide a list of strings,
                however these will be turned into :class:`Contacts <pyOutlook.core.contact.Contact>` after sending the
                email.
            cc: A list of :class:`Contacts <pyOutlook.core.contact.Contact>` in the CC field. You can also provide a
                list of strings, however these will be turned into :class:`Contacts <pyOutlook.core.contact.Contact>`
                after sending the email.
            bcc: A list of :class:`Contacts <pyOutlook.core.contact.Contact>` in the BCC field. You can also provide a
                list of strings, however these will be turned into :class:`Contacts <pyOutlook.core.contact.Contact>`
                after sending the email.
            is_draft: Whether or not the email is a draft.
            importance: The importance level of the email; with 0 indicating low, 1 indicating normal, and 2 indicating
                high. ``Message.IMPORTANCE_LOW``, ``Message.IMPORTANCE_NORMAL``, & ``Message.IMPORTANCE_HIGH`` can be
                used to reference the levels.
            categories: A list of strings, where each string is the name of a category.
            time_created: A datetime representing the time the email was created
            time_sent: A datetime representing the time the email was sent

        """

    IMPORTANCE_LOW = 0
    IMPORTANCE_NORMAL = 1
    IMPORTANCE_HIGH = 2

    def __init__(self, account, body, subject, to_recipients, sender=None,
                 cc=None, bcc=None, message_id=None, **kwargs):
        self.account = account
        self.message_id = message_id

        self.body = body
        self.body_preview = kwargs.get('body_preview', '')
        self.subject = subject

        self.is_draft = kwargs.get('is_draft', None)
        self.importance = kwargs.get('Importance', self.IMPORTANCE_NORMAL)
        self.categories = kwargs.get('categories', [])

        focused = kwargs.get('InferenceClassification', False)
        if focused == 'Focused':
            self._focused = True
        else:
            self._focused = False

        self.sender = sender
        self.to = to_recipients
        self.cc = cc or []
        self.bcc = bcc or []

        self.time_created = kwargs.get('time_created', None)
        self.time_sent = kwargs.get('time_sent', None)

        self._attachments = []
        self._has_attachments = kwargs.get('has_attachments', False)

        self.__is_read = kwargs.get('is_read', False)
        self.__parent_folder_id = kwargs.get('parent_folder_id', None)
        self.__parent_folder = None

    def __str__(self):
        return self.subject

    def __repr__(self):
        return str(self)

    @classmethod
    def _json_to_messages(cls, account, json_value):
        return [cls._json_to_message(account, message) for message in json_value['value']]

    @classmethod
    def _json_to_message(cls, account, api_json):
        uid = api_json['Id']
        subject = api_json.get('Subject', '')

        sender = api_json.get('Sender', {})
        sender = Contact._json_to_contact(sender)

        body = api_json.get('Body', {}).get('Content', '')
        body_preview = api_json.get('BodyPreview', '')

        to_recipients = api_json.get('ToRecipients', [])
        to_recipients = Contact._json_to_contacts(to_recipients)

        is_read = api_json['IsRead']
        has_attachments = api_json['HasAttachments']

        time_created = api_json.get('CreatedDateTime', None)
        if time_created is not None:
            time_created = parser.parse(time_created, ignoretz=True)

        time_sent = api_json.get('SentDateTime', None)
        if time_sent is not None:
            time_sent = parser.parse(time_sent, ignoretz=True)

        parent_folder_id = api_json.get('ParentFolderId', None)
        is_draft = api_json.get('IsDraft', None)
        importance = api_json.get('Importance', cls.IMPORTANCE_NORMAL)

        categories = api_json.get('Categories', [])

        return_message = Message(account, body, subject, to_recipients, sender=sender, message_id=uid, is_read=is_read,
                                 time_created=time_created, time_sent=time_sent, parent_folder_id=parent_folder_id,
                                 is_draft=is_draft, importance=importance, body_preview=body_preview,
                                 categories=categories, has_attachments=has_attachments)
        return return_message

    @property
    def focused(self):
        """ Sets and retrieves the 'Focused' status of a Message. If a user has the 'Focused' inbox, messages are
        divided between the Focused and Other tabs. """
        return self._focused

    @focused.setter
    def focused(self, value):

        if not isinstance(value, bool):
            raise TypeError('Message.focused must be a boolean value')

        endpoint = "https://outlook.office.com/api/v2.0/me/messages('{}')".format(self.message_id)

        if value:
            data = dict(InferenceClassification='Focused')
        else:
            data = dict(InferenceClassification='Other')

        r = requests.patch(endpoint, data=json.dumps(data), headers=self.account._headers)

        if check_response(r):
            self._focused = value

    @property
    def attachments(self):
        # type: () -> [Attachment]
        if not self._has_attachments:
            return []

        if self._attachments:
            return self._attachments

        endpoint = 'https://outlook.office.com/api/v2.0/me/messages/{}/attachments'.format(self.message_id)
        r = requests.get(endpoint, headers=self.account._headers)

        if check_response(r):
            data = r.json()
            self._attachments = Attachment.json_to_attachments(self.account, data)

        return self._attachments

    @property
    def is_read(self):
        """ Set and retrieve the 'Read' status of an email

            >>> message = Message()
            >>> message.is_read
            >>> False
            >>> message.is_read = True
        """
        return self.__is_read

    @is_read.setter
    def is_read(self, boolean):
        endpoint = 'https://outlook.office.com/api/v2.0/me/messages/{}'.format(self.message_id)
        payload = dict(IsRead=boolean)

        self._make_api_call('patch', endpoint, data=json.dumps(payload))
        self.__is_read = boolean

    @property
    def parent_folder(self):
        # type: () -> Folder
        """ Returns the :class:`Folder <pyOutlook.core.folder.Folder>` this message is in

            >>> from pyOutlook import *
            >>> account = OutlookAccount('')
            >>> message = account.get_messages()[0]
            >>> message.parent_folder
            Inbox
            >>> message.parent_folder.unread_count
            19

        Returns: :class:`Folder <pyOutlook.core.folder.Folder>`

        """
        if self.__parent_folder is None:
            self.__parent_folder = self.account.get_folder_by_id(self.__parent_folder_id)

        return self.__parent_folder

    def api_representation(self, content_type):
        """ Returns the JSON representation of this message required for making requests to the API.

        Args:
            content_type (str): Either 'HTML' or 'Text'
        """
        payload = dict(Subject=self.subject, Body=dict(ContentType=content_type, Content=self.body))

        if self.sender is not None:
            payload.update(From=self.sender.api_representation())

        # A list of strings can also be provided for convenience. If provided, convert them into Contacts
        if any(isinstance(item, str) for item in self.to):
            self.to = [Contact(email=email) for email in self.to]

        # Turn each contact into the JSON needed for the Outlook API

        recipients = [contact.api_representation() for contact in self.to]

        payload.update(ToRecipients=recipients)

        # Conduct the same process for CC and BCC if needed
        if self.cc:
            if any(isinstance(email, str) for email in self.cc):
                self.cc = [Contact(email) for email in self.cc]

            cc_recipients = [contact.api_representation() for contact in self.cc]
            payload.update(CcRecipients=cc_recipients)

        if self.bcc:
            if any(isinstance(email, str) for email in self.bcc):
                self.bcc = [Contact(email) for email in self.bcc]

            bcc_recipients = [contact.api_representation() for contact in self.bcc]
            payload.update(BccRecipients=bcc_recipients)

        if self._attachments:
            payload.update(Attachments=[attachment.api_representation() for attachment in self._attachments])

        payload.update(Importance=str(self.importance))

        return dict(Message=payload)

    def _make_api_call(self, http_type, endpoint, extra_headers = None, data=None):
        # type: (str, str, dict, Any) -> None
        """
        Internal method to handle making calls to the Outlook API and logging both the request and response
        Args:
            http_type: (str) 'post' or 'delete'
            endpoint: (str) The endpoint the request will be made to
            headers: A dict of headers to send to the requests module in addition to Authorization and Content-Type
            data: The data to provide to the requests module

        Raises:
            MiscError: For errors that aren't a 401
            AuthError: For 401 errors

        """

        headers = {"Authorization": "Bearer " + self.account.access_token, "Content-Type": "application/json"}

        if extra_headers is not None:
            headers.update(extra_headers)

        log.debug('Making Outlook API request for message (ID: {}) with Headers: {} Data: {}'
                  .format(self.message_id, headers, data))

        if http_type == 'post':
            r = requests.post(endpoint, headers=headers, data=data)
        elif http_type == 'delete':
            r = requests.delete(endpoint, headers=headers)
        elif http_type == 'patch':
            r = requests.patch(endpoint, headers=headers, data=data)
        else:
            raise NotImplemented

        check_response(r)
