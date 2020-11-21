from tkinter import *
import backend
backend.connect()
window = Tk()

l1 = Label(window,text='Title')
l1.grid(row=0,column=0)

l2 = Label(window,text='Author')
l2.grid(row=0,column=2)

l3 = Label(window,text='Year')
l3.grid(row=1,column=0)

l4 = Label(window,text='ISBN')
l4.grid(row=1,column=2)

titleText = StringVar()
e1 = Entry(window,textvariable=titleText)
e1.grid(row=0,column=1)

authorText = StringVar()
e2 = Entry(window,textvariable=authorText)
e2.grid(row=0,column=3)

yearText = IntVar()
e3 = Entry(window,textvariable=yearText)
e3.grid(row=1,column=1)

isbnText = IntVar()
e4 = Entry(window,textvariable=isbnText)
e4.grid(row=1,column=3)

list = Listbox(window,height=9,width=35)
list.grid(row=2,column=0,rowspan=6,columnspan=2)
sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list.configure(yscrollcommand=sb1.set)
sb1.configure(command=list.yview)

def get_selected_row(event):
    global selected_tuple
    index = list.curselection()[0]
    selected_tuple = list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])




list.bind('<<ListboxSelect>>',get_selected_row)

def viewAll():
    list.delete(0,END)
    for i in backend.view():
        list.insert(END,i)
b1 = Button(window,text='View All',width=12,command=viewAll)
b1.grid(row=2,column=3)

def search():
    list.delete(0,END)
    for i in backend.search(title=titleText.get(),author=authorText.get(),year=yearText.get(),isbn=isbnText.get()):
        list.insert(END,i)
b2 = Button(window,text='Search',width=12,command=search)
b2.grid(row=3,column=3)

def add():
    backend.insert(titleText.get(), authorText.get(), yearText.get(), isbnText.get())
b3 = Button(window,text='Add',width=12,command=add)
b3.grid(row=4,column=3)

def update():
    backend.update(selected_tuple[0],titleText.get(),authorText.get(),yearText.get(),isbnText.get())
    viewAll()
b4 = Button(window,text='Update',width=12,command=update)
b4.grid(row=5,column=3)

def delete():
    backend.delete(selected_tuple[0])
    viewAll()


b5 = Button(window,text='Delete',width=12,command=delete)
b5.grid(row=6,column=3)

def close():
    pass
b6 = Button(window,text='Close',width=12,command=window.destroy)
b6.grid(row=7,column=3)




window.mainloop()


