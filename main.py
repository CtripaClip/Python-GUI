"""
    Base code with CustomTkinter
    Code author - CtripaClip(Dzamal)

"""

import customtkinter as CTk

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.master_config = CTk.CTkFrame(master=self)

        self.geometry("800x600")
        self.title("SpeedTest")
        self.resizable(False, False)

        self.but1 = CTk.CTkButton(master=self, text="START", width=100).pack()

def new_window():
    pass

if __name__ == '__main__':
    app = App()
    app.mainloop()
