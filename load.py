import os
from tkinter import *
import customtkinter

#-----setting the appearence of the customtkinter widgets------
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
#-------------------------------------------------------------

#--------creating the root window----
main = customtkinter.CTk()
main.title("Quick B")

app_width=1366
app_height=768

#---------making the window to be appear at center----------
screen_width=main.winfo_screenwidth()
screen_height=main.winfo_screenheight()

x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)

main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
#-------------------------------------------------------------

main.resizable(0, 0)
#----------------------------------

#------function for the button click---------
def load():
    main.withdraw()
    os.system("python login.py")
    main.destroy()
#--------------------------------------------

#--------adding the image to the root window using lable-------
label1 =customtkinter.CTkLabel(main)
label1.place(relx=0, rely=0,width=1366, height=768)
img = PhotoImage(file="./images/load.png")
label1.configure(image=img)
#--------------------------------------------------------------


# ----------------login button -------------------------------------------------------
button1 = customtkinter.CTkButton(main,text="LOG IN",text_font=("Roboto Medium", -24))
button1.configure(bg_color='#ffffff',corner_radius = 50,
                    fg_color='#8249A0',
                  hover_color='#BF3EFF',
                    text_color='#000080',
                    command=load)                                       
button1.place(relx=0.095, rely=0.665, width=210, height=60)
#------------------------------------------------------------------------------------

#execute the tkinter
main.mainloop()
