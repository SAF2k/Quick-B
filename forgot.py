import sqlite3
import os
from tkinter import *
from tkinter import messagebox
import customtkinter
import itertools
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

PATH = os.path.dirname(os.path.realpath(__file__))

def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()
        

root = customtkinter.CTk()
root.protocol("WM_DELETE_WINDOW", Exit)

app_width=1280
app_height=768


screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

def reset_password():
        root.withdraw()
        global reset_p
        global page2
        reset_p = customtkinter.CTkToplevel()
        page2= reset_pass(reset_p)
        reset_p.mainloop()
        

def Char_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:7])


with sqlite3.connect("./Database/store.db") as db:
    cur = db.cursor()





class fogotpassword:
    def __init__(self, top=None):
        top.geometry("1280x768")
        top.resizable(0, 0)
        top.title("Fogrot Password")
#-------------------------------------------------------------------------------------------------------------
        self.frame1 = customtkinter.CTkFrame(top, width=1280, height=768, corner_radius=10)
        self.frame1.pack(padx=20, pady=20)

        self.label1 = customtkinter.CTkLabel(self.frame1, bg='#57a1f8')
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)

        self.frame2 = customtkinter.CTkFrame(
            self.frame1, width=450, height=450, corner_radius=10)
        self.frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.forgot_password = customtkinter.CTkLabel(self.frame2, fg_color=("#CCCCCC", "dimgray"),
                                                    corner_radius=8, width=350, height=60, text="Forgot Password",
                                                    text_font=("Roboto Medium", -26))
        self.forgot_password.place(relx=0.5, rely=0.17, anchor=CENTER)
        
        global emp_id

        self.entry_id = customtkinter.CTkLabel(self.frame2, text="Employee ID")
        self.entry_id.place(relx=0.3, rely=0.33, anchor=CENTER)
        
        self.employee_id = StringVar()
        
        self.emp_id = customtkinter.CTkEntry(self.frame2, width=250,
                                             height=50, placeholder_text="Employee Id",
                                             textvariable=self.employee_id)
        self.emp_id.bind("<Return>", self.is_empty)
        self.emp_id.place(relx=0.5, rely=0.42, anchor=CENTER)
        self.employee_id.trace("w", lambda *args: Char_limit(self.employee_id))

        self.entry_addr = customtkinter.CTkLabel(
            self.frame2, text="Employee Aadhar No.")
        self.entry_addr.place(relx=0.36, rely=0.55, anchor=CENTER)
        self.emp_id.bind('<FocusIn>', self.emp_in)
        self.emp_id.bind('<FocusOut>', self.emp_out)

        
        self.entry2 = customtkinter.CTkEntry(self.frame2, width=250,
                                             height=50)
        self.entry2.place(relx=0.5, rely=0.64, anchor=CENTER)
        self.entry2.bind('<FocusIn>', self.addr_in)
        self.entry2.bind('<FocusOut>', self.addr_out)
        self.entry2.bind("<Return>", self.validate)

        self.submit_button = customtkinter.CTkButton(self.frame1,  width=200,
                                                     height=40, text="Submit", command=self.validate)
        self.submit_button.place(relx=0.5, rely=0.70, anchor=CENTER)

    def is_empty(self,Event):
        entry = self.emp_id.get()
        if len(entry) == 0:
            self.emp_id.configure(border_color="red")
            messagebox.showinfo("Hello","Employee ID should not be empty")
        else:
            self.validate()
            
    def emp_in(self, e):
        self.emp_id.configure(border_color="blue")

    def emp_out(self, e):
        self.emp_id.configure(border_color="")

    def addr_in(self, e):
        self.entry2.configure(border_color="blue")

    def addr_out(self, e):
        self.entry2.configure(border_color="")
    
    def search(self,get_id,e_id):
        for i in range(len(get_id)):
            if get_id[i] == e_id:
                return True
        return False

    def search_aadhar(self,aadhar,aadhar_num):
        for i in range(len(aadhar)):
            if aadhar== aadhar_num:
                return True
        return False


    def validate(self, *args):
        global idemp
        idemp = self.emp_id.get()
        if self.emp_id.get() == "":
            self.emp_id.configure(border_color="red")
        if self.entry2.get() == "":  
            self.entry2.configure(border_color="red")
            
        get_aadhar="SELECT aadhar_num FROM employee WHERE emp_id=?"
        cur.execute(get_aadhar,[self.emp_id.get()])
        results=cur.fetchall()
        if len(results)!=0:
            aadhar=list(itertools.chain(*results))
            aadhar_num=self.entry2.get()
            if self.search_aadhar(str(aadhar[0]),aadhar_num):
                reset_password()
            else:
                messagebox.showerror("Error","Employee id and aaahar does not match")
        else:
            messagebox.showerror("Error","Emp Id doesn't found")


class reset_pass:
    def __init__(self,top=None):
        top.geometry("1280x768")
        top.resizable(0, 0)
        top.title("Fogrot Password")
        top.protocol("WM_DELETE_WINDOW", Exit)
#-------------------------------------------------------------------------------------------------------------
        self.frame1 = customtkinter.CTkFrame(top, width=1280, height=768, corner_radius=10)
        self.frame1.pack(padx=20, pady=20)

        self.label1 = customtkinter.CTkLabel(self.frame1, bg='#57a1f8', width=120, height=25)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)

        self.frame2 = customtkinter.CTkFrame(self.frame1, width=450, height=450, corner_radius=10)
        self.frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.Reset = customtkinter.CTkLabel(self.frame2, fg_color=("#CCCCCC", "dimgray"),
                                            corner_radius=8, width=350, height=60, text="Reset Password",
                                            text_font=("Roboto Medium", -26))
        self.Reset.place(relx=0.5, rely=0.17, anchor=CENTER)
        
        self.new_pass = customtkinter.CTkLabel(
            self.frame2, text="New Password")
        self.new_pass.place(relx=0.3, rely=0.33, anchor=CENTER)

        self.entry1 = customtkinter.CTkEntry(self.frame2, width=250,
                                        height=50)                       
        self.entry1.place(relx=0.5, rely=0.42, anchor=CENTER)
        self.entry1.bind('<FocusIn>', self.new_in)
        self.entry1.bind('<FocusOut>', self.new_out)
        
        self.conflabel = customtkinter.CTkLabel(
            self.frame2, text="Confirm Password")
        self.conflabel.place(relx=0.36, rely=0.55, anchor=CENTER)
        
        self.entry2 = customtkinter.CTkEntry(self.frame2, width=250,
                                        height=50)
        self.entry2.bind('<FocusIn>', self.conf_in)
        self.entry2.bind('<FocusOut>', self.conf_out)                     
        self.entry2.place(relx=0.5, rely=0.64, anchor=CENTER)
        self.entry2.bind("<Return>", self.update_pass)

        submit_button = customtkinter.CTkButton(self.frame2, width=200,text="Reset",
                                height=40,command=self.update_pass)
        submit_button.place(relx=0.5, rely=0.80, anchor=CENTER)
    
    def new_in(self, e):
        self.entry1.configure(border_color="blue")

    def new_out(self, e):
        self.entry1.configure(border_color="")
        
    def conf_in(self, e):
        self.entry2.configure(border_color="blue")

    def conf_out(self, e):
        self.entry2.configure(border_color="")

    def update_pass(self, *args):
        e_id=idemp
        if (len(self.entry1.get())<8):
            messagebox.showerror("Error","Password must be 8 or more character")
        elif self.entry1.get()==self.entry2.get():     
            update = ("UPDATE employee SET password = ? where emp_id = ?")
            cur.execute(update, [(self.entry1.get()),e_id])
            db.commit()
            messagebox.showinfo("Success!!", "Password successfully updated.")
            root.destroy()
            os.system("python Login.py")
        else:
            messagebox.showerror("Error","Password doesnot match")   
            
            
f=fogotpassword(root)
root.mainloop()