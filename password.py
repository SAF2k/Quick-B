import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

entry = customtkinter.CTkEntry(app,
                               placeholder_text="CTkEntry",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.insert(0,"HI")
entry.configure(state="disabled")
entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()