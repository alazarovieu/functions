import random
import PIL
from PIL import ImageTk
import PIL.Image
from tkinter import *


class GUI:
    def __init__(self, window):

        self.window = window
        window.title("Hangman")
        window.geometry("800x600")
        window.resizable(0, 0)

        # canvas to display letters
        self.canvas_letters = []
        self.canvas_display = []

        # create frame which does not allow to expand with the widgets
        self.frame = Frame(master=window, bg="white")
        self.frame.pack_propagate(0)

        # expand to fill the root window geometry
        self.frame.pack(fill=BOTH, expand=1)

        # create canvas to display images
        self.canvas = Canvas(master=self.frame, width=300, height=400, bg="white")
        self.canvas.grid(row=1, column=1, pady=20, columnspan=8, sticky="e")

        # initial image
        self.canvas.img = ImageTk.PhotoImage(PIL.Image.open("h1.png"))
        self.canvas.create_image(0, 0, image=self.canvas.img, anchor="nw")

        # calling the functions to get the word
        self.word = self.get_guess()
        self.get_guess_length(self.word)

        # entry
        self.enter_letter = ""
        self.et1 = Entry(master=self.frame, textvariable=self.enter_letter, font="verdana")
        self.et1.grid(row=8, column=2)
        self.l1 = Label(master=self.frame, text="LETTER:", font ="verdana", pady=20)
        self.l1.grid(row=8, column=1, padx=30)
        self.b1 = Button(master=self.frame, text="Try", cursor="hand2", command=self.match(self.enter_letter, self.word))
        self.b1.grid(row=8, column=3, padx=30)

    def get_guess(self):
        f = open("hangManDictionary.txt")
        total_fileL = 0
        for line in f:
            total_fileL += 1

        n = random.randint(0, total_fileL)
        print(n)
        counter = 0
        select = ""
        f = open("hangManDictionary.txt")

        for line in f:
            if counter < n-1:
                counter += 1
            else:
                select = line
                print(select)
                return select

    def get_guess_length(self, guess):
        l = len(guess)
        for i in range(0, l):
            self.canvas_letters.append(Label(master=self.frame, text="______"))
            self.canvas_letters[i].grid(row=8, column=i+5)
            self.canvas_display.append(Label(master=self.frame, text=""))
            self.canvas_display[i].grid(row=7, column=i+5)

    def match(self, letter, guess):
        for i in guess:
            if letter == i:
                self.canvas_display[i].Label.configure(master=self.frame, text=letter)
                l2 = Label(master=self.frame, text="MATCH!")
                l2.grid(row=9, column=0, columnspan=3, sticky="ew")
                continue
            else:
                l3 = Label(master=self.frame, text="ERROR!")
                l3.grid(row=9, column=0, columnspan=3, sticky="ew")
                l3.destroy()
                continue


window = Tk()
game = GUI(window)
window.mainloop()
