import sqlite3
import re
import os
import random
import string
from turtle import bgcolor, width
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
import customtkinter
from ttkwidgets import autocomplete
from webbrowser import BackgroundBrowser
from ttkwidgets.autocomplete import AutocompleteEntry
import itertools
from PIL import ImageTk,Image
import pygame
import time
#============================================

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("system")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme('dark-blue')

PATH=os.path.dirname(os.path.realpath(__file__))

root = customtkinter.CTk()
root.geometry("1280x768+320+144")
root.title("Retail Manager")

app_width=1280
app_height=768

root.maxsize(app_width,app_height)
root.minsize(app_width,app_height)


entry1 = StringVar()
entry2 = StringVar()
cust_new_bill = StringVar()
cust_search_bill = StringVar()
bill_date = StringVar()


with sqlite3.connect("./Database/store.db") as db:
    cur = db.cursor()

def random_bill_number(stringLength):
    Digits = string.digits
    strr = ''.join(random.choice(Digits) for i in range(stringLength-5))
    return ('QB'+strr)


def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

def only_numbers(char):
    return char.isdigit()

def Char_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:20]) 

def phone_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:10])

def id_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:8])

def qty_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:4])


f = open('./Database/userlogin.txt', "r+", encoding='utf-8')
getemp=f.read()
f.close()

pygame.mixer.init()

def msg_billgen():
    pygame.mixer.music.load("./audio/bill generated succesfully.mp3")
    pygame.mixer.music.play(loops=0)

     
class Item:
    def __init__(self, name, price, qty):
        self.product_name = name
        self.price = price
        self.qty = qty

class Cart:
    def __init__(self):
        self.items = []
        self.dictionary = {}

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        self.items.pop()

    def remove_items(self):
        self.items.clear()

    def total(self):
        total = 0.0
        for i in self.items:
            total += i.price * i.qty
        return total

    def isEmpty(self):
        if len(self.items)==0:
            return True
        
    def allCart(self):
        for i in self.items:
            if (i.product_name in self.dictionary):
                self.dictionary[i.product_name] += i.qty
            else:
                self.dictionary.update({i.product_name:i.qty})

def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()

class bill_window:
    def __init__(self, top=None):
        top.geometry("1280x768+320+144")
        top.resizable(1,1)
        top.title("Billing System")
        
        self.frame1 = customtkinter.CTkFrame(
            root, width=1280, height=768, corner_radius=10, border_color='blue')
        self.frame1.pack(padx=20, pady=20)  
        
        self.label1 = customtkinter.CTkLabel(
            self.frame1, bg='#57a1f8')
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = ImageTk.PhotoImage(Image.open(
            PATH + "./images/login_bg.png").resize((1240, 700)))
        self.label1.configure(image=self.img)
        
        self.frame2 = customtkinter.CTkFrame(
            self.frame1, width=450, height=400, corner_radius=10)
        self.frame2.place(relx=0.2, rely=0.535, anchor=CENTER)
        
        self.frame3 = customtkinter.CTkFrame(self.frame1, width=1200, height=70,
                                             corner_radius=10)
        self.frame3.place(relx=0.5, rely=0.18, anchor=CENTER)
        
        self.frame4 = customtkinter.CTkFrame(
            self.frame1, width=390, height=50, corner_radius=10)
        self.frame4.place(relx=0.825, rely=0.07, anchor=CENTER)
        
        self.frame5 = customtkinter.CTkFrame(
            self.frame1, width=450, height=100, corner_radius=10)
        self.frame5.place(relx=0.2, rely=0.90, anchor=CENTER)
        
        self.frame6 = customtkinter.CTkFrame(
            self.frame1, width=735, height=518, corner_radius=10)
        self.frame6.place(relx=0.685, rely=0.61, anchor=CENTER)
        
       
        self.frame7 = customtkinter.CTkFrame(
            self.frame1, width=105, height=40, corner_radius=10)
        self.frame7.place(relx=0.06, rely=0.06, anchor=CENTER)

        self.label1 = Label(self.frame6,width=710, height=500)
        self.label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img1 = PhotoImage(file="./images/bill.png")
        self.label1.configure(image=self.img1)
        
        
#------------------------------------------------------------------------------------
        with open('./Database/userlogin.txt', 'r+', encoding='utf-8') as f:
            content=f.read()
            print(content)
            f.close()

        self.emp_id=customtkinter.CTkLabel(self.frame7)
        self.emp_id.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.emp_id.configure(text=content)
        
               
#----------------------------------------------------------------------------------------------------------------

        self.clock = customtkinter.CTkLabel(self.frame4)
        self.clock.place(relx=0.85, rely=0.5, anchor=CENTER)
        self.time()

        image_size = 15
        self.logout1= ImageTk.PhotoImage(Image.open(
        PATH + "./images/logout.png").resize((image_size,image_size)))
        self.button2 = customtkinter.CTkButton(self.frame4, width=120,
                                               height=32,image=self.logout1,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Logout",command=self.Logout)
        self.button2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.switch_3 = customtkinter.CTkSwitch(self.frame4,
                                                text="Light Mode", bg_color=None,
                                                command=self.change_mode)
        self.switch_3.place(relx=0.15, rely=0.5, anchor=CENTER)

#-------------------------------------------------------------------------------------------------------

        self.label_emp = customtkinter.CTkLabel(self.frame1, text="Billing Sysyem",
                                                fg_color=(
                                                    "#CCCCCC", "dimgray"),
                                                corner_radius=8,
                                                width=250, height=50,
                                                text_font=("Roboto Medium", -28))
        self.label_emp.place(relx=0.5, rely=0.07, anchor=CENTER)

#---------------------------------------------------------------------------------------
        
        self.bill_no_label = customtkinter.CTkLabel(
            self.frame3, text_font=("Roboto Medium", -13), text="Bill Number")
        self.bill_no_label.place(relx=0.06, rely=0.5, anchor=CENTER)

        cust_search_bill=StringVar()
        
        self.billNo_entry = customtkinter.CTkEntry(self.frame3, width=190,
                                             height=40, placeholder_text="Bill Number",
                                             border_width=2, corner_radius=10,textvariable=cust_search_bill)        
        self.billNo_entry.place(relx=0.19, rely=0.5, anchor=CENTER)
        cust_search_bill.trace("w", lambda *args: id_limit(cust_search_bill))


        
        self.search1= ImageTk.PhotoImage(Image.open(
        PATH + "./images/search.png").resize((image_size,image_size)))
        self.button2 = customtkinter.CTkButton(self.frame3, width=120,
                                               height=35,image=self.search1,
                                               border_width=1,
                                               corner_radius=20,
                                               text="Search",
                                               command=self.search_bill)
        self.button2.place(relx=0.33, rely=0.5, anchor=CENTER)
        
#--------------------------------------------------------------------------------------
        
       
        
        self.cust_name_label = customtkinter.CTkLabel(
            self.frame3, text_font=("Roboto Medium", -13), text="Customer Name")
        self.cust_name_label.place(relx=0.49, rely=0.5, anchor=CENTER)
        
        cust_name=StringVar()
        self.entry1 = customtkinter.CTkEntry(self.frame3, validate="key",width=190,
                                                   height=40, placeholder_text="Customer Name",
                                                   textvariable=cust_name,
                                                   border_width=1, corner_radius=10)
        cust_name.trace("w", lambda *args: Char_limit(cust_name))                                          

        self.entry1.place(relx=0.62, rely=0.5, anchor=CENTER)
        
#-------------------------------------------------------------------------------------------
        
        
        
        self.cust_no_label = customtkinter.CTkLabel(self.frame3, text_font=("Roboto Medium", -13), text="Customer Number")
        self.cust_no_label.place(relx=0.76, rely=0.5, anchor=CENTER)
         
        cust_num=customtkinter.StringVar()
        validation = root.register(only_numbers)
        self.entry2 = customtkinter.CTkEntry(self.frame3, width=190,
                                                height=40, placeholder_text="Customer Number",textvariable=cust_num,
                                                validate="key", validatecommand=(validation, '%S'),
                                                border_width=1, corner_radius=10)
        self.entry2.place(relx=0.89, rely=0.5, anchor=CENTER)
        cust_num.trace("w", lambda *args: phone_limit(cust_num))
        
        
#------------------------------------------------------------------------------------------------
        
        self.bill_option = customtkinter.CTkLabel(
            self.frame5, text_font=("Roboto Medium", -14), text="Bill Options")
        self.bill_option.place(relx=0.5, rely=0.2, anchor=CENTER)
        

        self.total= ImageTk.PhotoImage(Image.open(
        PATH + "./images/total.png").resize((image_size,image_size)))
        self.button3 = customtkinter.CTkButton(self.frame5, width=80,
                                               height=35,image=self.total,
                                               border_width=1,
                                               corner_radius=20,
                                               text="Total",
                                               command=self.total_bill)
        self.button3.place(relx=0.12, rely=0.65, anchor=CENTER)


        self.generate= ImageTk.PhotoImage(Image.open(
        PATH + "./images/generate.png").resize((image_size,image_size)))
        self.button4 = customtkinter.CTkButton(self.frame5, width=80,
                                               height=35,image=self.generate,
                                               border_width=1,
                                               corner_radius=20,
                                               text="Generate",
                                               command=self.gen_bill)
        self.button4.place(relx=0.39, rely=0.65, anchor=CENTER)

        self.clear = ImageTk.PhotoImage(Image.open(
        PATH + "./images/clear.png").resize((image_size,image_size)))   
        self.button5 = customtkinter.CTkButton(self.frame5, width=80,
                                               height=35,image=self.clear,
                                               border_width=1,
                                               corner_radius=20,
                                               text="Clear",
                                               command=self.clear_bill)
        self.button5.place(relx=0.66, rely=0.65, anchor=CENTER)
        

        self.exit = ImageTk.PhotoImage(Image.open(
        PATH + "./images/back.png").resize((image_size,image_size)))
        self.button6 = customtkinter.CTkButton(self.frame5, width=70,
                                               height=35,image=self.exit,
                                               border_width=1,
                                               corner_radius=20,
                                               text="Exit",
                                               fg_color='#FF6347',
                                               command=exitt)
        self.button6.place(relx=0.89, rely=0.65, anchor=CENTER)
        
#-----------------------------------------------------------------------------------------

        self.product_entey = customtkinter.CTkLabel(self.frame2, fg_color=("#CCCCCC", "dimgray"),
                                                    corner_radius=8,width=250, height=40,text="Product Entry",
                                                    text_font=("Roboto Medium", -20))
        self.product_entey.place(relx=0.5, rely=0.15, anchor=CENTER)
        

        self.addtocart= ImageTk.PhotoImage(Image.open(
        PATH + "./images/addtocart.png").resize((image_size,image_size)))
        self.button7 = customtkinter.CTkButton(self.frame2, width=120,
                                               height=40,image=self.addtocart,
                                               border_width=1,
                                               corner_radius=20,
                                               text="Add To Cart",
                                               command=self.add_to_cart)
        self.button7.place(relx=0.2, rely=0.8, anchor=CENTER)
        

        self.remove= ImageTk.PhotoImage(Image.open(
        PATH + "./images/remove.png").resize((image_size,image_size)))
        self.button8 = customtkinter.CTkButton(self.frame2, width=120,
                                               height=40,image=self.remove,
                                               border_width=1,
                                               corner_radius=20,
                                               text="Remove",
                                               command=self.remove_product)
        self.button8.place(relx=0.5, rely=0.8, anchor=CENTER)
        

        self.clear1 = ImageTk.PhotoImage(Image.open(
        PATH + "./images/clear.png").resize((image_size,image_size)))
        self.button9 = customtkinter.CTkButton(self.frame2, width=120,
                                               height=40,image=self.clear1,
                                               border_width=1,
                                               corner_radius=20,
                                               text="Clear",
                                               command=self.clear_selection)
        self.button9.place(relx=0.8, rely=0.8, anchor=CENTER)


        cmplt_name = "SELECT product_name FROM raw_inventory WHERE status = ?"
        cur.execute(cmplt_name,["Enable"])
        results = cur.fetchall()
        autofill=list(itertools.chain(*results))

        self.entry4= AutocompleteEntry(master=self.frame2,
                                                   width=29,
                                                   font=('Times', 18),
                                                   completevalues=autofill)
        self.entry4.place(relx=0.5, rely=0.35, anchor=CENTER)
        self.entry4.insert(0, "Product id or Product Name")
        self.entry4.bind("<Return>",self.is_empty)
        self.entry4.bind("<Button-1>",self.click)
        self.entry4.bind("<Leave>",self. leave)
  


        qty=customtkinter.StringVar()
        validation = root.register(only_numbers)
        self.entry5 = customtkinter.CTkEntry(master=self.frame2,
                                             placeholder_text="quantity",
                                             width=350,textvariable=qty,
                                             validate="key", validatecommand=(validation, '%S'),
                                             height=45,
                                             border_width=2,
                                             corner_radius=10)
        self.entry5.place(relx=0.5, rely=0.55, anchor=CENTER)
        qty.trace("w", lambda *args: qty_limit(qty))
        self.entry5.configure(state="disabled")
        self.entry5.bind("<Return>", self.add_to_cart)
        

#----------------------------------------------------------------------------------------------

        
        self.Scrolledtext1 = tkst.ScrolledText(self.frame6,width=115,height=18)
        self.Scrolledtext1.place(relx=0.018,rely=0.41)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

    def click(self,*args):
        self.entry4.delete(0, END)
  
# call function when we leave entry box
    def leave(self,*args):
        name=self.entry4.get()
        if name!='':
            pass
        else:
            self.entry4.delete(0, 'end')
            self.entry4.insert(0, 'Product Id or Product Name ')
            root.focus()

    def is_empty(self,Event):
        name=self.entry4.get()
        if len(name)==0:
            messagebox.showinfo("Hello","Product id or Name should not be empty")
        else:
            self.entry5.configure(state="normal")
            self.entry5.focus_set()
            self.show_qty()

    def search(self,get_product,name):
        for i in range(len(get_product)):
            if get_product[i] == name:
                return True
        return False

        
    def show_qty(self):
        get_entry = "SELECT product_name FROM raw_inventory WHERE status = 'Enable'"
        cur.execute(get_entry)
        results = cur.fetchall()
        get_product=list(itertools.chain(*results))
        print(get_product)
        name=self.entry4.get()
        if self.search(get_product,name):
                self.qty_label =customtkinter.CTkLabel(root)
                                                
                self.qty_label.place(relx=0.080, rely=0.600, width=90, height=26)
                
                product_name=self.entry4.get()
                product_id = self.entry4.get()
                find_qty = "SELECT stock FROM raw_inventory WHERE product_id = ? or product_name=?"
                cur.execute(find_qty, [product_id,product_name])
                results = cur.fetchone()
                self.qty_label.configure(text="In Stock: {}".format(results[0]))
        else:
            messagebox.showerror("ERROR","Item not found")
        

    cart = Cart()
    
    def add_to_cart(self,*args):
        self.Scrolledtext1.configure(state="normal")
        strr = self.Scrolledtext1.get('1.0', END)
        if strr.find('Total')==-1:
            product_name=self.entry4.get()
            product_id=self.entry4.get()
            product_qty=self.entry5.get()
            if(product_id!=""or product_name!=""):
                if(product_qty!="0"):
                    find_mrp = "SELECT mrp, stock,product_name,product_id FROM raw_inventory WHERE product_id = ? or product_name=?"
                    cur.execute(find_mrp, [product_id,product_name])
                    results = cur.fetchall()
                    stock = results[0][1]
                    mrp = results[0][0]
                    product_name=results[0][2]
                    product_id=results[0][3]
                    if product_qty.isdigit()==True:
                        if (stock-int(product_qty))>=0:
                            sp = mrp*int(product_qty)
                            item = Item(product_id,mrp, int(product_qty))
                            self.cart.add_item(item)
                            self.Scrolledtext1.configure(state="normal")
                            bill_text ="    {}\t\t        {}\t\t\t\t\t\t{}\t\t\t      {}\n".format(product_id,product_name, product_qty, sp)
                            self.Scrolledtext1.insert('insert', bill_text)
                            self.Scrolledtext1.configure(state="disabled")
                        else:
                            messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=root)
                    else:
                        messagebox.showerror("Oops!", "Invalid quantity.", parent=root)
                else:
                    messagebox.showerror("Oops!", "Invalid quantity.", parent=root)
            else:
                messagebox.showerror("Oops!", "Choose a product.", parent=root)
        else:
            self.Scrolledtext1.delete('1.0', END)
            new_li = []
            li = strr.split("\n")
            for i in range(len(li)):
                if len(li[i])!=0:
                    if li[i].find('Total')==-1:
                        new_li.append(li[i])
                    else:
                        break
            for j in range(len(new_li)-1):
                self.Scrolledtext1.insert('insert', new_li[j])
                self.Scrolledtext1.insert('insert','\n')
            product_id = self.entry4.get()
            if(product_id!=""):
                product_qty = self.entry4.get()
                find_mrp = "SELECT mrp, stock, product_name FROM raw_inventory WHERE product_id = ?"
                cur.execute(find_mrp, [product_name])
                results = cur.fetchall()
                stock = results[0][1]
                mrp = results[0][0]
                product_name=results[0][2]
                if product_qty.isdigit()==True:
                    if (stock-int(product_qty))>=0:
                        sp = results[0][0]*int(product_qty)
                        global p_id
                        p_id=product_id
                        item = Item(product_id, mrp, int(product_qty))
                        self.cart.add_item(item)
                        self.Scrolledtext1.configure(state="normal")
                        bill_text="    {}\t\t        {}\t\t\t\t\t\t{}\t\t\t      {}\n".format(product_id,product_name, product_qty, sp)
                        self.Scrolledtext1.insert('insert', bill_text)
                        self.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=root)
                else:
                    messagebox.showerror("Oops!", "Invalid quantity.", parent=root)
            else:
                messagebox.showerror("Oops!", "Choose a product.", parent=root)

    def remove_product(self):
        if(self.cart.isEmpty()!=True):
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total')==-1:
                try:
                    self.cart.remove_item()
                except IndexError:
                    messagebox.showerror("Oops!", "Cart is empty", parent=root)
                else:
                    self.Scrolledtext1.configure(state="normal")
                    get_all_bill = (self.Scrolledtext1.get('1.0', END).split("\n"))
                    new_string = get_all_bill[:len(get_all_bill)-3]
                    self.Scrolledtext1.delete('1.0', END)
                    for i in range(len(new_string)):
                        self.Scrolledtext1.insert('insert', new_string[i])
                        self.Scrolledtext1.insert('insert','\n')
                    
                    self.Scrolledtext1.configure(state="disabled")
            else:
                try:
                    self.cart.remove_item()
                except IndexError:
                    messagebox.showerror("Oops!", "Cart is empty", parent=root)
                else:
                    self.Scrolledtext1.delete('1.0', END)
                    new_li = []
                    li = strr.split("\n")
                    for i in range(len(li)):
                        if len(li[i])!=0:
                            if li[i].find('Total')==-1:
                                new_li.append(li[i])
                            else:
                                break
                    new_li.pop()
                    for j in range(len(new_li)-1):
                        self.Scrolledtext1.insert('insert', new_li[j])
                        self.Scrolledtext1.insert('insert','\n')
                    self.Scrolledtext1.configure(state="disabled")

        else:
            messagebox.showerror("Oops!", "Add a product.", parent=root)

    def wel_bill(self):

        self.empid_message = Text(root)
        self.empid_message.place(relx=0.484, rely=0.373, width=90, height=26)
        self.empid_message.configure(font="-family {Podkova} -size 12")
        self.empid_message.configure(borderwidth=0)
        self.empid_message.configure(background="#ffffff")

        self.custname = Text(root)
        self.custname.place(relx=0.504, rely=0.405, width=90, height=30)
        self.custname.configure(font="-family {Podkova} -size 12")
        self.custname.configure(borderwidth=0)
        self.custname.configure(background="#ffffff")

        self.phone_no = Text(root)
        self.phone_no.place(relx=0.823, rely=0.405, width=170, height=30)
        self.phone_no.configure(font="-family {Podkova} -size 12")
        self.phone_no.configure(borderwidth=0)
        self.phone_no.configure(background="#ffffff")

        self.bill_no = Text(root)
        self.bill_no.place(relx=0.479, rely=0.438, width=176, height=26)
        self.bill_no.configure(font="-family {Podkova} -size 12")
        self.bill_no.configure(borderwidth=0)
        self.bill_no.configure(background="#ffffff")

        self.bill_date_message = Text(root)
        self.bill_date_message.place(
            relx=0.765, rely=0.438, width=90, height=26)
        self.bill_date_message.configure(font="-family {Podkova} -size 12")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(background="#ffffff")

        

    def total_bill(self):
        if self.cart.isEmpty():
            messagebox.showerror("Oops!", "Add a product.", parent=root)
        else:
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total')==-1:
                self.Scrolledtext1.configure(state="normal")
                divider = "\n\n\n"+("─"*60)
                self.Scrolledtext1.insert('insert', divider)
                total = "\n   Total\t\t\t\t\t\t\t\t\t\t\t Rs. {}".format(self.cart.total())
                self.Scrolledtext1.insert('insert', total)
                divider2 = "\n"+("─"*60)
                self.Scrolledtext1.insert('insert', divider2)
                self.Scrolledtext1.configure(state="disabled")
            else:
                return

    state = 1
    def gen_bill(self):

        if self.state == 1:
            strr = self.Scrolledtext1.get('1.0', END)
            self.wel_bill()
            if(self.entry1.get()==""):
                messagebox.showerror("Oops!", "Please enter a valid customer name.", parent=root)
            elif(self.entry2.get()==""):
                messagebox.showerror("Oops!", "Please enter a number.", parent=root)
            elif valid_phone(self.entry2.get())==False:
                messagebox.showerror("Oops!", "Please enter a valid number.", parent=root)
            elif(self.cart.isEmpty()):
                messagebox.showerror("Oops!", "Cart is empty.", parent=root)
            else: 
                if strr.find('Total')==-1:
                    self.total_bill()
                    self.gen_bill()
                else:

                    self.empid_message.insert(END,getemp)
                    self.empid_message.configure(state="disabled")

                    self.custname.insert(END, self.entry1.get())
                    self.custname.configure(state="disabled")
            
                    self.phone_no.insert(END,self.entry2.get())
                    self.phone_no.configure(state="disabled")
            
                    cust_new_bill.set(random_bill_number(8))

                    self.bill_no.insert(END, cust_new_bill.get())
                    self.bill_no.configure(state="disabled")
                
                    bill_date.set(str(date.today()))

                    self.bill_date_message.insert(END, bill_date.get())
                    self.bill_date_message.configure(state="disabled")


                    with sqlite3.connect("./Database/store.db") as db:
                        cur = db.cursor() 
                    insert = ("INSERT INTO bill(bill_no, date, customer_name, customer_no, bill_details,emp_id,product_id) VALUES(?,?,?,?,?,?,?)")
                    cur.execute(insert, [cust_new_bill.get(),bill_date.get(),self.entry1.get(),self.entry2.get(),self.Scrolledtext1.get('1.0', END),getemp,self.entry4.get()])
                    db.commit()
                    print(self.cart.allCart())
                    for name, qty in self.cart.dictionary.items():
                        print(name, qty)
                        update_qty = ("UPDATE raw_inventory SET stock = stock - ? WHERE product_id = ?")
                        cur.execute(update_qty, [qty, name])
                        db.commit()
                    msg_billgen()
                    messagebox.showinfo("Success!!", "Bill Generated", parent=root)
                    self.entry4.configure(state="disabled")
                    self.entry5.configure(state="disabled")
                    self.state = 0
        else:
            return
                    
    def clear_bill(self):
        self.wel_bill()
        self.entry4.configure(state="normal")
        self.entry5.configure(state="normal")
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.custname.configure(state="normal")
        self.bill_no.configure(state="normal")
        self.phone_no.configure(state="normal")
        self.bill_date_message.configure(state="normal")
        self.Scrolledtext1.configure(state="normal")
        self.custname.delete(1.0, END)
        self.phone_no.delete(1.0, END)
        self.bill_no.delete(1.0, END)
        self.bill_date_message.delete(1.0, END)
        self.empid_message.delete(1.0,END)
        self.Scrolledtext1.delete(1.0, END)
        self.bill_no.configure(state="disabled")
        self.custname.configure(state="disabled")
        self.phone_no.configure(state="disabled")
        self.bill_date_message.configure(state="disabled")
        self.Scrolledtext1.configure(state="disabled")
        self.cart.remove_items()
        self.state = 1
        self.entry1.configure(state="normal")
        self.entry2.configure(state="normal")

    def clear_selection(self):
        self.entry4.delete(0, END)
        self.entry5.delete(0,END)
        try:
            self.qty_label.configure(foreground="#333333")
        except AttributeError:
            pass
             
    def search_bill(self):
        find_bill = "SELECT * FROM bill WHERE bill_no = ?"
        cur.execute(find_bill, [self.billNo_entry.get()])
        results = cur.fetchall()
        if results:
            self.clear_bill()
            self.wel_bill()
            self.custname.insert(END, results[0][2])
            self.custname.configure(state="disabled")
    
            self.empid_message.insert(END, results[0][5])
            self.empid_message.configure(state="disabled")
    
            self.phone_no.insert(END, results[0][3])
            self.phone_no.configure(state="disabled")
    
            self.bill_no.insert(END, results[0][0])
            self.bill_no.configure(state="disabled")

            self.bill_date_message.insert(END, results[0][1])
            self.bill_date_message.configure(state="disabled")

            self.Scrolledtext1.configure(state="normal")
            self.Scrolledtext1.insert(END, results[0][4])
            self.Scrolledtext1.configure(state="disabled")

            self.entry1.configure(state="disabled")
            self.entry2.configure(state="disabled")

            self.state = 0

        else:
            messagebox.showerror("Error!!", "Bill not found.", parent=root)
            self.billNo_entry.delete(0, END)

            
    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.configure(text=string)
        self.clock.after(1000, self.time)
        
    def Logout(self):
        sure = messagebox.askyesno(
            "Logout", "Are you sure you want to logout?")
        if sure == True:
            root.destroy()
            os.system('Login.py')
            
    def change_mode(self):
        if self.switch_3.get() == 0:
            customtkinter.set_appearance_mode("dark") 
        else:
            customtkinter.set_appearance_mode("light")

            

page1 = bill_window(root)
root.mainloop()
