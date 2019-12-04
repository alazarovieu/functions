import tkinter as tk


class Project(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.title = "Python project"

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(self, container)
        self.frames[StartPage] = frame

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="StartPage")
        label.pack(pady=20, padx=20)
        self.lb1 = tk.Label(master=self, text="Title")
        self.lb1.grid(row=0, column=0, sticky="w", pady=5)

        self.lb2 = tk.Label(master=self, text="  Year")
        self.lb2.grid(row=0, column=2, sticky="w", pady=5)

        self.lb3 = tk.Label(master=self, text="Director")
        self.lb3.grid(row=1, column=0, sticky="w", pady=5)

        self.lb4 = tk.Label(master=self, text="  Actress/Actor")
        self.lb4.grid(row=1, column=2, sticky="w", pady=5)


"""
        img = ImageTk.PhotoImage(Image.open("/Users/alazarov/Desktop/UNI/THIRD SEMESTER/Python/ski.png"))
        panel = Label(window, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
        pad = 3
        self._geom = '200x200+0+0'
        window.geometry("{0}x{1}+0+0".format(
            window.winfo_screenwidth() - pad, window.winfo_screenheight() - pad))
        window.bind('<Escape>', self.toggle_geom)

        self.bt1 = Button(master=self.window, width=10, text="PageOne!", font=self.font2,
                          command=lambda: Tk.tkraise(PageOne(window)))
        self.bt1.pack()


    def toggle_geom(self, event):
        geom = self.window.winfo_geometry()
        print(geom, self._geom)
        self.window.geometry(self._geom)
        self._geom = geom


class PageOne(object):
    def __init__(self, window):
        self.window = window
        self.window.title("Page One")
        self.font1 = l_font
        self.font2 = m_font
        self.font3 = s_font
        pad = 3
        self._geom = '200x200+0+0'
        window.geometry("{0}x{1}+0+0".format(
            window.winfo_screenwidth() - pad, window.winfo_screenheight() - pad))
        window.bind('<Escape>', self.toggle_geom)

        self.bt1 = Button(master=self.window, width=20, text="Back to home", font=self.font2,
                          command=lambda: Tk.tkraise(IndexPage(window)))
        self.bt1.grid(row=2, column=2)

    def toggle_geom(self, event):
        geom = self.window.winfo_geometry()
        print(geom, self._geom)
        self.window.geometry(self._geom)
        self._geom = geom
"""

app = Project()
app.mainloop()
