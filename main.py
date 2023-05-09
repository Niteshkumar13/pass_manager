from tkinter import *
from tkinter import messagebox
import random
window = Tk()
window.minsize(500,450)
imagee = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image=imagee)
canvas.pack(padx=100)
label1 = Label(text="Web_Name",font=("Rockwell Extra Bold",13))
label1.pack()
label1.place(x=20,y=200)
entry1 = Entry(font=("arial",14),width=25)
entry1.pack()
entry1.focus()
entry1.place(x=200,y=200)
label2 = Label(text="Username/Email",font=("Rockwell Extra Bold",12))
label2.pack()
label2.place(x=20,y=250)
entry2 = Entry(font=("arial",14),width=25)
entry2.pack()
entry2.place(x=200,y=250)
label3 = Label(text="password",font=("Rockwell Extra Bold",13))
label3.pack()
label3.place(x=20,y=300)
entry3 = Entry(font=("arial",14),width=17)
entry3.pack()
entry3.place(x=200,y=300)
def submit():
    with open("dbf.txt","a") as text_file:
        x = entry1.get()
        y = entry2.get()
        z = entry3.get()
        if len(x) == 0 or len(y) == 0 or len(z) == 0:
            messagebox.showinfo(title="oops",message="you have missed some field")
        else:
            text_file.write(f"{x} | {y} | {z}\n")
            entry3.delete(0,END)
            entry1.delete(0,END)
            entry2.delete(0, END)

def password():
    entry3.delete(0,END)
    c_alpha = [chr(x) for x in range(65,91)]
    s_alpha = [chr(x) for x in range(97,123)]
    special_chr = ["@","!","*","$","&","(",")","#"]
    list = []
    for _ in range(3):
        list.append(random.choice(c_alpha))
        list.append(random.choice(s_alpha))
        list.append(random.choice(special_chr))
    random.shuffle(list)
    s = "".join(list)
    entry3.insert(0, s)

button1 = Button(width=10,text="gen_pass",
                 font=("arial",10),
                 bg="Tomato",
                 fg="blue",
                 activebackground="tomato",
                 activeforeground="blue",
                 borderwidth=0,
                 command=password
                 )
button1.pack()
button1.place(x=400,y=300)
submit = Button(text="Submit",
                fg="blue",
                bg="Tomato",
                activeforeground="blue",
                activebackground="Tomato",
                borderwidth=0,
                command=submit
                )
submit.pack()
submit.place(x=240,y=350)

window.mainloop()