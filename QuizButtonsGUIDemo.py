import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text = "Quiz of compounds")
label.config(width = 17, height = 3, font = ("Sans", "17", "bold"), fg = "dodgerblue")
label.grid(row = 0, column = 0, columnspan = 1)

btn1 = tk.Button(root, text = "Start Quiz/Game")
btn1.config(width = 17, height = 4, font = ("Sans", "17", "bold"), fg = "grey37")
btn1.grid(row = 1, column = 0, sticky = "NESW")

btn2 = tk.Button(root, text = "Hint 1")
btn2.config(width = 17, height = 3, font = ("Sans", "11"), fg = "grey77")
btn2.grid(row = 2, column = 0, sticky = "NESW")

btn3 = tk.Button(root, text = "Hint 2")
btn3.config(width = 17, height = 3, font = ("Sans", "11"), fg = "grey77")
btn3.grid(row = 3, column = 0, sticky = "NESW")

btn4 = tk.Button(root, text = "Hint 3")
btn4.config(width = 17, height = 3, font = ("Sans", "11"), fg = "grey77")
btn4.grid(row = 4, column = 0, sticky = "NESW")

root.mainloop()