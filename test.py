import tkinter as tk


class Lotfi(tk.Entry):
    def __init__(self, master=None, max_len=10, **kwargs):
        self.var = tk.StringVar()
        self.max_len = max_len
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)

    def check(self, *args):
        if len(self.get()) <= self.max_len:
            self.old_value = self.get()  # accept change
        else:
            self.var.set(self.old_value)  # reject change


#demo code:
window = tk.Tk()
ent = Lotfi(window)
ent.pack(pady=10,padx=10)
window.mainloop()
 
 ]
 =[[]]
# import rotatescreen
# import time

# Screen = rotatescreen.get_primary_diaplay()
# for i in range(13):
#     time.sleep(1)
#     Screen.rotate_tp(i*90 % 360)
