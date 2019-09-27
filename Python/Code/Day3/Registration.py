from tkinter import *

window=Tk()
window.geometry('500x500')
window.title("Registration Form")

def sel():
   selection = "You selected the option " + str(var.get())
   label_4.config(text = selection)

def submitform(event):
    label_5.config(text="You have successfully submitted registration form")

    
var = IntVar()   
label_0=Label(window, text="  Registration form  ",fg='blue' , bg='yellow', relief=RAISED, width=20,font=("arial",20,"bold"))
label_0.place(x=90,y=53)
#appearance  FLAT, SOLID , GROVE, RIDGE, SUNKEN, RAISED
label_1=Label(window, text="Full Name",width=20,font=("bold",10))
label_1.place(x=80,y=130)
entry_1=Entry(window)
entry_1.place(x=240,y=130)


label_2=Label(window, text="Email",width=20,font=("bold",10))
label_2.place(x=80,y=180)
entry_2=Entry(window)
entry_2.place(x=240,y=180)


label_3=Label(window, text="Gender",width=20,font=("bold",10))
label_3.place(x=80,y=230)
r1=Radiobutton(window, text="Male", variable=var, value=1,command=sel)
r1.place(x=240,y=230)
r2=Radiobutton(window, text="Female", variable=var, value=2,command=sel)
r2.place(x=310,y=230)


label_4 = Label(window)
label_4.place(x=250,y=260)

label_5 = Label(window)
label_5.place(x=100,y=360)

button_1=Button(window, text="submit", fg='white',bg='brown', relief=RIDGE, font=("arial",12,"bold"))
button_1.place(x=280, y=450)
button_1.bind("<Button-1>",submitform)

    
##GROVE, RIDGE, SUNKEN, RAISED
window.mainloop()




