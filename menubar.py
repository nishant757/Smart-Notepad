from tkinter import *


def hello():
    str = T.get(1.0, END)
    print(str)


root = Tk()
menubar = Menu()
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_command(label="Save as", command=hello)
filemenu.add_command(label="Close", command=hello)
filemenu.add_command(label="Exit", command=hello)
root.config(menu=menubar)
S = Scrollbar(root)
T = Text(root, height=2, width=30)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
str = 'my name is nishant' \
      'i name 20 year old' \
      'ley me do my work' \
      'dont disturb' \
      ''
T.insert(END, str)
T.tag_add("name", '1.0', '1.5')
T.tag_config("name", background="yellow", foreground="blue")
s = []
for i in str:
    q = T.search("n", '1.0', stopindex=END)
    s.append(q)

root.mainloop()


'''from tkinter import *
from tkinter import ttk


def func(e):
    l2.config(text=cb.get())


root = Tk()
root.geometry('300x500')
course = ("java", 'python', 'c', 'c++')
l1 = Label(root, text="choose")
l1.grid(row=0, column=0)
cb = ttk.Combobox(root, values=course, width=20, state='readonly')
cb.grid(row=1, column=0)
cb.current(0)
cb.bind("<<ComboboxSelected>>", func)
b = Button(root, text="click", command=func)
b.grid(row=2, column=0)
l2 = Label(root, text="")
l2.grid(row=3, column=0)
root.mainloop()'''




