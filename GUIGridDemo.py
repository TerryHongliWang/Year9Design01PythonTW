import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text = "Welcome to Yes!")
label.grid(row = 0, column = 0, columnspan = 2)

btn1 = tk.Button(root, text = "1")
btn1.config(width = 7, height = 3)
btn1.grid(row = 1, column = 0, sticky = "NESW")

btn2 = tk.Button(root, text = "2")
btn2.config(width = 7, height = 3)
btn2.grid(row = 1, column = 1, sticky = "NESW")

btn3 = tk.Button(root, text = "3")
btn3.config(width = 7, height = 3)
btn3.grid(row = 2, column = 0, sticky = "NESW")

btn4 = tk.Button(root, text = "4")
btn4.config(width = 7, height = 3)
btn4.grid(row = 2, column = 1, sticky = "NESW")

root.mainloop()