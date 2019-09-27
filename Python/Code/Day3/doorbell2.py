import tkinter as tk
def doorbell(event):
    print(" You rang the Doorbell !")
window = tk.Tk()
window.title(" Doorbell App")
window.geometry("400x500")
mylabel=tk.Label(text="Doorbell App")
mylabel.grid(column=190,row=10)
mybutton = tk.Button(window, text = "Doorbell")
mybutton.grid(column=200,row=200)
mybutton.bind("<Button-1>",doorbell)
window.mainloop()
