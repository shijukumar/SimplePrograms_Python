#Sum of N numbers output in Messagebox

from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.geometry("300x250")
main_window.title("Sum of N numbers")

heading_font = ("Arial", 21,'bold')
label_font = ("TimesNewRoman",14)
button_font = ("TimesNewRoman",11)
sumofn_label = Label(main_window,text = "Sum of N numbers",bg = '#FFC312',fg = '#ff3f34',font = heading_font)
sumofn_label.pack(pady = 10)

def calc_sumof_n():
    total = 0
    n = int(entry_n.get())
    for num in range (n+1):
        total = total + num
    messagebox.showinfo("RESULT",total)
def reset():
    entry_n.delete(0,END)

frame = Frame(main_window)
frame.pack()
label_n = Label(frame,text = "Enter the nth number",font = label_font)
label_n.grid(row = 0,column = 0,pady = 10)
entry_n = Entry(frame,width = 5,font = label_font)
entry_n.grid(row = 0,column = 1)
calc_btn = Button(frame,text="CALCULATE",bg = '#34e7e4',font = button_font,command = calc_sumof_n)
calc_btn.grid(columnspan = 2,pady = 20)
reset_btn = Button(frame,text="RESET",bg = '#d63031',font = button_font,command = reset)
reset_btn.grid(columnspan = 2,pady = 20)
main_window.mainloop()
