import tkinter as tk

root = tk.Tk()

output = tk.Text(root, height = 10, width = 30)
output.config(state = "disable", background = "grey77")
output.grid(row = 0, column = 0, rowspan = 5)

labInput1 = tk.Label(root, text = "Input 1")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root, text = "Input 2")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root, text = "Input 3")
labInput3.grid(row = 7, column =  0)

var1 = tk.IntVar()
var2 = tk.Intvar()

cHC = tk.Checkbutton(root, text = "Expand", variable = var)

cLF = tk.Checkbutton(root, text = "expand", variable = var)
cLF.grid(row = 1, column = 1)

root.mainloop()