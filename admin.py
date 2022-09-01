
import sqlite3
import os
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
import customtkinter
import pygame
from PIL import ImageTk,Image
import time

# ============================================

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

PATH = os.path.dirname(os.path.realpath(__file__))

root = customtkinter.CTk()
root.title("Quick B")
root.state('zoomed')
root.geometry("1280x768+320+144")



user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()

with sqlite3.connect("./Database/store.db") as db:
    cur = db.cursor()


def random_emp_id(stringLength):
    Digits = string.digits
    strr = ''.join(random.choice(Digits) for i in range(stringLength-3))
    return ('EMP'+strr)


def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

def valid_pass(pswd):
    if len(pswd)>=8:
        return True
    return False

def only_character(char):
    return char.isalpha()

def only_numbers(char):
    return char.isdigit()


def isValidAadhaarNumber(str):
    
	# Regex to check valid      # Aadhaar number.
	regex = ("^[2-9]{1}[0-9]{3}\\" +
			"s[0-9]{4}\\s[0-9]{4}$")
	
	# Compile the ReGex
	p = re.compile(regex)

	# If the string is empty    # return false
	if (str == None):
		return False

	# Return if the string      # matched the ReGex
	if(re.search(p, str)):
		return True
	else:
		return False


def Char_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:20]) 

def phone_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:10])

def adhar_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:15])
        
def id_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:7])



def emp():
    root.withdraw()
    os.system("python employee.py")
    root.deiconify()

######-------audio messages-------
pygame.mixer.init()

def msg_Padd():
    pygame.mixer.music.load("./audio/productadd.mp3")
    pygame.mixer.music.play(loops=0)

def msg_Pupdate():
    pygame.mixer.music.load("./audio/productupdate.mp3")
    pygame.mixer.music.play(loops=0)

def msg_Pstatus():
    pygame.mixer.music.load("./audio/productstatus.mp3")
    pygame.mixer.music.play(loops=0)

def msg_Eadd():
    pygame.mixer.music.load("./audio/Employeeadd.mp3")
    pygame.mixer.music.play(loops=0)

def msg_Eupdate():
    pygame.mixer.music.load("./audio/Employeeupdate.mp3")
    pygame.mixer.music.play(loops=0)

def msg_Estatus():
    pygame.mixer.music.load("./audio/Employeestatus.mp3")
    pygame.mixer.music.play(loops=0)


#############--------------------------------###########################



class Admin_Page:
    def __init__(self, top = None):
        top.geometry("1280x768+320+144")
        top.resizable(0,0)
        top.title("ADMIN Mode")
        
        self.frame1 = customtkinter.CTkFrame(root, width=1280, height=768, corner_radius=10, border_color= 'blue')
        self.frame1.pack(padx=20, pady=20)
        
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1 = customtkinter.CTkLabel(
            self.frame1, bg='#57a1f8', width=120, height=25)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.label1.configure(image=self.img)

        self.frame2 = customtkinter.CTkFrame(self.frame1, width=550, height=680, corner_radius=10)
        self.frame2.place(x=30, y=25)
        
        self.frame3 = customtkinter.CTkFrame(self.frame2, width=450, height=480, corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        self.frame4 = customtkinter.CTkFrame(self.frame1, width=150, height=150, corner_radius=10)
        self.frame4.place(relx=0.91, rely=0.15, anchor=CENTER)
        
        self.switch_3 = customtkinter.CTkSwitch(self.frame4,
                                                text="Light Mode", bg_color=None,
                                                command=self.change_mode)
        self.switch_3.place(relx=0.5, rely=0.47, anchor=CENTER)

        image_size = 20

        self.logout = ImageTk.PhotoImage(Image.open(
        PATH + "./images/logout.png").resize((image_size, image_size)))
        

       
        self.button1 = customtkinter.CTkButton(self.frame4, width=120,
                                               height=32,image=self.logout,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Logout",
                                               command=self.Logout)
        self.button1.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        
        self.label_login = customtkinter.CTkLabel(self.frame2, text="ADMIN", 
                                                  fg_color=("#CCCCCC","dimgray"), 
                                                  corner_radius=8, 
                                                  width=370, height=80, 
                                                  text_font=("Roboto Medium", -32))
        self.label_login.place(relx=0.5, rely=0.13, anchor=CENTER)


        self.inventory = ImageTk.PhotoImage(Image.open(
        PATH + "./images/inventorypng.png").resize((image_size, image_size)))
        
        self.button2 = customtkinter.CTkButton(self.frame2, width=350,
                                               height=55,image=self.inventory,
                                               border_width=1,
                                               corner_radius=8,
                                               text="Inventory", 
                                               text_font=("Roboto Medium", -20),
                                               command=inventory)
        self.button2.place(relx=0.5, rely=0.35, anchor=CENTER)

        self.employee = ImageTk.PhotoImage(Image.open(
        PATH + "./images/employeelogo.png").resize((image_size, image_size)))
        self.button3 = customtkinter.CTkButton(self.frame2, width=350,
                                               height=55,image=self.employee,
                                               border_width=1,
                                               corner_radius=8,
                                               text="Employees",
                                               text_font=(
                                                   "Roboto Medium", -20),
                                               command=employee)
        self.button3.place(relx=0.5, rely=0.475, anchor=CENTER)
        
        self.invoice = ImageTk.PhotoImage(Image.open(
        PATH + "./images/invoices1.png").resize((image_size, image_size)))
        self.button4 = customtkinter.CTkButton(self.frame2, width=350,
                                               height=55,image=self.invoice,
                                               border_width=1,
                                               corner_radius=8,
                                               text="Invoices",
                                               text_font=("Roboto Medium", -20),
                                               command=invoices)
        self.button4.place(relx=0.5, rely=0.6, anchor=CENTER)


        self.about = ImageTk.PhotoImage(Image.open(
        PATH + "./images/about.png").resize((image_size, image_size)))
        self.button5 = customtkinter.CTkButton(self.frame2, width=350,
                                               height=55,image=self.about,
                                               border_width=1,
                                               corner_radius=8,
                                               text="About Us",
                                               text_font=("Roboto Medium", -20),
                                               command=about)
        self.button5.place(relx=0.5, rely=0.725, anchor=CENTER)
        

        self.bill = ImageTk.PhotoImage(Image.open(
        PATH + "./images/bill1.png").resize((image_size, image_size)))
        self.button6 = customtkinter.CTkButton(self.frame2, width=350,
                                               height=55,image=self.bill,
                                               border_width=1,
                                               corner_radius=8,
                                               text="Bill", 
                                               text_font=("Roboto Medium", -20),
                                               command=bill)
        self.button6.place(relx=0.5, rely=0.85, anchor=CENTER)
        
        self.clock = customtkinter.CTkLabel(self.frame4)
        self.clock.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.time()
        
    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.configure(text=string)
        self.clock.after(1000, self.time)

        
        

    def change_mode(self):
        if self.switch_3.get() == 0:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=root)
        if sure == True:
            root.destroy()
            os.system('Login.py')
    
def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()

def inventory():
    root.withdraw()
    global inv
    global page3
    inv = customtkinter.CTkToplevel()
    page3 = Inventory(inv)
    page3.time()
    inv.protocol("WM_DELETE_WINDOW", exitt)
    inv.mainloop()

def bill():
    messagebox.showinfo("Billing Page", "You Entered Billing Page Successfully.")
    root.withdraw()
    os.system("python employee.py")
    root.deiconify()
    
def employee():
    root.withdraw()
    global emp
    global page5
    emp = customtkinter.CTkToplevel()
    page5 = Employee(emp)
    page5.time()
    emp.protocol("WM_DELETE_WINDOW", exitt)
    emp.mainloop()


def invoices():
    root.withdraw()
    global invoice
    invoice = customtkinter.CTkToplevel()
    page7 = Invoice(invoice)
    page7.time()
    invoice.protocol("WM_DELETE_WINDOW", exitt)
    invoice.mainloop()

def about():
    root.withdraw()
    global aboutus
    aboutus = Toplevel()
    page8 = Aboutus(aboutus)
    aboutus.protocol("WM_DELETE_WINDOW", exitt)
    aboutus.mainloop()



#-----------------------------------------------------------------------------------------------------

class Inventory:
    def __init__(self, top=None):
        top.geometry("1280x768+320+144")
        top.resizable(0, 0)
        top.title("Inventory")
 
 #--------------------------------------------------frames-----------------------------------------------------
        
        self.frame1 = customtkinter.CTkFrame(inv, width=1280, height=768, corner_radius=10)
        self.frame1.pack(padx=20, pady=20)
        
        self.label1 = customtkinter.CTkLabel(
            self.frame1, bg='#57a1f8', width=120, height=25)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)
        
        self.frame2 = customtkinter.CTkFrame(self.frame1, width=300, height=680, corner_radius=10)
        self.frame2.place(x=30, y=25)
        
        self.frame3 = customtkinter.CTkFrame(self.frame2, width=250, height=180, corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.33, anchor=CENTER)
        
        self.frame4 = customtkinter.CTkFrame(self.frame1, width=450, height=50, corner_radius=10)
        self.frame4.place(relx=0.80, rely=0.07, anchor=CENTER)
        
        self.frame5 = customtkinter.CTkFrame(self.frame2, width=250, height=310, corner_radius=10)
        self.frame5.place(relx=0.5, rely=0.73, anchor=CENTER)
        
        self.frame6 = customtkinter.CTkFrame(self.frame1, width=840, height=570, corner_radius=10)
        self.frame6.place(relx=0.635, rely=0.55, anchor=CENTER)

#----------------------------------------------------------------------------------------------------------------

        self.clock = customtkinter.CTkLabel(self.frame4)
        self.clock.place(relx=0.85, rely=0.5, anchor=CENTER)


        image_size = 20
        self.logout1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/logout.png").resize((image_size,image_size)))
        
        self.button2 = customtkinter.CTkButton(self.frame4, width=120,
                                               height=32,image=self.logout1,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Logout",
                                               command=self.Logout)
        self.button2.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        self.switch_3 = customtkinter.CTkSwitch(self.frame4,
                                                text="Light Mode", bg_color=None,
                                                command=self.change_mode)
        self.switch_3.place(relx=0.15, rely=0.5, anchor=CENTER)

#-------------------------------------------------------------------------------------------------------

        self.label_login = customtkinter.CTkLabel(self.frame2, text="INVENTORY",
                                                  fg_color=("#CCCCCC", "dimgray"),
                                                  corner_radius=8,
                                                  width=250, height=70,
                                                  text_font=("Roboto Medium", -25))
        self.label_login.place(relx=0.5, rely=0.1, anchor=CENTER)
        
#-------------------------------------------------------------------------------------------------------   

        self.prod_id = StringVar()
        
        self.productid = customtkinter.CTkLabel(self.frame3, text="Product ID")
        self.productid.place(relx=0.5, rely=0.15, anchor=CENTER)

         
        validation = inv.register(only_numbers)
        p_id=StringVar()

        self.entry1 = customtkinter.CTkEntry(self.frame3, width=190,
                                             height=40, placeholder_text="Product ID",textvariable=p_id,
                                             validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        p_id.trace("w", lambda *args: id_limit(p_id))
        self.entry1.bind('<FocusIn>', self.prodectid_in)
        self.entry1.bind('<FocusOut>', self.prodectid_out)
        

        self.entry1.place(relx=0.5, rely=0.43, anchor=CENTER)
        
        self.search = ImageTk.PhotoImage(Image.open(
        PATH + "./images/search.png").resize((image_size, image_size)))

        self.button1 = customtkinter.CTkButton(self.frame3, width=150,
                                               height=35,image=self.search,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Search",
                                               command=self.search_product)                                  
        self.button1.place(relx=0.5, rely=0.75, anchor=CENTER)
        
#-----------------------------------------------------------------------------------------------------------

        self.prodoption = customtkinter.CTkLabel(self.frame5, text="Product Option")
        self.prodoption.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        self.addp = ImageTk.PhotoImage(Image.open(
        PATH + "./images/addp.png").resize((image_size,image_size)))

        self.button3 = customtkinter.CTkButton(self.frame5, width=200,
                                               height=35,image=self.addp,
                                               border_width=0,
                                               corner_radius=8,
                                               text="ADD PRODUCT",
                                               command=self.add_product)
        self.button3.place(relx=0.5, rely=0.25, anchor=CENTER)
        

        self.updatep = ImageTk.PhotoImage(Image.open(
        PATH + "./images/updatep.png").resize((image_size, image_size)))

        self.button4 = customtkinter.CTkButton(self.frame5, width=200,
                                               height=35,image=self.updatep,
                                               border_width=0,
                                               corner_radius=8,
                                               text="UPDATE PRODUCT",
                                               command=self.update_product)
        self.button4.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.deletep = ImageTk.PhotoImage(Image.open(
        PATH + "./images/deletep.png").resize((image_size, image_size)))
        
        self.button5 = customtkinter.CTkButton(self.frame5, width=200,
                                               height=35,image=self.deletep,
                                               border_width=0,
                                               corner_radius=8,
                                               text="DELETE PRODUCT",
                                               command=self.delete_product)
        self.button5.place(relx=0.5, rely=0.65, anchor=CENTER)
        

        self.back = ImageTk.PhotoImage(Image.open(
        PATH + "./images/back.png").resize((image_size, image_size)))
        self.button6 = customtkinter.CTkButton(self.frame5, width=150,
                                               height=35,image=self.back,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Back",
                                               fg_color='#FF6347',
                                               command=self.Exit)
        self.button6.place(relx=0.5, rely=0.85, anchor=CENTER)


#------------------------------------------------------------------------------------------------------------
        
        
        self.style = ttk.Style()
        self.style.theme_use("alt")
        
        self.style.configure("Treeview",
                        background='#333333',
                        foreground='#e5e5e5',
                        rowheight= 25,
                        fieldbackground='#333333',)
        
        self.tree = ttk.Treeview(self.frame6)
        self.tree.place(relx=0.5, rely=0.5, anchor=CENTER, width = 820, height = 550)
        self.tree.configure(selectmode="extended")
                         
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.tree.configure(
            columns=(
                "Product ID",
                "Name",
                "Category",
                "Sub-Category",
                "In Stock",
                "MRP",
                "Cost Price",
                "Vendor No",
                "Status.",
                
            )
        )

        self.tree.heading("Product ID", text="Product ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Category", text="Category", anchor=W)
        self.tree.heading("Sub-Category", text="Sub-Category", anchor=W)
        self.tree.heading("In Stock", text="In Stock", anchor=W)
        self.tree.heading("MRP", text="MRP", anchor=W)
        self.tree.heading("Cost Price", text="Cost Price", anchor=W)
        self.tree.heading("Vendor No", text="Vendor No", anchor=W)
        self.tree.heading("Status.", text="Status.", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=60)
        self.tree.column("#2", stretch=NO, minwidth=0, width=195)
        self.tree.column("#3", stretch=NO, minwidth=0, width=70)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.tree.column("#5", stretch=NO, minwidth=0, width=70)
        self.tree.column("#6", stretch=NO, minwidth=0, width=70)
        self.tree.column("#7", stretch=NO, minwidth=0, width=70)
        self.tree.column("#8", stretch=NO, minwidth=0, width=80)

        self.DisplayData()
        

    def change_mode(self):
        if self.switch_3.get() == 0:
            customtkinter.set_appearance_mode("dark")
            
            self.style.configure("Treeview",
                            background='#333333',
                            foreground='#e5e5e5',
                            rowheight=25,
                            fieldbackground='#333333',)
        else:
            customtkinter.set_appearance_mode("light")
            
            self.style.configure("Treeview",
                                 background='#dbdbdb',
                                 foreground='#1f2d3b',
                                 rowheight=25,
                                 fieldbackground='#dbdbdb',)
            
    def prodectid_in(self, e):
        self.entry1.configure(border_color="blue")
        
    def prodectid_out(self, e):
        self.entry1.configure(border_color="")

    def DisplayData(self):
        cur.execute("SELECT * FROM raw_inventory")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    def testint(self, val):
        if val.isdigit() and val<=20:
            return True
        elif val == "":
            return True
        return False

    def search_product(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        try:
            to_search = int(self.entry1.get())
        except ValueError:
            self.entry1.configure(border_color="red")
            messagebox.showerror("Oops!!", "Invalid Product Id.", parent=inv)
        else:
            for search in val:
                if search == to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Success!!", "Product ID: {} found.".format(
                        self.entry1.get()), parent=inv)
                    break
            else:
                messagebox.showerror("Oops!!", "Product ID: {} not found.".format(
                    self.entry1.get()), parent=inv)

    sel = []

    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_product(self):
        val = []
        to_delete = []

        if len(self.sel)==1:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to disable the selected products?", parent=inv)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                        
                
                for j in range(len(val)):
                    if j%9==0:
                        to_delete.append(val[j])
                        
                
                for k in to_delete:
                    get_status="SELECT * FROM raw_inventory WHERE product_id=?"
                    cur.execute(get_status,[k])
                    results = cur.fetchall()
                    print(results)
                    if results:
                        if results[0][8]=="Disable":
                            messagebox.showerror("Error!!","Product already disabled.")
                        else:
                            status="Disable"
                            state=(
                                    "UPDATE raw_inventory SET status=? WHERE product_id=?"
                                )
                            cur.execute(state,[status,k])
                            db.commit()
                            msg_Pstatus()
                            messagebox.showinfo("Success!!", "Product disabled from database.", parent=inv)
                            self.sel.clear()
                            self.tree.delete(*self.tree.get_children())
                            self.DisplayData()
        elif len(self.sel)==0:
            messagebox.showerror("Error!!","Please select a product.", parent=inv)
        else:
            messagebox.showerror("Error","Can only disable one product at a time.", parent=inv)

    def update_product(self):
        if len(self.sel) == 1:
            global p_update
            p_update = customtkinter.CTkToplevel()
            page9 = Update_Product(p_update)
            p_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global valll
            valll = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    valll.append(j)
            page9.entry1.insert(0, valll[1])
            page9.entry2.insert(0, valll[2])
            page9.entry3.insert(0, valll[3])
            page9.entry4.insert(0, int(valll[4]))
            page9.entry5.insert(0, int(valll[5]))
            page9.entry6.insert(0, int(valll[6]))
            page9.entry7.insert(0, int(valll[7]))
            page9.combobox.set(valll[8])

            with open('./Database/currentuser.txt', 'w') as f:
                f.write(page9.entry1.get())
                f.close()
            p_update.mainloop()

        elif len(self.sel) == 0:
            messagebox.showerror(
                "Error", "Please choose a product to update.", parent=inv)
        else:
            messagebox.showerror(
                "Error", "Can only update one product at a time.", parent=inv)        

    def add_product(self):
        global p_add
        global page4
        p_add = customtkinter.CTkToplevel()
        page4 = add_product(p_add)
        p_add.mainloop()

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.configure(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=inv)
        if sure == True:
            inv.destroy()
            root.deiconify()

    def ex2(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=p_update)
        if sure == True:
            p_update.destroy()
            inv.deiconify()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?",parent=inv)
        if sure == True:
            inv.destroy()
            root.destroy()


#------------------------------------------------------------------------------------------
#===========================================================================================

class add_product:
    def __init__(self, top=None):
        top.geometry("1280x768+320+144")
        top.resizable(0, 0)
        top.title("Add Product")
        
#--------------------------------------------------------------------------------------------

        self.frame1 = customtkinter.CTkFrame(p_add, width=1280, height=768, corner_radius=10)
        self.frame1.pack(padx=20, pady=20)

        self.label1 = customtkinter.CTkLabel(self.frame1, bg='#57a1f8', width=120, height=25)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)
        
        self.frame3 = customtkinter.CTkFrame(self.frame1, width=600, height=80, corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.9, anchor=CENTER)
        
        self.frame2 = customtkinter.CTkFrame(self.frame1, width=1050, height=450, corner_radius=10)
        self.frame2.place(relx=0.5, rely=0.52, anchor=CENTER)
       
#---------------------------------------------------------------------------------

        self.add_product = customtkinter.CTkLabel(self.frame1, text="Add Product",
                                                  fg_color=("#CCCCCC", "dimgray"),
                                                  corner_radius=8,
                                                  width=370, height=80,
                                                  text_font=("Roboto Medium", -32))
        self.add_product.place(relx=0.5, rely=0.1, anchor=CENTER)
        
#---------------------------------------------------------------------------------------
        image_size = 20
        self.add1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/add.png").resize((image_size, image_size)))
        
        self.button1 = customtkinter.CTkButton(self.frame3, width=190,
                                               height=45,image=self.add1,
                                               border_width=0,
                                               corner_radius=8,
                                               text="ADD",
                                               command=self.add)
        self.button1.place(relx=0.25, rely=0.5, anchor=CENTER)
        
        
        self.clear = ImageTk.PhotoImage(Image.open(
        PATH + "./images/clear.png").resize((image_size, image_size)))

        self.button2 = customtkinter.CTkButton(self.frame3, width=190,
                                               height=45,image=self.clear,
                                               border_width=0,
                                               corner_radius=8,
                                               text="CLEAR",
                                               command=self.clearr)
        self.button2.place(relx=0.75, rely=0.5, anchor=CENTER)
        
#----------------------------------------------------------------------------------------

        self.product_name = customtkinter.CTkLabel( self.frame2, text="Product Name")
        self.product_name.place(relx=0.120, rely=0.1, anchor=CENTER)
        
        self.p_name=StringVar()
       
        self.entry1 = customtkinter.CTkEntry(self.frame2, width=890,
                                             height=40, placeholder_text="Product Name",
                                             border_width=2, corner_radius=10,textvariable=self.p_name)
        self.entry1.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.p_name.trace("w", lambda *args: Char_limit(self.p_name))
        self.entry1.bind('<FocusIn>', self.pname_in)
        self.entry1.bind('<FocusOut>', self.pname_out)


#----------------------------------------------------------------------------------------------
        
        self.product_catagory = customtkinter.CTkLabel(self.frame2, text="Product Catagory")
        self.product_catagory.place(relx=0.130, rely=0.3, anchor=CENTER)
        
        self.Pcategory=StringVar()
        validation = p_add.register(only_character)
        
        self.entry2 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Product Catagory",
                                             textvariable=self.Pcategory,validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        self.entry2.place(relx=0.275, rely=0.4, anchor=CENTER)
        self.Pcategory.trace("w", lambda *args: Char_limit(self.Pcategory))
        self.entry2.bind('<FocusIn>', self.pcat_in)
        self.entry2.bind('<FocusOut>', self.pcat_out)     
        
#-------------------------------------------------------------------------------------------------
        self.product_subcat = customtkinter.CTkLabel(self.frame2, text="Product SubCatagory")
        self.product_subcat.place(relx=0.590, rely=0.3, anchor=CENTER)

        self.Psubcat=StringVar()

        self.entry3 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Product SubCatagory",
                                              textvariable=self.Psubcat,
                                             border_width=2, corner_radius=10)
        self.entry3.place(relx=0.725, rely=0.4, anchor=CENTER)
        self.Psubcat.trace("w", lambda *args: Char_limit(self.Psubcat))
        self.entry3.bind('<FocusIn>', self.psub_in)
        self.entry3.bind('<FocusOut>', self.psub_out)

 
 #------------------------------------------------------------------------------------------------       
        self.product_quantity = customtkinter.CTkLabel(self.frame2, text="Quantity")
        self.product_quantity.place(relx=0.105, rely=0.5, anchor=CENTER)

        self.pquantity=StringVar()
        validation = p_add.register(only_numbers)


        self.entry4 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Quantity",
                                             textvariable=self.pquantity,
                                             validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        self.entry4.place(relx=0.275, rely=0.6, anchor=CENTER)
        self.pquantity.trace("w", lambda *args: Char_limit(self.pquantity))
        self.entry4.bind('<FocusIn>', self.pqty_in)
        self.entry4.bind('<FocusOut>', self.pqty_out)

        
#---------------------------------------------------------------------------------------------------
        self.cost_price = customtkinter.CTkLabel(
            self.frame2, text="Cost Price")
        self.cost_price.place(relx=0.560, rely=0.5, anchor=CENTER)
  
        self.Pcost=StringVar()
        validation = p_add.register(only_numbers)
        
        
        self.entry5 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Cost Price",
                                            textvariable=self.Pcost,validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        self.entry5.place(relx=0.725, rely=0.6, anchor=CENTER)
        self.Pcost.trace("w", lambda *args: Char_limit(self.Pcost))
        self.entry5.bind('<FocusIn>', self.cp_in)
        self.entry5.bind('<FocusOut>', self.cp_out)
        
#---------------------------------------------------------------------------------------------------
        self.product_mrp = customtkinter.CTkLabel(self.frame2, text="Selling Prive (MRP)")
        self.product_mrp.place(relx=0.13, rely=0.7, anchor=CENTER)

        self.Pmrp=StringVar()
        validation = p_add.register(only_numbers)
        
        self.entry6 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Selling Prive (MRP)",
                                            validate="key", validatecommand=(validation, '%S'),
                                            textvariable=self.Pmrp,
                                             border_width=2, corner_radius=10)
        self.entry6.place(relx=0.275, rely=0.8, anchor=CENTER)
        self.Pmrp.trace("w", lambda *args: Char_limit(self.Pmrp))
        self.entry6.bind('<FocusIn>', self.pmrp_in)
        self.entry6.bind('<FocusOut>', self.pmrp_out)

        
#----------------------------------------------------------------------------------------------------

        self.vender_no = customtkinter.CTkLabel(
            self.frame2, text="Vendor Phone Number")
        self.vender_no.place(relx=0.59, rely=0.7, anchor=CENTER)

        self.vendor=StringVar()
        validation = p_add.register(only_numbers)
        
        self.entry7 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Vendor Phone Number",
                                             textvariable=self.vendor,validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        self.entry7.place(relx=0.725, rely=0.8, anchor=CENTER)
        self.vendor.trace("w", lambda *args: phone_limit(self.vendor))
        self.entry7.bind('<FocusIn>', self.ven_in)
        self.entry7.bind('<FocusOut>', self.ven_out)


#--------------------------------------------------------------------------------------------------------
        

    def add(self):
        pqty = self.entry4.get()
        pcat = self.entry2.get()
        pmrp = self.entry6.get()
        pname = self.entry1.get()
        psubcat = self.entry2.get()
        pcp = self.entry5.get()
        pvendor = self.entry7.get()

        if pname.strip():
            if pcat.strip():
                if psubcat.strip():
                    if pqty:
                        if pcp:
                            try:
                                float(pcp)
                            except ValueError:
                                self.entry5.configure(border_color="red")
                                messagebox.showerror("Oops!", "Invalid cost price.", parent=p_add)
                            else:
                                if pmrp:
                                    try:
                                        float(pmrp)
                                    except ValueError:
                                        self.entry6.configure(border_color="red")
                                        messagebox.showerror("Oops!", "Invalid MRP.", parent=p_add)
                                    else:
                                        if valid_phone(pvendor):
                                            with sqlite3.connect("./Database/store.db") as db:
                                                cur = db.cursor()
                                            status="Enable"
                                            insert = ("INSERT INTO raw_inventory(product_name, product_cat, product_subcat, stock, mrp, cost_price, vendor_phn,status) VALUES(?,?,?,?,?,?,?,?)")
                                            cur.execute(insert, [pname, pcat, psubcat, int(pqty), float(pmrp), float(pcp), pvendor,status])
                                            msg_Padd()
                                            db.commit()
                                            messagebox.showinfo(
                                                "Success!!", "Product successfully added in inventory.", parent=p_add)
                                            p_add.destroy()
                                            page3.tree.delete(*page3.tree.get_children())
                                            page3.DisplayData()
                                            p_add.destroy()
                                        else:
                                            self.entry7.configure(border_color="red")
                                            messagebox.showerror(
                                                "Oops!", "Invalid phone number.", parent=p_add)
                                else:
                                    self.entry6.configure(border_color="red")
                                    messagebox.showerror(
                                        "Oops!", "Please enter MRP.", parent=p_add)
                        else:
                            self.entry5.configure(border_color="red")
                            messagebox.showerror(
                                "Oops!", "Please enter product cost price.", parent=p_add)
                    else:
                        self.entry4.configure(border_color="red")
                        messagebox.showerror(
                            "Oops!", "Please enter product quantity.", parent=p_add)
                else:
                    self.entry3.configure(border_color="red")
                    messagebox.showerror(
                        "Oops!", "Please enter product sub-category.", parent=p_add)
            else:
                self.entry2.configure(border_color="red")
                messagebox.showerror(
                    "Oops!", "Please enter product category.", parent=p_add)
        else:
            self.entry1.configure(border_color="red")
            messagebox.showerror(
                "Oops!", "Please enter product name", parent=p_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
 
    def pname_in(self, e):
        self.entry1.configure(border_color="blue")

    def pname_out(self, e):
        self.entry1.configure(border_color="")

    def pcat_in(self, e):
        self.entry2.configure(border_color="blue")

    def pcat_out(self, e):
        self.entry2.configure(border_color="")
        
    def psub_in(self, e):
        self.entry3.configure(border_color="blue")

    def psub_out(self, e):
        self.entry3.configure(border_color="")

    def pqty_in(self, e):
        self.entry4.configure(border_color="blue")

    def pqty_out(self, e):
        self.entry4.configure(border_color="")
        
    def cp_in(self, e):
        self.entry5.configure(border_color="blue")

    def cp_out(self, e):
        self.entry5.configure(border_color="")
    
    def pmrp_in(self, e):
        self.entry6.configure(border_color="blue")

    def pmrp_out(self, e):
        self.entry6.configure(border_color="")
        
    def ven_in(self, e):
        self.entry7.configure(border_color="blue")

    def ven_out(self, e):
        self.entry7.configure(border_color="")
#==================================================================================
        
class Update_Product:
    def __init__(self, top=None):
        top.geometry("1280x768+320+144")
        top.resizable(0, 0)
        top.title("Add Product")
        
#--------------------------------------------------------------------------------------------

        self.frame1 = customtkinter.CTkFrame(
            p_update, width=1280, height=768, corner_radius=10)
        self.frame1.pack(padx=20, pady=20)
        

        self.label1 = customtkinter.CTkLabel(
            self.frame1, bg='#57a1f8', width=120, height=25)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)

        self.frame3 = customtkinter.CTkFrame(
            self.frame1, width=600, height=80, corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.frame2 = customtkinter.CTkFrame(
            self.frame1, width=1050, height=450, corner_radius=10)
        self.frame2.place(relx=0.5, rely=0.52, anchor=CENTER)

#---------------------------------------------------------------------------------

        self.update_product = customtkinter.CTkLabel(self.frame1, text="Update Product",
                                                     fg_color=(
                                                         "#CCCCCC", "dimgray"),
                                                     corner_radius=8,
                                                     width=370, height=80,
                                                     text_font=("Roboto Medium", -32))
        self.update_product.place(relx=0.5, rely=0.1, anchor=CENTER)

#---------------------------------------------------------------------------------------
        image_size = 20
        self.update1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/updatep.png").resize((image_size,image_size)))
     
        self.button1 = customtkinter.CTkButton(self.frame3, width=190,
                                               height=45,image=self.update1,
                                               border_width=0,
                                               corner_radius=8,
                                               text="UPDATE",
                                               command=self.update)
        self.button1.place(relx=0.25, rely=0.5, anchor=CENTER)

        self.clear1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/clear.png").resize((image_size,image_size)))

        self.button2 = customtkinter.CTkButton(self.frame3, width=190,
                                               height=45,image=self.clear1,
                                               border_width=0,
                                               corner_radius=8,
                                               text="CLEAR",
                                               command=self.clearr)
        self.button2.place(relx=0.75, rely=0.5, anchor=CENTER)

#----------------------------------------------------------------------------------------

        self.product_name = customtkinter.CTkLabel(
            self.frame2, text="Product Name")
        self.product_name.place(relx=0.120, rely=0.1, anchor=CENTER)

        p_name=StringVar()
        
        self.entry1 = customtkinter.CTkEntry(self.frame2, width=890,
                                             height=40, placeholder_text="Product Name",textvariable=p_name,
                                             border_width=2, corner_radius=10)
        self.entry1.place(relx=0.5, rely=0.2, anchor=CENTER)
        p_name.trace("w", lambda *args: Char_limit(p_name))
        self.entry1.bind('<FocusIn>', self.pname_in)
        self.entry1.bind('<FocusOut>', self.pname_out)
       
#----------------------------------------------------------------------------------------------

        self.product_catagory = customtkinter.CTkLabel(
            self.frame2, text="Product Catagory")
        self.product_catagory.place(relx=0.130, rely=0.3, anchor=CENTER)

        Pcategory=StringVar()
        validation = p_update.register(only_character)

        self.entry2 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Product Catagory",
                                             textvariable=Pcategory,validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        self.entry2.place(relx=0.275, rely=0.4, anchor=CENTER)
        Pcategory.trace("w", lambda *args: Char_limit(Pcategory))
        self.entry2.bind('<FocusIn>', self.pcat_in)
        self.entry2.bind('<FocusOut>', self.pcat_out)

#-------------------------------------------------------------------------------------------------
        self.product_subcat = customtkinter.CTkLabel(
            self.frame2, text="Product SubCatagory")
        self.product_subcat.place(relx=0.590, rely=0.3, anchor=CENTER)

        Psubcat=StringVar()

        self.entry3 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Product SubCatagory",
                                             textvariable=Psubcat,
                                             border_width=2,corner_radius=10)
        self.entry3.place(relx=0.725, rely=0.4, anchor=CENTER)
        Psubcat.trace("w", lambda *args: Char_limit(Psubcat))
        self.entry3.bind('<FocusIn>', self.psub_in)
        self.entry3.bind('<FocusOut>', self.psub_out)
        
 #------------------------------------------------------------------------------------------------
       
        self.product_quantity = customtkinter.CTkLabel(self.frame2, text="Quantity")
        self.product_quantity.place(relx=0.105, rely=0.5, anchor=CENTER)
        
        validation = p_update.register(only_numbers)


        self.entry4 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Quantity",validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        self.entry4.place(relx=0.275, rely=0.6, anchor=CENTER)
        self.entry4.bind('<FocusIn>', self.pqty_in)
        self.entry4.bind('<FocusOut>', self.pqty_out)

#---------------------------------------------------------------------------------------------------
        self.cost_price = customtkinter.CTkLabel(
            self.frame2, text="Cost Price")
        self.cost_price.place(relx=0.560, rely=0.5, anchor=CENTER)
        
        Pcost=StringVar()
        validation = p_update.register(only_numbers)

        self.entry5 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Cost Price",validate="key", validatecommand=(validation, '%S'),
                                             textvariable=Pcost,
                                             border_width=2, corner_radius=10)
        self.entry5.place(relx=0.725, rely=0.6, anchor=CENTER)
        self.entry5.bind('<FocusIn>', self.cp_in)
        self.entry5.bind('<FocusOut>', self.cp_out)

#---------------------------------------------------------------------------------------------------
        self.product_mrp = customtkinter.CTkLabel(
            self.frame2, text="Selling Price (MRP)")
        self.product_mrp.place(relx=0.13, rely=0.7, anchor=CENTER)
        
        Pmrp=StringVar()
        validation = p_update.register(only_numbers)

        self.entry6 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Selling Price (MRP)",
                                             validate="key", validatecommand=(validation, '%S'),
                                             textvariable=Pmrp)
        self.entry6.place(relx=0.275, rely=0.8, anchor=CENTER)
        self.entry6.bind('<FocusIn>', self.pmrp_in)
        self.entry6.bind('<FocusOut>', self.pmrp_out)

#----------------------------------------------------------------------------------------------------

        self.vender_no = customtkinter.CTkLabel(
            self.frame2, text="Vendor Phone Number")
        self.vender_no.place(relx=0.59, rely=0.7, anchor=CENTER)
        
        validation = p_update.register(only_numbers)
        self.entry7 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Vendor Phone Number",validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        self.entry7.place(relx=0.725, rely=0.8, anchor=CENTER) 
        self.entry7.bind('<FocusIn>', self.ven_in)
        self.entry7.bind('<FocusOut>', self.ven_out)

#--------------------------------------------------------------------------------------------------------

        self.value=customtkinter.StringVar(value="hi")
        self.combobox = customtkinter.CTkComboBox(self.frame2,
                                            values=["Disable", "Enable"],variable=self.value,
                                            command=self.disenable,state="readonly",text_color="black")
        self.combobox.place(relx=0.500, rely=0.92, anchor=CENTER) 
        

        
#--------------------------------------------------------------------------------------------------
    def disenable(self,choice):
        if choice=="Disable":
            self.entry1.configure(state="disabled")
            self.entry2.configure(state="disabled")
            self.entry3.configure(state="disabled")
            self.entry4.configure(state="disabled")
            self.entry5.configure(state="disabled")
            self.entry6.configure(state="disabled")
            self.entry7.configure(state="disabled")
        elif choice=="Enable":
            self.entry1.configure(state="normal")
            self.entry2.configure(state="normal")
            self.entry3.configure(state="normal")
            self.entry4.configure(state="normal")
            self.entry5.configure(state="normal")
            self.entry6.configure(state="normal")
            self.entry7.configure(state="normal")


#------------------------------------------------------------------------------------------------
    def update(self):
        pqty = self.entry4.get()
        pcat = self.entry2.get()
        pmrp = self.entry6.get()
        pname = self.entry1.get()
        psubcat = self.entry3.get()
        pcp = self.entry5.get()
        pvendor = self.entry7.get()
        status=self.combobox.get()
        
      
        
        if pname.strip():
            if pcat.strip():
                if psubcat.strip():
                    if pqty:
                        if pcp:
                            try:
                                float(pcp)
                            except ValueError:
                                self.entry5.configure(border_color="red")
                                messagebox.showerror(
                                    "Oops!", "Invalid cost price.", parent=p_update)
                            else:
                                if pmrp:
                                    try:
                                        float(pmrp)
                                    except ValueError:
                                        self.entry6.configure(border_color="red")
                                        messagebox.showerror(
                                            "Oops!", "Invalid MRP.", parent=p_update)
                                    else:
                                        if valid_phone(pvendor):
                                            product_id = valll[0]
                                            with sqlite3.connect("./Database/store.db") as db:
                                                cur = db.cursor()
                                            update = (
                                                "UPDATE raw_inventory SET product_name = ?, product_cat = ?, product_subcat = ?, stock = ?, mrp = ?, cost_price = ?, vendor_phn = ?,status = ?WHERE product_id = ?"
                                            )
                                            cur.execute(update, [pname, pcat, psubcat, int(
                                                pqty), float(pmrp), float(pcp), pvendor,status, product_id])
                                            db.commit()
                                            msg_Pupdate()
                                            messagebox.showinfo(
                                                "Success!!", "Product successfully updated in inventory.", parent=p_update)
                                            valll.clear()
                                            Inventory.sel.clear()
                                            page3.tree.delete(
                                                *page3.tree.get_children())
                                            page3.DisplayData()
                                            p_update.destroy()
                                        else:
                                            self.entry7.configure(border_color="red")
                                            messagebox.showerror(
                                                "Oops!", "Invalid phone number.", parent=p_update)
                                else:
                                    self.entry6.configure(border_color="red")
                                    messagebox.showerror(
                                        "Oops!", "Please enter MRP.", parent=p_update)
                        else:
                            self.entry5.configure(border_color="red")
                            messagebox.showerror(
                            "Oops!", "Please enter product cost price.", parent=p_update)
                    else:
                        self.entry4.configure(border_color="red")
                        messagebox.showerror(
                            "Oops!", "Please enter product quantity.", parent=p_update)
                else:
                    self.entry3.configure(border_color="red")
                    messagebox.showerror(
                        "Oops!", "Please enter product sub-category.", parent=p_update)
            else:
                self.entry2.configure(border_color="red")
                messagebox.showerror(
                    "Oops!", "Please enter product category.", parent=p_update)
        else:
            self.entry1.configure(border_color="red")
            messagebox.showerror(
                "Oops!", "Please enter product name", parent=p_update)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        
    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False

    def pname_in(self, e):
        self.entry1.configure(border_color="blue")

    def pname_out(self, e):
        self.entry1.configure(border_color="")

    def pcat_in(self, e):
        self.entry2.configure(border_color="blue")

    def pcat_out(self, e):
        self.entry2.configure(border_color="")

    def psub_in(self, e):
        self.entry3.configure(border_color="blue")

    def psub_out(self, e):
        self.entry3.configure(border_color="")

    def pqty_in(self, e):
        self.entry4.configure(border_color="blue")

    def pqty_out(self, e):
        self.entry4.configure(border_color="")

    def cp_in(self, e):
        self.entry5.configure(border_color="blue")

    def cp_out(self, e):
        self.entry5.configure(border_color="")

    def pmrp_in(self, e):
        self.entry6.configure(border_color="blue")

    def pmrp_out(self, e):
        self.entry6.configure(border_color="")

    def ven_in(self, e):
        self.entry7.configure(border_color="blue")

    def ven_out(self, e):
        self.entry7.configure(border_color="")

#=============================================================================

class Employee:
    def __init__(self, top=None):
        top.geometry("1280x768+320+144")
        top.resizable(0, 0)
        top.title("Employee Management")

 #--------------------------------------------------frames-----------------------------------------------------

        self.frame1 = customtkinter.CTkFrame(
            emp, width=1280, height=768, corner_radius=10)
        self.frame1.pack(padx=20, pady=20)

        self.label1 = customtkinter.CTkLabel(
            self.frame1, bg='#57a1f8', width=120, height=25)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)

        self.frame2 = customtkinter.CTkFrame(
            self.frame1, width=300, height=680, corner_radius=10)
        self.frame2.place(x=30, y=25)

        self.frame3 = customtkinter.CTkFrame(
            self.frame2, width=250, height=180, corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.33, anchor=CENTER)

        self.frame4 = customtkinter.CTkFrame(
            self.frame1, width=450, height=50, corner_radius=10)
        self.frame4.place(relx=0.80, rely=0.07, anchor=CENTER)

        self.frame5 = customtkinter.CTkFrame(
            self.frame2, width=250, height=310, corner_radius=10)
        self.frame5.place(relx=0.5, rely=0.73, anchor=CENTER)

        self.frame6 = customtkinter.CTkFrame(
            self.frame1, width=840, height=570, corner_radius=10)
        self.frame6.place(relx=0.635, rely=0.55, anchor=CENTER)
        
#----------------------------------------------------------------------------------------------------------------

        self.clock = customtkinter.CTkLabel(self.frame4)
        self.clock.place(relx=0.85, rely=0.5, anchor=CENTER)

        image_size = 20
        self.logout1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/logout.png").resize((image_size,image_size)))

        self.button2 = customtkinter.CTkButton(self.frame4, width=120,
                                               height=32,
                                               border_width=0,image=self.logout1,
                                               corner_radius=8,
                                               text="Logout",
                                               command=self.Logout)
        self.button2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.switch_3 = customtkinter.CTkSwitch(self.frame4,
                                                text="Light Mode", bg_color=None,
                                                command=self.change_mode)
        self.switch_3.place(relx=0.15, rely=0.5, anchor=CENTER)

#-------------------------------------------------------------------------------------------------------
        
        self.label_emp = customtkinter.CTkLabel(self.frame2, text="EMPLOYEES",
                                                  fg_color=(
                                                      "#CCCCCC", "dimgray"),
                                                  corner_radius=8,
                                                  width=250, height=70,
                                                  text_font=("Roboto Medium", -25))
        self.label_emp.place(relx=0.5, rely=0.1, anchor=CENTER)

#-------------------------------------------------------------------------------------------------------
        

        self.emp_id = customtkinter.CTkLabel(self.frame3, text="Employee ID")
        self.emp_id.place(relx=0.5, rely=0.15, anchor=CENTER)
         
        e_id=StringVar()

        self.entry1 = customtkinter.CTkEntry(self.frame3, width=190,
                                             height=40, placeholder_text="Employee ID",
                                             textvariable=e_id,
                                             border_width=2, corner_radius=10)
        self.entry1.place(relx=0.5, rely=0.43, anchor=CENTER)
        e_id.trace("w", lambda *args: id_limit(e_id))
        self.entry1.bind('<FocusIn>', self.prodectid_in)
        self.entry1.bind('<FocusOut>', self.prodectid_out)

        self.search = ImageTk.PhotoImage(Image.open(
        PATH + "./images/search.png").resize((image_size, image_size)))

        self.button1 = customtkinter.CTkButton(self.frame3, width=150,
                                               height=35,
                                               border_width=0,image=self.search,
                                               corner_radius=8,
                                               text="Search",
                                               command=self.search_emp)
        self.button1.place(relx=0.5, rely=0.75, anchor=CENTER)

#-----------------------------------------------------------------------------------------------------------

        self.prodoption = customtkinter.CTkLabel(
            self.frame5, text="Employee Option")
        self.prodoption.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.addp = ImageTk.PhotoImage(Image.open(
        PATH + "./images/add.png").resize((image_size,image_size)))

        self.button3 = customtkinter.CTkButton(self.frame5, width=200,
                                               height=35,
                                               border_width=0,image=self.addp,
                                               corner_radius=8,
                                               text="ADD EMPLOYEE",
                                               command=self.add_emp)
        self.button3.place(relx=0.5, rely=0.25, anchor=CENTER)

        self.updatep = ImageTk.PhotoImage(Image.open(
        PATH + "./images/updatep.png").resize((image_size, image_size)))
        
        self.button4 = customtkinter.CTkButton(self.frame5, width=200,
                                               height=35,
                                               border_width=0,
                                               corner_radius=8,image=self.updatep,
                                               text="UPDATE EMPLOYEE",
                                               command=self.update_emp)
        self.button4.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.deletep = ImageTk.PhotoImage(Image.open(
        PATH + "./images/deletep.png").resize((image_size, image_size)))

        self.button5 = customtkinter.CTkButton(self.frame5, width=200,
                                               height=35,
                                               border_width=0,
                                               corner_radius=8,image=self.deletep,
                                               text="DELETE EMPLOYEE",
                                               command=self.delete_emp)
        self.button5.place(relx=0.5, rely=0.65, anchor=CENTER)


        self.back1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/back.png").resize((image_size, image_size)))

        self.button6 = customtkinter.CTkButton(self.frame5, width=150,
                                               height=35,image=self.back1,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Back",
                                               fg_color='#FF6347',
                                               command=self.Exit)
        self.button6.place(relx=0.5, rely=0.85, anchor=CENTER)
        
        self.style = ttk.Style()
        self.style.theme_use("alt")
        
        self.style.configure("Treeview",
                        background='#333333',
                        foreground='#e5e5e5',
                        rowheight= 25,
                        fieldbackground='#333333',)
        
        self.tree = ttk.Treeview(self.frame6)
        self.tree.place(relx=0.5, rely=0.5, anchor=CENTER, width = 820, height = 550)
        self.tree.configure(selectmode="extended")
                         
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.tree.configure(
            columns=(
                "Employee ID",
                "Employee Name",
                "Contact No.",
                "Address",
                "Aadhar No.",
                "Password",
                "Designation",
                "Status"
            )
        )

        self.tree.heading("Employee ID", text="Employee ID", anchor=W)
        self.tree.heading("Employee Name", text="Employee Name", anchor=W)
        self.tree.heading("Contact No.", text="Contact No.", anchor=W)
        self.tree.heading("Address", text="Address", anchor=W)
        self.tree.heading("Aadhar No.", text="Aadhar No.", anchor=W)
        self.tree.heading("Password", text="Password", anchor=W)
        self.tree.heading("Designation", text="Designation", anchor=W)
        self.tree.heading("Status", text="Status", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=120)
        self.tree.column("#3", stretch=NO, minwidth=0, width=90)
        self.tree.column("#4", stretch=NO, minwidth=0, width=170)
        self.tree.column("#5", stretch=NO, minwidth=0, width=100)
        self.tree.column("#6", stretch=NO, minwidth=0, width=90)
        self.tree.column("#7", stretch=NO, minwidth=0, width=90)
        self.tree.column("#8", stretch=NO, minwidth=0, width=90)

        self.DisplayData()

    def DisplayData(self):
        cur.execute("SELECT * FROM employee")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))
    
    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False
    
    def prodectid_in(self, e):
        self.entry1.configure(border_color="blue")

    def prodectid_out(self, e):
        self.entry1.configure(border_color="")
            
    def change_mode(self):
        if self.switch_3.get() == 0:
            customtkinter.set_appearance_mode("dark")

            self.style.configure("Treeview",
                                 background='#333333',
                                 foreground='#e5e5e5',
                                 rowheight=25,
                                 fieldbackground='#333333',)
        else:
            customtkinter.set_appearance_mode("light")

            self.style.configure("Treeview",
                                 background='#dbdbdb',
                                 foreground='#1f2d3b',
                                 rowheight=25,
                                 fieldbackground='#dbdbdb',)

    def search_emp(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search == to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Employee ID: {} found.".format(
                    self.entry1.get()), parent=emp)
                break
        else:
            self.entry1.configure(border_color="red")
            messagebox.showerror("Oops!!", "Employee ID: {} not found.".format(
                self.entry1.get()), parent=emp)

    sel = []

    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_emp(self):
        val = []
        to_delete = []

        if len(self.sel)==1:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to change the status of selected employee(s)?", parent=emp)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%8==0:
                        to_delete.append(val[j])
                
                flag = 1

                for k in to_delete:
                    if k=="EMP0000":
                        flag = 0
                        break
                    get_status="SELECT * FROM employee WHERE emp_id=?"
                    cur.execute(get_status,[k])
                    results = cur.fetchall()
                    print(results)
                    if results:
                        if results[0][7]=="Disable":
                            messagebox.showerror("Error!!","Employee already disabled.")
                        else:
                            status="Disable"
                            state=(
                                    "UPDATE employee SET status=? WHERE emp_id=?"
                                )
                            cur.execute(state,[status,k])
                            db.commit()

                            if flag==1:
                                msg_Estatus()
                                messagebox.showinfo("Success!!", "Employee(s) status changed in database.", parent=emp)
                                self.sel.clear()
                                self.tree.delete(*self.tree.get_children())
                                self.DisplayData()
                            else:
                                messagebox.showerror("Error!!","Cannot delete master admin.")
        elif len(self.sel)==0:
            messagebox.showerror("Error!!","Please select an employee.", parent=emp)
        else:
            messagebox.showerror("Error","Can only disable  one Employee at a time.", parent=emp)      
                    

    def update_emp(self):
        if len(self.sel) == 1:
            global e_update
            e_update = customtkinter.CTkToplevel()
            page8 = Update_Employee(e_update)
            e_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)

            page8.entry1.insert(0, vall[1])
            page8.entry2.insert(0, vall[2])
            page8.entry3.insert(0, vall[4])
            page8.entry4.insert(0, vall[6])
            page8.entry4.configure(state="disabled")
            page8.entry5.insert(0, vall[3])
            page8.entry6.insert(0, vall[5])
            page8.combobox.set(vall[7])
            e_update.mainloop()
        elif len(self.sel) == 0:
            messagebox.showerror(
                "Error", "Please select an employee to update.")
        else:
            messagebox.showerror(
                "Error", "Can only update one employee at a time.")

        # try:
        #     with open('./Database/currentuser.txt', 'w') as f:
        #         f.write(vall[1])
        #         f.close()
              
        # except IndexError:
        #     pass
        

    def add_emp(self):
        global e_add
        e_add = customtkinter.CTkToplevel()
        page6 = add_employee(e_add)
        e_add.protocol("WM_DELETE_WINDOW", self.ex)
        e_add.mainloop()

    def ex(self):
        e_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()

    def ex2(self):
        e_update.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.configure(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=emp)
        if sure == True:
            emp.destroy()
            root.deiconify()

    def Logout(self):
        sure = messagebox.askyesno(
            "Logout", "Are you sure you want to logout?")
        if sure == True:
            emp.destroy()
            root.destroy()
            
#-----------------------------------------------------------------------
#------------------------------------------------------------------------


class add_employee:
    def __init__(self, top=None):
        top.geometry("1280x768+320+144")
        top.resizable(0, 0)
        top.title("Add Employee")

#--------------------------------------------------------------------------------------------

        self.frame1 = customtkinter.CTkFrame(e_add, width=1280, height=768, corner_radius=10)
        self.frame1.pack(padx=20, pady=20)

        self.label1 = customtkinter.CTkLabel(self.frame1, bg='#57a1f8', width=120, height=25)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)

        self.frame3 = customtkinter.CTkFrame(
            self.frame1, width=600, height=80, corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.frame2 = customtkinter.CTkFrame(
            self.frame1, width=1050, height=450, corner_radius=10)
        self.frame2.place(relx=0.5, rely=0.52, anchor=CENTER)

#---------------------------------------------------------------------------------

        self.add_employee = customtkinter.CTkLabel(self.frame1, text="Add Employee",
                                                  fg_color=(
                                                      "#CCCCCC", "dimgray"),
                                                  corner_radius=8,
                                                  width=370, height=80,
                                                  text_font=("Roboto Medium", -32))
        self.add_employee.place(relx=0.5, rely=0.1, anchor=CENTER)

#---------------------------------------------------------------------------------------
        
#--------------------------------------------------------------------------------------
        image_size = 20
        self.add1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/add.png").resize((image_size, image_size)))

        self.button1 = customtkinter.CTkButton(self.frame3, width=190,
                                               height=45,
                                               border_width=0,image=self.add1,
                                               corner_radius=8,
                                               text="ADD",
                                               command=self.add)
        self.button1.place(relx=0.25, rely=0.5, anchor=CENTER)

        self.clear = ImageTk.PhotoImage(Image.open(
        PATH + "./images/clear.png").resize((image_size, image_size)))
        
        self.button2 = customtkinter.CTkButton(self.frame3, width=190,
                                               height=45,
                                               border_width=0,image=self.clear,
                                               corner_radius=8,
                                               text="CLEAR",
                                               command=self.clearr)
        self.button2.place(relx=0.75, rely=0.5, anchor=CENTER)
        
#----------------------------------------------------------------------------------------
       
        self.emp_name = customtkinter.CTkLabel(
            self.frame2, text="Employee Name")
        self.emp_name.place(relx=0.130, rely=0.1, anchor=CENTER)

        self.e_name=StringVar()

        self.entry1 = customtkinter.CTkEntry(self.frame2, width=890,
                                             height=40, placeholder_text="Employee Name",
                                             textvariable=self.e_name,
                                             border_width=2, corner_radius=10)
        self.entry1.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.e_name.trace("w", lambda *args: Char_limit(self.e_name))
        self.entry1.bind('<FocusIn>', self.pname_in)
        self.entry1.bind('<FocusOut>', self.pname_out)

#----------------------------------------------------------------------------------------------

        self.contact_no = customtkinter.CTkLabel(
            self.frame2, text="Contact Number")
        self.contact_no.place(relx=0.130, rely=0.3, anchor=CENTER)

        self.contact=StringVar()
        validation = e_add.register(only_numbers)


        self.entry2 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Contact Number",
                                             textvariable=self.contact,validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        self.entry2.place(relx=0.275, rely=0.4, anchor=CENTER)
        self.contact.trace("w", lambda *args: phone_limit(self.contact))
        self.entry2.bind('<FocusIn>', self.pcat_in)
        self.entry2.bind('<FocusOut>', self.pcat_out)
        
#-------------------------------------------------------------------------------------------------
        self.emp_adhar = customtkinter.CTkLabel(
            self.frame2, text="Aadhaar Number")
        self.emp_adhar.place(relx=0.580, rely=0.3, anchor=CENTER)

        self.aadhar=StringVar()
       

        self.entry3 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Aadhaar Number",
                                             textvariable=self.aadhar,
                                             border_width=2, corner_radius=10)
        self.entry3.place(relx=0.725, rely=0.4, anchor=CENTER)
        self.aadhar.trace("w", lambda *args: adhar_limit(self.aadhar))
        self.entry3.bind('<FocusIn>', self.psub_in)
        self.entry3.bind('<FocusOut>', self.psub_out)

 #------------------------------------------------------------------------------------------------
        self.emp_des = customtkinter.CTkLabel(
            self.frame2, text="Designation")
        self.emp_des.place(relx=0.115, rely=0.5, anchor=CENTER)


        self.entry4 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40,
                                             border_width=2, corner_radius=10)
        self.entry4.insert(0,"Employee")
        self.entry4.configure(state="disabled")
        self.entry4.place(relx=0.275, rely=0.6, anchor=CENTER)
        self.entry4.bind('<FocusIn>', self.pqty_in)
        self.entry4.bind('<FocusOut>', self.pqty_out)
       
#---------------------------------------------------------------------------------------------------
        self.emp_addr = customtkinter.CTkLabel(
            self.frame2, text="Address")
        self.emp_addr.place(relx=0.555, rely=0.5, anchor=CENTER)

        self.address=StringVar()

        self.entry5 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Address",
                                            textvariable=self.address,
                                             border_width=2, corner_radius=10)
        self.entry5.place(relx=0.725, rely=0.6, anchor=CENTER)
        self.address.trace("w", lambda *args: Char_limit(self.address))
        self.entry5.bind('<FocusIn>', self.cp_in)
        self.entry5.bind('<FocusOut>', self.cp_out)
        
#---------------------------------------------------------------------------------------------------
        self.emp_pass = customtkinter.CTkLabel(
            self.frame2, text="Password")
        self.emp_pass.place(relx=0.110, rely=0.7, anchor=CENTER)

        self.epswd=StringVar()

        self.entry6 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40,textvariable=self.epswd,
                                             border_width=2, corner_radius=10)
        self.entry6.place(relx=0.275, rely=0.8, anchor=CENTER)
        self.epswd.trace("w", lambda *args: Char_limit(self.epswd))
        self.entry6.bind('<FocusIn>', self.pmrp_in)
        self.entry6.bind('<FocusOut>', self.pmrp_out)

#----------------------------------------------------------------------------------------------------

    def add(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()

        if ename.strip():
            if valid_phone(econtact):
                if isValidAadhaarNumber(eaddhar):
                    if edes:
                        if eadd:
                            if valid_pass(epass):
                                status="Enable"
                                emp_id = random_emp_id(7)
                                insert = (
                                    "INSERT INTO employee(emp_id, name, contact_num, address, aadhar_num, password, designation,status) VALUES(?,?,?,?,?,?,?,?)")
                                cur.execute(
                                    insert, [emp_id, ename, econtact, eadd, eaddhar, epass, edes,status])
                                db.commit()
                                msg_Eadd()
                                messagebox.showinfo(
                                    "Success!!", "Employee ID: {} successfully added in database.".format(emp_id), parent=e_add)
                                self.clearr()
                            else:
                                self.entry6.configure(border_color="red")
                                messagebox.showerror(
                                    "Oops!", "Password must be more than 8 character.", parent=e_add)
                        else:
                            self.entry5.configure(border_color="red")
                            messagebox.showerror(
                                "Oops!", "Please enter address.", parent=e_add)
                    else:
                        self.entry4.configure(border_color="red")
                        messagebox.showerror(
                            "Oops!", "Please enter designation.", parent=e_add)
                else:
                    self.entry3.configure(border_color="red")
                    messagebox.showerror(
                        "Oops!", "Invalid Aadhar number.", parent=e_add)
            else:
                self.entry2.configure(border_color="red")
                messagebox.showerror(
                    "Oops!", "Invalid phone number.", parent=e_add)
        else:
            self.entry1.configure(border_color="red")
            messagebox.showerror(
                "Oops!", "Please enter employee name.", parent=e_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        
    def pname_in(self, e):
        self.entry1.configure(border_color="blue")

    def pname_out(self, e):
        self.entry1.configure(border_color="")

    def pcat_in(self, e):
        self.entry2.configure(border_color="blue")

    def pcat_out(self, e):
        self.entry2.configure(border_color="")

    def psub_in(self, e):
        self.entry3.configure(border_color="blue")

    def psub_out(self, e):
        self.entry3.configure(border_color="")

    def pqty_in(self, e):
        self.entry4.configure(border_color="blue")

    def pqty_out(self, e):
        self.entry4.configure(border_color="")

    def cp_in(self, e):
        self.entry5.configure(border_color="blue")

    def cp_out(self, e):
        self.entry5.configure(border_color="")

    def pmrp_in(self, e):
        self.entry6.configure(border_color="blue")

    def pmrp_out(self, e):
        self.entry6.configure(border_color="")

# #------------------------------------------------------------------------------------
# #-------------------------------------------------------------------------------------


class Update_Employee():
    def __init__(self, top=None):
        top.geometry("1280x768+320+144")
        top.resizable(0, 0)
        top.title("Add Employee")

#--------------------------------------------------------------------------------------------

        self.frame1 = customtkinter.CTkFrame(
            e_update, width=1280, height=768, corner_radius=10)
        self.frame1.pack(padx=20, pady=20)

        self.label1 = customtkinter.CTkLabel(
            self.frame1, bg='#57a1f8', width=120, height=25)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)

        self.frame3 = customtkinter.CTkFrame(
            self.frame1, width=600, height=80, corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.frame2 = customtkinter.CTkFrame(
            self.frame1, width=1050, height=450, corner_radius=10)
        self.frame2.place(relx=0.5, rely=0.52, anchor=CENTER)

#---------------------------------------------------------------------------------

        self.add_employee = customtkinter.CTkLabel(self.frame1, text="UPDATE Employee",
                                                   fg_color=(
                                                       "#CCCCCC", "dimgray"),
                                                   corner_radius=8,
                                                   width=370, height=80,
                                                   text_font=("Roboto Medium", -32))
        self.add_employee.place(relx=0.5, rely=0.1, anchor=CENTER)

#---------------------------------------------------------------------------------------

        self.r1 = e_update.register(self.testint)
        self.r2 = e_update.register(self.testchar)

#--------------------------------------------------------------------------------------
        image_size = 20
        self.update1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/logout.png").resize((image_size,image_size)))

        self.button1 = customtkinter.CTkButton(self.frame3, width=190,
                                               height=45,
                                               border_width=0,image=self.update1,
                                               corner_radius=8,
                                               text="UPDATE",
                                               command=self.update)
        self.button1.place(relx=0.25, rely=0.5, anchor=CENTER)

        self.clear1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/clear.png").resize((image_size,image_size)))

        self.button2 = customtkinter.CTkButton(self.frame3, width=190,
                                               height=45,
                                               border_width=0,
                                               corner_radius=8,image=self.clear1,
                                               text="CLEAR",
                                               command=self.clearr)
        self.button2.place(relx=0.75, rely=0.5, anchor=CENTER)

#----------------------------------------------------------------------------------------

        self.emp_name = customtkinter.CTkLabel(
            self.frame2, text="Employee Name")
        self.emp_name.place(relx=0.130, rely=0.1, anchor=CENTER)

        self.e_name=StringVar()

        self.entry1 = customtkinter.CTkEntry(self.frame2, width=890,
                                             height=40, placeholder_text="Employee Name",
                                             textvariable=self.e_name,
                                             border_width=2, corner_radius=10)
        self.entry1.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.e_name.trace("w", lambda *args: Char_limit(self.e_name))

#----------------------------------------------------------------------------------------------

        self.contact_no = customtkinter.CTkLabel(
            self.frame2, text="Contact Number")
        self.contact_no.place(relx=0.130, rely=0.3, anchor=CENTER)

        self.contact=StringVar()
        validation = e_update.register(only_numbers)


        self.entry2 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Contact Number",
                                             textvariable=self.contact,validate="key", validatecommand=(validation, '%S'),
                                             border_width=2, corner_radius=10)
        self.entry2.place(relx=0.275, rely=0.4, anchor=CENTER)
        self.contact.trace("w", lambda *args: phone_limit(self.contact))

#-------------------------------------------------------------------------------------------------
        self.emp_adhar = customtkinter.CTkLabel(
            self.frame2, text="Aadhaar Number")
        self.emp_adhar.place(relx=0.580, rely=0.3, anchor=CENTER)

        self.aadhar=StringVar()

        self.entry3 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Aadhaar Number",
                                             border_width=2, corner_radius=10,)
        self.entry3.place(relx=0.725, rely=0.4, anchor=CENTER)
       
 #------------------------------------------------------------------------------------------------
        self.emp_des = customtkinter.CTkLabel(
            self.frame2, text="Designation")
        self.emp_des.place(relx=0.115, rely=0.5, anchor=CENTER)


        self.entry4 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40,
                                             border_width=2, corner_radius=10)
        self.entry4.place(relx=0.275, rely=0.6, anchor=CENTER)
        
#---------------------------------------------------------------------------------------------------
        self.emp_addr = customtkinter.CTkLabel(
            self.frame2, text="Address")
        self.emp_addr.place(relx=0.555, rely=0.5, anchor=CENTER)

        self.address=StringVar()
        self.entry5 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40, placeholder_text="Address",
                                             textvariable=self.address,
                                             border_width=2, corner_radius=10)
        self.entry5.place(relx=0.725, rely=0.6, anchor=CENTER)
        self.address.trace("w", lambda *args: Char_limit(self.address))
#---------------------------------------------------------------------------------------------------
        self.emp_pass = customtkinter.CTkLabel(
            self.frame2, text="Password")
        self.emp_pass.place(relx=0.110, rely=0.7, anchor=CENTER)

        self.epswd=StringVar()

        self.entry6 = customtkinter.CTkEntry(self.frame2, width=419,
                                             height=40,textvariable=self.epswd,
                                             border_width=2, corner_radius=10)
        self.entry6.place(relx=0.275, rely=0.8, anchor=CENTER)
        self.epswd.trace("w", lambda *args: Char_limit(self.epswd))


#----------------------------------------------------------------------------------------------------
       
        self.value=customtkinter.StringVar()
        self.combobox = customtkinter.CTkComboBox(self.frame2,
                                            values=["Disable", "Enable"],variable=self.value,
                                            command=self.disenable,state="readonly",text_color="black")
        self.combobox.place(relx=0.500, rely=0.92, anchor=CENTER)   
        
 #-----------------------------------------------------------------------------------------------
    def disenable(self,choice):
        if choice=="Disable":
            self.entry1.configure(state="disabled")
            self.entry2.configure(state="disabled")
            self.entry3.configure(state="disabled")
            self.entry5.configure(state="disabled")
            self.entry6.configure(state="disabled")

        elif choice=="Enable":
            self.entry1.configure(state="normal")
            self.entry2.configure(state="normal")
            self.entry3.configure(state="normal")
            self.entry5.configure(state="normal")
            self.entry6.configure(state="normal")
           
#------------------------------------------------------------------------------ 
 
    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False
    
    def update(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()
        status = self.combobox.get()

        if ename.strip():
            if valid_phone(econtact):
                if isValidAadhaarNumber(eaddhar):
                    if edes:
                        if eadd:
                            if valid_pass(epass):
                                emp_id = vall[0]
                                update = (
                                    "UPDATE employee SET name = ?, contact_num = ?, address = ?, aadhar_num = ?, password = ?, designation = ?,status=? WHERE emp_id = ?"
                                )
                                cur.execute(
                                    update, [ename, econtact, eadd, eaddhar, epass, edes, status, emp_id])
                                db.commit()
                                msg_Eupdate()
                                messagebox.showinfo("Success!!", "Employee ID: {} successfully updated in database.".format(
                                    emp_id), parent=e_update)
                                vall.clear()
                                page5.tree.delete(*page5.tree.get_children())
                                page5.DisplayData()
                                Employee.sel.clear()
                                e_update.destroy()
                            else:
                                messagebox.showerror(
                                    "Oops!", "Password must be  mor ethan 8 character.", parent=e_update)
                        else:
                            messagebox.showerror(
                                "Oops!", "Please enter address.", parent=e_update)
                    else:
                        messagebox.showerror(
                            "Oops!", "Please enter designation.", parent=e_update)
                else:
                    messagebox.showerror(
                        "Oops!", "Invalid Aadhar number.", parent=e_update)
            else:
                messagebox.showerror(
                    "Oops!", "Invalid phone number.", parent=e_update)
        else:
            messagebox.showerror(
                "Oops!", "Please enter employee name.", parent=e_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
    
#-----------------------------------------------------------------------

class Invoice:
    def __init__(self, top=None):
        top.geometry("1366x768+320+144")
        top.resizable(0, 0)
        top.title("Invoices")

#--------------------------------------------------frames-----------------------------------------------------

        self.frame1 = customtkinter.CTkFrame(
            invoice, width=1280, height=768, corner_radius=10)
        self.frame1.pack(padx=20, pady=20)

        self.label1 = customtkinter.CTkLabel(
            self.frame1, bg='#57a1f8', width=120, height=25)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)

        self.frame2 = customtkinter.CTkFrame(
            self.frame1, width=300, height=680, corner_radius=10)
        self.frame2.place(x=30, y=25)

        self.frame3 = customtkinter.CTkFrame(
            self.frame2, width=250, height=180, corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.33, anchor=CENTER)

        self.frame4 = customtkinter.CTkFrame(
            self.frame1, width=450, height=50, corner_radius=10)
        self.frame4.place(relx=0.80, rely=0.07, anchor=CENTER)


        self.frame6 = customtkinter.CTkFrame(
            self.frame1, width=840, height=570, corner_radius=10)
        self.frame6.place(relx=0.635, rely=0.55, anchor=CENTER)
        
        
#-------------------------------------------------------------------------------------------------------

        self.label_login = customtkinter.CTkLabel(self.frame2, text="INVOICE",
                                                  fg_color=("#CCCCCC", "dimgray"),
                                                  corner_radius=8,
                                                  width=250, height=70,
                                                  text_font=("Roboto Medium", -25))
        self.label_login.place(relx=0.5, rely=0.1, anchor=CENTER)

#----------------------------------------------------------------------------------------------------------------

        self.clock = customtkinter.CTkLabel(self.frame4)
        self.clock.place(relx=0.85, rely=0.5, anchor=CENTER)
        
        image_size = 20
        self.logout1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/logout.png").resize((image_size,image_size)))
        self.button2 = customtkinter.CTkButton(self.frame4, width=120,
                                               height=32,image=self.logout1,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Logout",
                                               command=self.Logout)
        self.button2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.switch_3 = customtkinter.CTkSwitch(self.frame4,
                                                text="Light Mode", bg_color=None,
                                                command=self.change_mode)
        self.switch_3.place(relx=0.15, rely=0.5, anchor=CENTER)

#--------------------------------------------------------------------------------------------------------
        b_id=StringVar()

        self.billno = customtkinter.CTkLabel(self.frame3, text="Bill Number")
        self.billno.place(relx=0.5, rely=0.15, anchor=CENTER)

        self.entry1 = customtkinter.CTkEntry(self.frame3, width=190,
                                             height=40, placeholder_text="Product ID",textvariable=b_id,
                                             border_width=2, corner_radius=10)
        b_id.trace("w", lambda *args: id_limit(b_id))
        self.entry1.place(relx=0.5, rely=0.43, anchor=CENTER)
        self.entry1.bind('<FocusIn>', self.prodectid_in)
        self.entry1.bind('<FocusOut>', self.prodectid_out)

        self.search1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/search.png").resize((image_size,image_size)))
        self.button1 = customtkinter.CTkButton(self.frame3, width=150,
                                               height=35,image=self.search1,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Search",
                                               command=self.search_inv)
        self.button1.place(relx=0.5, rely=0.75, anchor=CENTER)
        
        self.back = ImageTk.PhotoImage(Image.open(
        PATH + "./images/back.png").resize((image_size,image_size)))
        self.button6 = customtkinter.CTkButton(self.frame2, width=150,
                                               height=35,image=self.back,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Back",
                                               fg_color='#FF6347',
                                               command=self.Exit)
        self.button6.place(relx=0.5, rely=0.90, anchor=CENTER)

#-----------------------------------------------------------------------------------------------------------

        self.style = ttk.Style()
        self.style.theme_use("alt")

        self.style.configure("Treeview",
                             background='#333333',
                             foreground='#e5e5e5',
                             rowheight=25,
                             fieldbackground='#333333',)

        self.tree = ttk.Treeview(self.frame6)
        self.tree.place(relx=0.5, rely=0.5, anchor=CENTER,
                        width=750, height=550)
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.bind("<Double-1>", self.double_tap)

        self.tree.configure(
            columns=(
                "Bill Number",
                "Date",
                "Customer Name",
                "Customer Phone No.",
            )
        )

        self.tree.heading("Bill Number", text="Bill Number", anchor=W)
        self.tree.heading("Date", text="Date", anchor=W)
        self.tree.heading("Customer Name", text="Customer Name", anchor=W)
        self.tree.heading("Customer Phone No.",
                          text="Customer Phone No.", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=200)
        self.tree.column("#2", stretch=NO, minwidth=0, width=150)
        self.tree.column("#3", stretch=NO, minwidth=0, width=200)
        self.tree.column("#4", stretch=NO, minwidth=0, width=200)

        self.DisplayData()

    def DisplayData(self):
        cur.execute("SELECT * FROM bill")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))


    sel = []
    
    def change_mode(self):
        if self.switch_3.get() == 0:
            customtkinter.set_appearance_mode("dark")

            self.style.configure("Treeview",
                                 background='#333333',
                                 foreground='#e5e5e5',
                                 rowheight=25,
                                 fieldbackground='#333333',)
        else:
            customtkinter.set_appearance_mode("light")

            self.style.configure("Treeview",
                                 background='#dbdbdb',
                                 foreground='#1f2d3b',
                                 rowheight=25,
                                 fieldbackground='#dbdbdb',)

    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def double_tap(self, Event):
        item = self.tree.identify('item', Event.x, Event.y)
        global bill_num
        bill_num = self.tree.item(item)['values'][0]
        global bill
        bill = customtkinter.CTkToplevel()
        pg = open_bill(bill)
        #bill.protocol("WM_DELETE_WINDOW", exitt)
        bill.mainloop()

    

    def search_inv(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search == to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Bill Number: {} found.".format(
                    self.entry1.get()), parent=invoice)
                break
            else:
                self.entry1.configure(border_color="red")
                messagebox.showerror("Oops!!", "Bill NUmber: {} not found.".format(
                    self.entry1.get()), parent=invoice)
                break

    def Logout(self):
        sure = messagebox.askyesno(
            "Logout", "Are you sure you want to logout?")
        if sure == True:
            invoice.destroy()
            root.destroy()
            
    def prodectid_in(self, e):
        self.entry1.configure(border_color="blue")

    def prodectid_out(self, e):
        self.entry1.configure(border_color="")


    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.configure(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno(
            "Exit", "Are you sure you want to exit?", parent=invoice)
        if sure == True:
            invoice.destroy()
            root.deiconify()


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

class open_bill:
    def __init__(self, top=None):
        top.geometry("720x400+320+144")
        top.resizable(0, 0)
        top.title("Bill")
        
        self.label1 = customtkinter.CTkLabel(bill)
        self.label1.place(relx=0, rely=0, width=765, height=488)
        self.img = PhotoImage(file="./images/bill.png")
        self.label1.configure(image=self.img)

        self.EMPID = Text(bill)
        self.EMPID.place(relx=0.178, rely=0.163, width=180, height=30)
        self.EMPID.configure(font="-family {Podkova} -size 12")
        self.EMPID.configure(borderwidth=0)
        self.EMPID.configure(background="#ffffff")

        self.name_message = Text(bill)
        self.name_message.place(relx=0.223, rely=0.233, width=176, height=30)
        self.name_message.configure(font="-family {Podkova} -size 12")
        self.name_message.configure(borderwidth=0)
        self.name_message.configure(background="#ffffff")

        self.num_message = Text(bill)
        self.num_message.place(relx=0.788, rely=0.231, width=95, height=30)
        self.num_message.configure(font="-family {Podkova} -size 12")
        self.num_message.configure(borderwidth=0)
        self.num_message.configure(background="#ffffff")

        self.bill_message = Text(bill)
        self.bill_message.place(relx=0.175, rely=0.295, width=176, height=26)
        self.bill_message.configure(font="-family {Podkova} -size 10")
        self.bill_message.configure(borderwidth=0)
        self.bill_message.configure(background="#ffffff")

        self.bill_date_message = Text(bill)
        self.bill_date_message.place(relx=0.680, rely=0.297, width=90, height=26)
        self.bill_date_message.configure(font="-family {Podkova} -size 10")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(background="#ffffff")


        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.044, rely=0.50, width=695, height=284)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

        find_bill = "SELECT * FROM bill WHERE bill_no = ?"
        cur.execute(find_bill, [bill_num])
        results = cur.fetchall()
        if results:
            self.EMPID.insert(END,results[0][5])
            self.EMPID.configure(state="disabled")
            
            self.name_message.insert(END, results[0][2])
            self.name_message.configure(state="disabled")
    
            self.num_message.insert(END, results[0][3])
            self.num_message.configure(state="disabled")
    
            self.bill_message.insert(END, results[0][0])
            self.bill_message.configure(state="disabled")

            self.bill_date_message.insert(END, results[0][1])
            self.bill_date_message.configure(state="disabled")

            self.Scrolledtext1.configure(state="normal")
            self.Scrolledtext1.insert(END, results[0][4])
            self.Scrolledtext1.configure(state="disabled")

        
        
        
class Aboutus:
    def __init__(self, top=None):
        top.title("slider")
        top.geometry("1366x768+320+144")
        top.resizable(0,0)

        self.label1 = Label(top)
        self.label1.place(relx=0.5, rely=0.5,anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)

        b1=customtkinter.CTkButton(top,width=100,height=40,
                                  fg_color="blue",text="Back",
                                  command=self.Exit)
        b1.place(relx=0.05,rely=0.08)
        
        self.label_login = customtkinter.CTkLabel(top, text="ABOUT US",
                                                  fg_color=(
                                                      "#CCCCCC", "dimgray"),
                                                  corner_radius=8,
                                                  width=370, height=80,
                                                  text_font=("Roboto Medium", -32))
        self.label_login.place(relx=0.5, rely=0.13, anchor=CENTER)



#================IMAGES===================

        self.image1=ImageTk.PhotoImage(file="./images/1.png")
        self.image2=ImageTk.PhotoImage(file="./images/2.png")
       

#========================================
        Frame_Slider=Frame(top)
        Frame_Slider.place(x=20,y=190,width=1328,height=555)

        self.lbl1=Label(Frame_Slider,image=self.image1,bd=0)
        self.lbl1.place(x=0,y=0)

        self.lbl2=Label(Frame_Slider,image=self.image2,bd=0)
        self.lbl2.place(x=1100,y=0)

      

        
        self.x=1100
        self.Slider_func()

    def Slider_func(self):
        self.x-=1
        if self.x==0:
            self.x=1100
            time.sleep(2)

            self.new_im=self.image1
            self.image1=self.image2
            self.image2=self.new_im


            self.lbl1.configure(image=self.image1)
            self.lbl2.configure(image=self.image2)
             

        self.lbl2.place(x=self.x,y=0)
        self.lbl2.after(1,self.Slider_func)

    def Exit(self):
        sure = messagebox.askyesno(
            "Exit", "Are you sure you want to exit?", parent=aboutus)
        if sure == True:
            aboutus.destroy()
            root.deiconify()


page1 = Admin_Page(root)
root.mainloop()

