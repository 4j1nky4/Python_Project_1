import tkinter
from time import strftime

root = tkinter.Tk()
root.title("Digital Clock")
root.configure(background='black')

def time():
    time_string = strftime('%H:%M:%S %p')
    date_string = strftime('%A, %B %d, %Y')
    time_label.config(text=time_string)
    date_label.config(text=date_string)
    time_label.after(1000, time)

time_label = tkinter.Label(root, font=('calibri', 72, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')

date_label = tkinter.Label(root, font=('calibri', 24), background='black', foreground='white')
date_label.pack(anchor='center')

time()
root.mainloop()