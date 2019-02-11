from tkinter import *

window = Tk()
file = open('list_items.txt','a+')
window.title("To do list")
window.geometry('375x50')
def add_line():
    item = str(e_value.get())
    file.write(item+"\n")
    print(item)
    entry_1.delete(0,END)
def save_line():
    global file
    file.close()
    file = open('list_items.txt','a+')
def save_line_close():
    global file
    file.close()
    window.destroy()
button1 = Button(window,text="Add Line",command=add_line)
button1.grid(row=0,column=2)
button2 = Button(window,text="Save Changes",command=save_line)
button2.grid(row=0,column=3)
button3 = Button(window,text="Save and Close",command=save_line_close)
button3.grid(row=0,column=4)
e_value = StringVar()
entry_1 = Entry(window,textvariable = e_value)
entry_1.grid(row = 0,column = 0)

window.mainloop()
