from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageTk

from register import RegisterClass
from login import LoginClass

class GAPS_Class:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphical Password Authentication System | sikandarsingh2210@gmail.com | +91-7057525359")
        self.root.geometry("1000x720+150+10")
        self.root.config(bg = "white")
        self.root.resizable(False, False)
        self.root.overrideredirect(True)

        Label(self.root, text = "Graphical Password Authentication System", font = ("goudy old style", 32, "bold"), fg = "darkred", bg = "white", bd = 0).place(x = 0, y = 20, relwidth = 1, height = 70)

        self.setting_image = PhotoImage(file = "Icons/settings1.png")
        self.setting_image = self.setting_image.subsample(8, 8)
        Button(self.root, image = self.setting_image, command = self.setting_cmd, bd = 0, relief = GROOVE, cursor = "hand2", bg = "white", activebackground = "white").place(x = 10, y = 15, width = 80, height = 80)

        self.close_image = PhotoImage(file = "Icons/cross.png")
        self.close_image = self.close_image.subsample(8, 8)
        Button(self.root, image = self.close_image, command = self.close_cmd, bd = 0, relief = GROOVE, cursor = "hand2", bg = "white", activebackground = "white").place(x = 920, y = 15, width = 80, height = 80)

        self.auth_image = ImageTk.PhotoImage(file = "Images/auth1.png")
        # self.auth_image = self.auth_image.subsample(8, 8)
        Label(self.root, image = self.auth_image, bd = 0).place(x = 350, y = 110)

        self.register_btn = Button(self.root, text = "Register", command = self.register_cmd, cursor = "hand2", activebackground = "white", activeforeground = "darkblue", font = ("courier", 20, "bold"), fg = "darkblue", bg = "white")
        self.register_btn.place(x = 280, y = 400, width = 400, height = 50)

        self.login_btn = Button(self.root, text = "Login", command = self.login_cmd, cursor = "hand2", activebackground = "white", activeforeground = "darkblue", font = ("courier", 20, "bold"), fg = "darkblue", bg = "white")
        self.login_btn.place(x = 280, y = 500, width = 400, height = 50)

        Label(self.root, text = "Graphical Password Authentication System | Developed in Python Programming using Tkinter Library \n Developed by Sikandar Singh | Contact : +91-7057525359 | sikandarsingh.official.22@gmail.com", font = ("goudy old style", 16, "bold"), fg = "darkred", bg = "white", bd = 0).place(x = 0, y = 665, relwidth = 1, height = 50)

    def register_cmd(self):
        self.window = Toplevel(self.root)
        obj = RegisterClass(self.window)

    def login_cmd(self):
        self.window = Toplevel(self.root)
        obj = LoginClass(self.window)

    def close_cmd(self):
        close = msg.askyesno("Exit Application","Do you really want to exit application", parent = self.root)
        if close == True:
            self.root.destroy()
        else:
            pass

    def setting_cmd(self):
        pass

if __name__ == "__main__":
    root = Tk()
    obj = GAPS_Class(root)
    root.mainloop()
