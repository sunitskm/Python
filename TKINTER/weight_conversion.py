from tkinter import *
window = Tk()
window.title("KGTOALL")
window.geometry('500x500')
def kg_other():
    val_float = float(e_value.get())
    #Delete previous existing text to avoid overlapping of text entries
    t_g.delete(1.0,END)
    t_p.delete(1.0,END)
    t_o.delete(1.0,END)
    #Calculations for weights
    val_g = val_float * 1000.0
    val_p = val_float * 2.20462
    val_o = val_float * 35.274
    #Insert calculated values to text fields
    t_g.insert(END,val_g)
    t_p.insert(END,val_p)
    t_o.insert(END,val_o)

#Adding button
b = Button(window,text = "Convert",command = kg_other)
b.grid(row = 0, column = 2)
#Entry to enter weight in kgs
e_value = StringVar()
e = Entry(window,textvariable = e_value)
e.grid(row = 0, column = 1)
#Label to display kg
l = Label(window,text = "Kg")
l.grid(row = 0, column = 0)

#text fields
t_g = Text(window,height = 1,width = 20)
t_g.grid(row = 1,column = 0)
t_p = Text(window,height = 1,width = 20)
t_p.grid(row = 1,column = 1)
t_o = Text(window,height = 1,width = 20)
t_o.grid(row = 1,column = 2)
window.mainloop()
