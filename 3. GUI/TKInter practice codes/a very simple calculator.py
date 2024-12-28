import tkinter as tk
from tkinter import Button, Entry, messagebox, Radiobutton

ctrls = []

my_app = tk.Tk()

radioValue = tk.IntVar()

rb1 = tk.Radiobutton(my_app, variable="radioValue", value="1")
ctrls.append(rb1)
rb2 = tk.Radiobutton(my_app, variable="radioValue", value="2")
ctrls.append(rb2)
rb3 = tk.Radiobutton(my_app, variable="radioValue", value="3")
ctrls.append(rb3)
rb4 = tk.Radiobutton(my_app, variable="radioValue", value="4")
ctrls.append(rb4)

for i in range(len(ctrls)):
    ctrls[i].grid(row=i)

# rbAdd.grid(row=0)
my_app.mainloop()