# Import module
from tkinter import *
import os
import customtkinter

#------setting the appearence of the custom tkinter widgets--------
customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
#---------------------------------------------------------------------

#--------root window creation-----------
splash_root= customtkinter.CTk()
splash_root.title("Quick B")

app_width=500
app_height=400

#-----------making root to be appear at center---------------------
screen_width=splash_root.winfo_screenwidth()
screen_height=splash_root.winfo_screenheight()

x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)

splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
#-------------------------------------------------------------------

splash_root.resizable(0, 0)
#-------------------------------------------------

#--------adding images to the root using the lable--------
splash_label =customtkinter.CTkLabel(splash_root)
splash_label.pack()
img = PhotoImage(file="./images/splash.png")
splash_label.configure(image=img)
splash_label =customtkinter.CTkLabel(splash_label)
#--------------------------------------------------------

# main window function
def main():
  # destroy splash window
  splash_root.destroy()
  os.system("python load.py")#calling the load.py files after splashscreen
  


# Set Interval
splash_root.after(3000,main)

# Execute tkinter
splash_root.mainloop()
