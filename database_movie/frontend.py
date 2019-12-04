from tkinter import *
import backend


class Front(object):
    # PASS = just assume there will be something there
    def __init__(self, window):
        self.window = window
        self.window.title("This is a fancy database project!")
        self.myfont = ("Helvetica", 19)
        self.yourfont = ("Broadway", 19)
        # need to create a backend instance here
        self.bk = backend.Back()

        # let's create the widgets
        self.lbl1 = Label(master=self.window, text="Title", font=self.myfont)
        self.lbl1.grid(row=0, column=0, sticky="w")

        self.lbl2 = Label(master=self.window, text="  Year", font=self.myfont)
        self.lbl2.grid(row=0, column=2, sticky="w")

        self.lbl3 = Label(master=self.window, text="Director", font=self.myfont)
        self.lbl3.grid(row=1, column=0, sticky="w")

        self.lbl4 = Label(master=self.window, text="  Actress/Actor", font=self.myfont)
        self.lbl4.grid(row=1, column=2, sticky="w")

        # entryText
        self.text_title = StringVar()
        self.et1 = Entry(master=self.window, textvariable=self.text_title, font=self.myfont)
        self.et1.grid(row=0, column=1)

        self.text_director = StringVar()
        self.et2 = Entry(master=self.window, textvariable=self.text_director, font=self.myfont)
        self.et2.grid(row=1, column=1)

        self.text_year = StringVar()
        self.et3 = Entry(master=self.window, textvariable=self.text_year, font=self.myfont)
        self.et3.grid(row=0, column=3)

        self.text_actor = StringVar()
        self.et4 = Entry(master=self.window, textvariable=self.text_actor, font=self.myfont)
        self.et4.grid(row=1, column=3)

        # main screen
        self.listbox = Listbox(master=self.window, font=self.yourfont, height=10, width=80)
        self.listbox.grid(row=2, column=0, rowspan=8, columnspan=2, padx=20, pady=20)

        # need to bind an action for clicking in the listbox
        self.listbox.bind("<<ListboxSelect>>", func=self.get_row)
        self.scroll = Scrollbar(master=self.window)
        self.scroll.grid(row=2, column=2, rowspan=8, sticky="nsw", pady=40)

        # link it to the listbox
        self.scroll.configure(command=self.listbox.yview())  # yview_scroll()?

        # the buttons
        self.bt1 = Button(master=self.window, text="Delete", width=10, font=self.myfont, command=self.delete)
        self.bt1.grid(row=2, column=3, pady=5)

        self.bt2 = Button(master=self.window, text="Add", width=10, font=self.myfont, command=self.add)
        self.bt2.grid(row=3, column=3, pady=5)

        self.bt3 = Button(master=self.window, text="Search", width=10, font=self.myfont, command=self.view)
        self.bt3.grid(row=4, column=3, pady=5)

        self.bt4 = Button(master=self.window, text="Update", width=10, font=self.myfont, command=self.update)
        self.bt4.grid(row=5, column=3, pady=5)

        self.bt5 = Button(master=self.window, text="View All", width=10, font=self.myfont, command=self.view)
        self.bt5.grid(row=6, column=3, pady=5)

        self.bt6 = Button(master=self.window, text="Close", width=10, font=self.myfont, command=self.close)
        self.bt6.grid(row=7, column=3, pady=5)

    def get_row(self, action=None):
        # curse selection returns a list of all the selected lines
        if not self.listbox.curselection():
            return
        line_num = self.listbox.curselection()[0]
        title = self.listbox.get(line_num)[1]
        year = self.listbox.get(line_num)[2]
        director = self.listbox.get(line_num)[3]
        lead = self.listbox.get(line_num)[4]
        self.text_title.set(title)
        self.text_actor.set(lead)
        self.text_year.set(year)
        self.text_director.set(director)
        self.kept_index = self.listbox.get(line_num)[0]

    def view(self):
        data = self.bk.view_all()
        self.listbox.delete(0, END)
        for line in data:
            self.listbox.insert(END, line)

    def add(self):
        title = self.text_title.get()
        year = self.text_year.get()
        director = self.text_director.get()
        lead = self.text_actor.get()
        self.bk.add_element(title, year, director, lead)
        self.view()

    def close(self):
        exit(1)

    def delete(self):
        line_num = self.listbox.curselection()[0]
        idx = self.listbox.get(line_num)[0]
        self.bk.del_element(idx)
        self.view()

    def update(self):
        idx = self.kept_index
        title = self.text_title.get()
        year = self.text_year.get()
        director = self.text_director.get()
        lead = self.text_actor.get()
        self.bk.update_element(title, year, director, lead, idx)
        self.view()


window = Tk()
Front(window)
window.mainloop()
