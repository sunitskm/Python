from tkinter import *
from backend import Database
database = Database()

window = Tk()
window.title("Sunit's Library")
def displayEntry(event):
    try:
        index = list_box.curselection()[0]
        selected_tuple = list_box.get(index)
        #print(index)
        #print(selected_tuple)
        global id_selected
        id_selected = selected_tuple[0]
        t = selected_tuple[1]
        a = selected_tuple[2]
        y = selected_tuple[3]
        i = selected_tuple[4]
        e1.delete(0,END)
        e1.insert(END,t)
        e2.delete(0,END)
        e2.insert(END,a)
        e3.delete(0,END)
        e3.insert(END,y)
        e4.delete(0,END)
        e4.insert(END,i)
    except IndexError:
        pass
def viewCommand():
    list_box.delete(0,END)
    rows = database.view_all()
    for row in rows:
        list_box.insert(END,row)
def searchCommand():
    list_box.delete(0,END)
    t = e_title.get()
    a = e_author.get()
    y = e_year.get()
    i = e_isbn.get()
    rows = database.search_entry(t,a,y,i)
    for row in rows:
        list_box.insert(END,row)
def addCommand():
    list_box.delete(0,END)
    t = e_title.get()
    a = e_author.get()
    y = e_year.get()
    i = e_isbn.get()
    database.add_entry(t,a,y,i)
    list_box.insert(END,(t,a,y,i))
def delCommand():
    database.delete_entry(id_selected)

def updateCommand():
    t = e_title.get()
    a = e_author.get()
    y = e_year.get()
    i = e_isbn.get()
    database.update_entry(id_selected,t,a,y,i)
l1 = Label(window,text = "Title")
l1.grid(row = 0,column = 0)
l2 = Label(window,text = "Author")
l2.grid(row = 0,column = 2)
l3 = Label(window,text = "Year")
l3.grid(row = 1,column = 0)
l4 = Label(window,text = "ISBN")
l4.grid(row = 1,column = 2)
e_title = StringVar()
e1 = Entry(window,textvariable = e_title)
e1.grid(row = 0,column = 1)
e_author = StringVar()
e2 = Entry(window,textvariable = e_author)
e2.grid(row = 0,column = 3)
e_year = StringVar()
e3 = Entry(window,textvariable = e_year)
e3.grid(row = 1,column = 1)
e_isbn = StringVar()
e4 = Entry(window,textvariable = e_isbn)
e4.grid(row = 1,column = 3)
list_box = Listbox(window,height = 10,width = 35)
list_box.grid(row = 2,column = 0,rowspan = 6, columnspan = 2)
scrollbar = Scrollbar(window)
scrollbar.grid(row = 2, column = 2,rowspan = 6)
list_box.config(yscrollcommand = scrollbar.set)
scrollbar.config(command=list_box.yview)
#try:
list_box.bind('<<ListboxSelect>>',displayEntry)
#except IndexError:
    #pass

b1 = Button(window,text = "View all",command = viewCommand)
b1.grid(row = 2, column = 3)

b2 = Button(window,text = "Search Entry", command = searchCommand)
b2.grid(row = 3, column = 3)
b3 = Button(window,text = "Add Entry",command = addCommand)
b3.grid(row = 4, column = 3)
b4 = Button(window,text = "Update Entry", command = updateCommand)
b4.grid(row = 5, column = 3)
b5 = Button(window,text = "Delete entry",command = delCommand)
b5.grid(row = 6, column = 3)
b6 = Button(window,text = "Close",command = window.destroy)
b6.grid(row = 7, column = 3)
#Entry to enter weight in kgs

window.mainloop()
