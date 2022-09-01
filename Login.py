# ==================imports===================
from multiprocessing.spawn import import_main_path
import sqlite3
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from time import strftime
import customtkinter
from PIL import ImageTk, Image
import datetime as dt

# ============================================

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1280x768+320+144")
root.title("Retail Manager(LOGIN)")
root.resizable(0, 0)

PATH = os.path.dirname(os.path.realpath(__file__))

date = dt.datetime.now()
nowDate = f"{date: %d-%m-%y}"
nowtime = f"{date: %H:%M:%S}"
print(nowtime)
print(nowDate)
#---------------------------------------------------------

def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()
        
root.protocol("WM_DELETE_WINDOW", Exit)

def forgotpass():
    messagebox.showinfo("Forgot Password","Forgot page Open Succefully")
    root.withdraw()
    os.system("python forgot.py")
    root.deiconify()


def login(*args):
    username = user.get()
    password = pas_entry.get()

    with sqlite3.connect("./Database/store.db") as db:
        cur = db.cursor()
    find_user = "SELECT * FROM employee WHERE emp_id = ? and password = ?"
    cur.execute(find_user, [username, password])
    results = cur.fetchall()
    if results:  
        if results[0][6] == "Admin":
            with open('./Database/userlogin.txt', 'w') as f:
                f.write(username)
                f.close()
            userlog = '\n'+username+'    '+nowtime+'    '+nowDate
            with open('./Database/userlog.txt', 'a') as f:
                f.write(userlog)
                f.close()
            user_entry.delete(0, END)
            pas_entry.delete(0, END)
            pas_entry.configure(border_color="")
            user_entry.configure(border_color="")
            messagebox.showinfo("Admin", "The login is successful.")
            root.withdraw()
            os.system("python admin.py")
            root.deiconify()
        else:
            userlog = '\n'+username+'    '+nowtime+'    '+nowDate
            with open('./Database/userlogin.txt', 'w') as f:
                f.write(username)
                f.close()
            with open('./Database/userlog.txt', 'a') as f:
                f.write(userlog)
                f.close()
            user_entry.delete(0, END)
            pas_entry.delete(0, END)
            pas_entry.configure(border_color="")
            user_entry.configure(border_color="")
            messagebox.showinfo("Employee", "The login is successful.")
            root.withdraw()
            os.system("python employee.py")
            root.deiconify()

    else:
        pas_entry.configure(border_color="red")
        user_entry.configure(border_color="red")
        messagebox.showerror("Error", "Incorrect username or password.")
        pas_entry.delete(0, END)


#-------------------------DESIGNE-------------------------


def change_mode():
    if switch_2.get() == 0:
        customtkinter.set_appearance_mode("dark")
        forgot_button.configure(hover_color="#333333")

    else:
        customtkinter.set_appearance_mode("light")
        forgot_button.configure(hover_color="#ffffff")


def empid_in(e):
    user_entry.configure(border_color="blue")

def empid_out(e):
    user_entry.configure(border_color="")
        

def emppas_in(e):
    pas_entry.configure(border_color="blue")

def emppas_out(e):
    pas_entry.configure(border_color="")

def show_password():
    if(showP.get()):
        pas_entry.configure(show='')
    else:
        pas_entry.configure(show='*')
        
def user_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:7])
        

def password_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:16])
      

frame1 = customtkinter.CTkFrame(root, width=1280, height=768, corner_radius=10)
frame1.pack(padx=20, pady=20)

label1 = customtkinter.CTkLabel(frame1)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)
img = ImageTk.PhotoImage(Image.open(PATH + "./images/login_bg.png").resize((1240, 700)))
label1.configure(image=img)

clock = customtkinter.CTkLabel(frame1)
clock.place(relx=0.06, rely=0.03, anchor=CENTER)

def time():
    string = strftime("%H:%M:%S %p")
    clock.configure(text=string)
    clock.after(1000, time)
time()

switch_2 = customtkinter.CTkSwitch(frame1,text="Light Mode",command=change_mode)
switch_2.place(x=20, y=40)

frame2 = customtkinter.CTkFrame(frame1, width=550, height=680, corner_radius=10)
frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

label_login = customtkinter.CTkLabel(frame2, text="LOGIN", fg_color=(
    "#CCCCCC", "dimgray"), corner_radius=8, width=370, height=80, text_font=("Roboto Medium", -32))
label_login.place(relx=0.5, rely=0.15, anchor=CENTER)

frame3 = customtkinter.CTkFrame(frame2, width=370, height=390, corner_radius=10)
frame3.place(relx=0.5, rely=0.55, anchor=CENTER)

#--------------------------------------------------------------------------------------------------------
    
user = StringVar()

user_label = customtkinter.CTkLabel(frame3, text="Employee ID")
user_label.place(relx=0.23, rely=0.08, anchor=CENTER)
        
user_entry = customtkinter.CTkEntry(frame3, width=290,height=50, 
                                    placeholder_text="Employee ID",border_width=2,
                                    corner_radius=10, textvariable=user)
user_entry.place(relx=0.5, rely=0.2, anchor=CENTER)
user_entry.focus_set()
user.trace("w", lambda *args: user_limit(user))
user_entry.bind('<FocusIn>', empid_in)
user_entry.bind('<FocusOut>', empid_out)


password = StringVar()

password_label = customtkinter.CTkLabel(frame3, text="Password")
password_label.place(relx=0.21, rely=0.33, anchor=CENTER)

pas_entry = customtkinter.CTkEntry(frame3, width=290,height=50,
                                   border_width=2, placeholder_text="Password", 
                                   corner_radius=10, textvariable=password)
pas_entry.place(relx=0.5, rely=0.45, anchor=CENTER)
pas_entry.configure(show="*")
password.trace("w", lambda *args: password_limit(password))
pas_entry.bind('<FocusIn>', emppas_in)
pas_entry.bind('<FocusOut>', emppas_out)
pas_entry.bind("<Return>", login)

#------------------------------------------------------------------------------------------------------

login_button = customtkinter.CTkButton(frame3,  width=200,
                                      height=40, text="Log In",
                                       border_width=0,
                                       corner_radius=8, command=login)
login_button.place(relx=0.5, rely=0.75, anchor=CENTER)

showP = customtkinter.CTkCheckBox(frame3, text='Show Password',
                                 onvalue=1, offvalue=0, command=show_password)
showP.place(relx=0.30, rely=0.60, anchor=CENTER)

#-------------------------------------------------------------------------------------------------------
forgot_button = customtkinter.CTkButton(frame3,  width=100,
                                      height=40, text="Forgot Password?",
                                       border_width=0,fg_color=None,hover_color="#333333",
                                       corner_radius=8,command=forgotpass)
forgot_button.place(relx=0.75, rely=0.90, anchor=CENTER)

root.mainloop()
