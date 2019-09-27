import tkinter as tk
window=tk.Tk()
window.title("My favorite sports player")
window.geometry("300x200")
mylabel=tk.Label(text="P. V. Sindhu Badminton player")
mylabel.grid(column=0,row=0)
button_name = tk.Button(window, text = "Click Me")
button_name.grid(column=3,row=3)
window.mainloop()