from __future__ import print_function

import webbrowser
from tkinter import *
from PIL import ImageTk, Image
import backend
l_font = ("Times new Roman", 18, )
m_font = ("Courier", 14)
s_font = ("Verdana", 12)

import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

import auth


def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'credentials_GMAIL.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credentials()

http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)

import send_email


class IndexPage(object):
    def __init__(self, window):
        self.emails = []
        self.window = window
        self.window.minsize(1100, 800)
        self.window.title("BIS community")

        # paths
        path = "ski.png"
        path_p = "prado.png"
        path_t = "techie.png"
        path_b = "bis.png"

        # frames
        self.frame = Frame(master=window, bg="white")
        self.frame.grid(row=1, column=0, columnspan=8)

        self.title = Frame(master=window, bg="white")
        self.title.grid(row=0, column=0, columnspan=8)

        self.form = Frame(master=window, bg="white")
        self.form.grid(row=4, column=0, columnspan=8)

        # fonts
        self.font1 = l_font
        self.font2 = m_font
        self.font3 = s_font

        # title

        self.canvas0 = Canvas(master=self.title, width=215, height=111, bg="black")
        self.canvas0.img =ImageTk.PhotoImage(Image.open(path_b))
        self.canvas0.create_image(10, 9, image=self.canvas0.img, anchor="nw")
        self.canvas0.grid(row=0, column=1, pady=20)

        # ski
        self.canvas = Canvas(master=self.frame, width=400, height=200, bg="green")
        self.canvas.img = ImageTk.PhotoImage(Image.open(path))
        self.canvas.create_image(0, 0, image=self.canvas.img, anchor="nw")
        self.canvas.grid(row=1, column=1, padx=30)

        # prado
        self.canvas = Canvas(master=self.frame, width=280, height=200, bg="green")
        self.canvas.img = ImageTk.PhotoImage(Image.open(path_p))
        self.canvas.create_image(-25, 0, image=self.canvas.img, anchor="nw")
        self.canvas.grid(row=1, column=0, padx=30)

        # techie
        self.canvas = Canvas(master=self.frame, width=280, height=200, bg="green")
        self.canvas.img = ImageTk.PhotoImage(Image.open(path_t))
        self.canvas.create_image(0, 0, image=self.canvas.img, anchor="nw")
        self.canvas.grid(row=1, column=2, padx=30)

        # Line
        self.canvas2 = Canvas(master=self.form, width=450, height=20, bg="black")
        self.canvas2.create_text(35, 7, text="Do not miss this opportunity and register below!!!", font=self.font2, anchor="nw", fill="white")
        self.canvas2.grid(row=4, column=2, pady=30)

        # create the backend instance
        self.bk = backend.Back()

        # labels

        '''
        self.lb1 = Label(master=self.window, text="2019 ACTIVITIES", font=self.font1)
        self.lb1.grid(row=0, column=0, columnspan=7, pady=20)
        '''

        self.lb2 = Label(master=self.window, text="    PRADO VISIT", font=self.font1, cursor="hand2")
        self.lb2.grid(row=2, column=1, sticky="e", pady=20)
        self.lb2.bind("<Button-1>", lambda e: self.callback("https://museodelprado.museumsmadrid.org/en"))

        self.lb3 = Label(master=self.window, text="         SKI TRIP", font=self.font1)
        self.lb3.grid(row=2, column=3, sticky="e", pady=20)

        self.lb4 = Label(master=self.window, text="TECH IE", font=self.font1, cursor="hand2")
        self.lb4.grid(row=2, column=6, sticky="ew", pady=20)
        self.lb4.bind("<Button-1>", lambda e: self.callback("http://techieconf.com/"))

        # description
        self.t_prado = Label(master=self.window, text="-Price: 15€", font=self.font3)
        self.t_prado.grid(row=3, column=1, sticky="ew")

        self.t_prado = Label(master=self.window, text="- Price: 300€", font=self.font3)
        self.t_prado.grid(row=3, column=3, sticky="e")

        self.t_tech = Label(master=self.window, text="- Price: 30€", font=self.font3)
        self.t_tech.grid(row=3, column=6, pady=1, padx=5, sticky="ew")

        # entry text and labels
        self.lb_name = Label(master=self.window, text="Name", font=self.font2)
        self.lb_name.grid(row=5, column=1, sticky="e", pady=20)

        self.text_name = StringVar()
        self.et1 = Entry(master=self.window, textvariable=self.text_name, font=self.font3)
        self.et1.grid(row=5, column=2, sticky="w", pady=20)

        self.lb_lastN = Label(master=self.window, text="Last name", font=self.font2)
        self.lb_lastN.grid(row=5, column=3, sticky="e", pady=20)

        self.text_lastN = StringVar()
        self.et2 = Entry(master=self.window, textvariable=self.text_lastN, font=self.font3)
        self.et2.grid(row=5, column=4, sticky="w", pady=20)

        self.lb_email = Label(master=self.window, text="Email", font=self.font2)
        self.lb_email.grid(row=5, column=5, sticky="e", pady=20)

        self.text_email = StringVar()
        self.et3 = Entry(master=self.window, textvariable=self.text_email, font=self.font3)
        self.et3.grid(row=5, column=6, sticky="w", pady=20)

        # submit
        self.bt1 = Button(master=self.window, width=14, text="REGISTER NOW!", font=self.font2, command=self.submit, cursor="hand2")
        self.bt1.grid(row=6, column=3, sticky="e", pady=20)

    def submit(self):
        name = self.text_name.get()
        lastN = self.text_lastN.get()
        email = self.text_email.get()
        self.emails.append(email)
        sendInst = send_email.send_email(service)
        message = sendInst.create_message_with_attachment('cod.apprentice.bis@gmail.com', email,
                                                          'BIS - SKI TRIP 2020',
                                                          'They want to kill our degree but they will never kill our'
                                                          ' friendships. Time flies by, lets have some fun together.'
                                                          , 'formi2.png')
        sendInst.send_message('me', message)
        self.bk.suscribe(name, lastN, email)
        self.lb_feedback = Label(master=self.window, text="You have been recorded \n successfully!", font=self.font2)
        self.lb_feedback.grid(row=7, column=3, pady=10, sticky="e")

    def callback(self, url):
        webbrowser.open_new(url)

window = Tk()
IndexPage(window)
window.mainloop()