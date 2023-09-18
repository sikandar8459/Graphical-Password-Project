from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageTk
import sqlite3
import random as rd

conn = sqlite3.connect("GAPS_DB.db")
cur = conn.cursor()

class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page | sikandarsingh2210@gmail.com | +91-7057525359")
        self.root.geometry("1000x720+150+10")
        self.root.config(bg = "white")
        self.root.resizable(False, False)
        self.root.focus_force()
        self.root.overrideredirect(True)

        Label(self.root, text = "Login", font = ("goudy old style", 32, "bold"), fg = "darkred", bg = "white", bd = 0).place(x = 0, y = 20, relwidth = 1, height = 70)

        self.setting_image = PhotoImage(file = "Icons/settings1.png")
        self.setting_image = self.setting_image.subsample(8, 8)
        Button(self.root, image = self.setting_image, command = self.setting_cmd, bd = 0, relief = GROOVE, cursor = "hand2", bg = "white", activebackground = "white").place(x = 10, y = 15, width = 80, height = 80)

        self.close_image = PhotoImage(file = "Icons/cross.png")
        self.close_image = self.close_image.subsample(8, 8)
        Button(self.root, image = self.close_image, command = self.root.destroy, bd = 0, relief = GROOVE, cursor = "hand2", bg = "white", activebackground = "white").place(x = 920, y = 15, width = 80, height = 80)

        self.username = StringVar()
        Label(self.root, text = "Username", font = ("goudy old style", 20, "bold"), fg = "darkblue", bg = "white").place(x = 65, y = 140)
        Entry(self.root, textvariable = self.username, font = ("goudy old style", 20), bd = 2, relief = SUNKEN, bg = "white").place(x = 200, y = 140, width = 720)

        Label(self.root, text = "Password", font = ("goudy old style", 20, "bold"), fg = "darkblue", bg = "white").place(x = 65, y = 250)

        self.password_frame = LabelFrame(self.root, bg = "grey", bd = 2, relief = RIDGE)
        self.password_frame.place(x = 200, y = 220, width = 720, height = 323)

        self.var_1 = PhotoImage(file = "Password_Images/1.png")
        self.var_1 = self.var_1.subsample(8, 8)

        self.var_2 = PhotoImage(file = "Password_Images/2.png")
        self.var_2 = self.var_2.subsample(8, 8)

        self.var_3 = PhotoImage(file = "Password_Images/3.png")
        self.var_3 = self.var_3.subsample(8, 8)

        self.var_4 = PhotoImage(file = "Password_Images/4.png")
        self.var_4 = self.var_4.subsample(8, 8)

        self.var_5 = PhotoImage(file = "Password_Images/5.png")
        self.var_5 = self.var_5.subsample(8, 8)

        self.var_6 = PhotoImage(file = "Password_Images/6.png")
        self.var_6 = self.var_6.subsample(8, 8)

        self.var_7 = PhotoImage(file = "Password_Images/7.png")
        self.var_7 = self.var_7.subsample(8, 8)

        self.var_8 = PhotoImage(file = "Password_Images/8.png")
        self.var_8 = self.var_8.subsample(8, 8)

        self.var_9 = PhotoImage(file = "Password_Images/9.png")
        self.var_9 = self.var_9.subsample(8, 8)

        self.var_11 = PhotoImage(file = "Password_Images/10.png")
        self.var_11 = self.var_11.subsample(8, 8)

        self.var_12 = PhotoImage(file = "Password_Images/11.png")
        self.var_12 = self.var_12.subsample(8, 8)

        self.var_13 = PhotoImage(file = "Password_Images/12.png")
        self.var_13 = self.var_13.subsample(8, 8)

        self.var_14 = PhotoImage(file = "Password_Images/13.png")
        self.var_14 = self.var_14.subsample(8, 8)

        self.var_15 = PhotoImage(file = "Password_Images/14.png")
        self.var_15 = self.var_15.subsample(8, 8)

        self.var_16 = PhotoImage(file = "Password_Images/15.png")
        self.var_16 = self.var_16.subsample(8, 8)

        self.var_17 = PhotoImage(file = "Password_Images/16.png")
        self.var_17 = self.var_17.subsample(8, 8)

        self.var_18 = PhotoImage(file = "Password_Images/17.png")
        self.var_18 = self.var_18.subsample(8, 8)

        self.var_19 = PhotoImage(file = "Password_Images/18.png")
        self.var_19 = self.var_19.subsample(8, 8)

        self.var_21 = PhotoImage(file = "Password_Images/19.png")
        self.var_21 = self.var_21.subsample(8, 8)

        self.var_22 = PhotoImage(file = "Password_Images/20.png")
        self.var_22 = self.var_22.subsample(8, 8)

        self.var_23 = PhotoImage(file = "Password_Images/21.png")
        self.var_23 = self.var_23.subsample(8, 8)

        self.var_24 = PhotoImage(file = "Password_Images/22.png")
        self.var_24 = self.var_24.subsample(8, 8)

        self.var_25 = PhotoImage(file = "Password_Images/23.png")
        self.var_25 = self.var_25.subsample(8, 8)

        self.var_26 = PhotoImage(file = "Password_Images/24.png")
        self.var_26 = self.var_26.subsample(8, 8)

        self.var_27 = PhotoImage(file = "Password_Images/25.png")
        self.var_27 = self.var_27.subsample(8, 8)

        self.var_28 = PhotoImage(file = "Password_Images/26.png")
        self.var_28 = self.var_28.subsample(8, 8)

        self.var_29 = PhotoImage(file = "Password_Images/27.png")
        self.var_29 = self.var_29.subsample(8, 8)

        self.var_31 = PhotoImage(file = "Password_Images/28.png")
        self.var_31 = self.var_31.subsample(8, 8)

        self.var_32 = PhotoImage(file = "Password_Images/29.png")
        self.var_32 = self.var_32.subsample(8, 8)

        self.var_33 = PhotoImage(file = "Password_Images/30.png")
        self.var_33 = self.var_33.subsample(8, 8)

        self.var_34 = PhotoImage(file = "Password_Images/31.png")
        self.var_34 = self.var_34.subsample(8, 8)

        self.var_35 = PhotoImage(file = "Password_Images/32.png")
        self.var_35 = self.var_35.subsample(8, 8)

        self.var_36 = PhotoImage(file = "Password_Images/33.png")
        self.var_36 = self.var_36.subsample(8, 8)

        self.var_37 = PhotoImage(file = "Password_Images/34.png")
        self.var_37 = self.var_37.subsample(8, 8)

        self.var_38 = PhotoImage(file = "Password_Images/35.png")
        self.var_38 = self.var_38.subsample(8, 8)

        self.var_39 = PhotoImage(file = "Password_Images/36.png")
        self.var_39 = self.var_39.subsample(8, 8)

        Button(self.password_frame, image = self.var_1, text = "1", command = lambda : self.show("1"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 0, y = 0, width = 80, height = 80)
        Button(self.password_frame, image = self.var_2, text = "2", command = lambda : self.show("2"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 80, y = 0, width = 80, height = 80)
        Button(self.password_frame, image = self.var_3, text = "3", command = lambda : self.show("3"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 160, y = 0, width = 80, height = 80)
        Button(self.password_frame, image = self.var_4, text = "4", command = lambda : self.show("4"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 240, y = 0, width = 80, height = 80)
        Button(self.password_frame, image = self.var_5, text = "5", command = lambda : self.show("5"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 320, y = 0, width = 80, height = 80)
        Button(self.password_frame, image = self.var_6, text = "6", command = lambda : self.show("6"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 400, y = 0, width = 80, height = 80)
        Button(self.password_frame, image = self.var_7, text = "7", command = lambda : self.show("7"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 480, y = 0, width = 80, height = 80)
        Button(self.password_frame, image = self.var_8, text = "8", command = lambda : self.show("8"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 560, y = 0, width = 80, height = 80)
        Button(self.password_frame, image = self.var_9, text = "9", command = lambda : self.show("9"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 640, y = 0, width = 78, height = 80)

        Button(self.password_frame, image = self.var_11, text = "11", command = lambda : self.show("a"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 0, y = 80, width = 80, height = 80)
        Button(self.password_frame, image = self.var_12, text = "12", command = lambda : self.show("b"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 80, y = 80, width = 80, height = 80)
        Button(self.password_frame, image = self.var_13, text = "13", command = lambda : self.show("c"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 160, y = 80, width = 80, height = 80)
        Button(self.password_frame, image = self.var_14, text = "14", command = lambda : self.show("d"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 240, y = 80, width = 80, height = 80)
        Button(self.password_frame, image = self.var_15, text = "15", command = lambda : self.show("e"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 320, y = 80, width = 80, height = 80)
        Button(self.password_frame, image = self.var_16, text = "16", command = lambda : self.show("f"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 400, y = 80, width = 80, height = 80)
        Button(self.password_frame, image = self.var_17, text = "17", command = lambda : self.show("g"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 480, y = 80, width = 80, height = 80)
        Button(self.password_frame, image = self.var_18, text = "18", command = lambda : self.show("h"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 560, y = 80, width = 80, height = 80)
        Button(self.password_frame, image = self.var_19, text = "19", command = lambda : self.show("i"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 640, y = 80, width = 78, height = 80)

        Button(self.password_frame, image = self.var_21, text = "21", command = lambda : self.show("#"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 0, y = 160, width = 80, height = 80)
        Button(self.password_frame, image = self.var_22, text = "22", command = lambda : self.show("$"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 80, y = 160, width = 80, height = 80)
        Button(self.password_frame, image = self.var_23, text = "23", command = lambda : self.show("%"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 160, y = 160, width = 80, height = 80)
        Button(self.password_frame, image = self.var_24, text = "24", command = lambda : self.show("*"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 240, y = 160, width = 80, height = 80)
        Button(self.password_frame, image = self.var_25, text = "25", command = lambda : self.show("@"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 320, y = 160, width = 80, height = 80)
        Button(self.password_frame, image = self.var_26, text = "26", command = lambda : self.show("+"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 400, y = 160, width = 80, height = 80)
        Button(self.password_frame, image = self.var_27, text = "27", command = lambda : self.show("="), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 480, y = 160, width = 80, height = 80)
        Button(self.password_frame, image = self.var_28, text = "28", command = lambda : self.show("?"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 560, y = 160, width = 80, height = 80)
        Button(self.password_frame, image = self.var_29, text = "29", command = lambda : self.show("&"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 640, y = 160, width = 78, height = 80)

        Button(self.password_frame, image = self.var_31, text = "31", command = lambda : self.show("j"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 0, y = 240, width = 80, height = 80)
        Button(self.password_frame, image = self.var_32, text = "32", command = lambda : self.show("k"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 80, y = 240, width = 80, height = 80)
        Button(self.password_frame, image = self.var_33, text = "33", command = lambda : self.show("l"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 160, y = 240, width = 80, height = 80)
        Button(self.password_frame, image = self.var_34, text = "34", command = lambda : self.show("m"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 240, y = 240, width = 80, height = 80)
        Button(self.password_frame, image = self.var_35, text = "35", command = lambda : self.show("n"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 320, y = 240, width = 80, height = 80)
        Button(self.password_frame, image = self.var_36, text = "36", command = lambda : self.show("o"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 400, y = 240, width = 80, height = 80)
        Button(self.password_frame, image = self.var_37, text = "37", command = lambda : self.show("p"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 480, y = 240, width = 80, height = 80)
        Button(self.password_frame, image = self.var_38, text = "38", command = lambda : self.show("q"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 560, y = 240, width = 80, height = 80)
        Button(self.password_frame, image = self.var_39, text = "39", command = lambda : self.show("r"), cursor = "hand2", font = ("goudy old style", 18, "bold"), bg = "white", bd = 2, relief = RAISED).place(x = 640, y = 240, width = 78, height = 80)

        Label(self.root, text = "( Note : Please select the same picture which you have seleted at the time registration. )", fg = "black", bg = "white", font = ("", 10)).place(x = 200, y = 550)

        self.login_btn = Button(self.root, text = "Login", command = self.login_cmd, cursor = "hand2", activebackground = "white", activeforeground = "darkblue", font = ("courier", 20, "bold"), fg = "darkblue", bg = "white")
        self.login_btn.place(x = 200, y = 580, width = 300, height = 50)

        self.expression = ""

    def show(self, value):
        self.expression += value

    def login_cmd(self):
        try:
            if self.username.get() == "" or self.expression == "":
                msg.showerror("Fields Error","All fields are required !!", parent = self.root)
            else:
                query = "select * from gaps_data where username = ?"
                value = (self.username.get(),)

                cur.execute(query, value)
                result = cur.fetchall()
                for item in result:
                    _id = item[0]
                    u_name = item[1]
                    email = item[2]
                    password = item[3]

                    if self.username.get() == u_name:
                        if self.expression == password:
                            msg.showinfo("Login Information","You have logged in successfully", parent = self.root)
                        else:
                            msg.showerror("Login Information","Invalid username !", parent = self.root)
                    else:
                        msg.showerror("Login Information","Invalid password !", parent = self.root)

                    self.clear_cmd()

        except Exception as ex:
            print(ex)
            msg.showerror("Exception Error", f"Error due to {ex}", parent = self.root)

    def clear_cmd(self):
        self.username.set("")
        self.expression = ""

    def setting_cmd(self):
        pass

if __name__ == "__main__":
    root = Tk()
    obj = LoginClass(root)
    root.mainloop()
