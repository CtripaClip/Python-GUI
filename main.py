"""
    Base code with CustomTkinter
    Code author - CtripaClip(Dzamal)
    The last updtate - 23.05.2023

"""

import customtkinter as CTk
import subprocess
import sys
from tkinter import *

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.master_config = CTk.CTkFrame(master=self)

        self.geometry("800x600") # settings
        self.title("SpeedTest")
        self.resizable(False, False)

        self.but1 = CTk.CTkButton(master=self, text="New window",command=new_window).pack() # button
        self.but2 = CTk.CTkButton(master=self, text="Notepad",command=open_notepad).pack() # button 2
        self.but3 = CTk.CTkButton(master=self, text="Exit", command=Exit, fg_color="red", width=100).pack() # button 3


def open_notepad():
    subprocess.call("notepad.exe")

def new_window(): # create new window
    tk = Tk()
    tk.geometry("600x400") # settings
    tk.title("NewWindow")

    b1 = Button(tk, text="Back", command=Exit, bg="red").pack()

def Exit():
    sys.exit()

if __name__ == '__main__': # run programm
    app = App()
    app.mainloop()
