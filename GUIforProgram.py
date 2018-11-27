import tkinter as tk


def clickedSearch():
	print("test")

	searchOut.grid_forget()
	searchIn.grid(row = 0, column = 2)

def searchFor():
	if len(searchIn) == 0:
		searchIn.grid_forget()
		searchOut.grid(row = 0, column = 2)

root = tk.Tk()
root.geometry("1080x720")

elementsTop = tk.Label(root, text = "Elements:")
elementsTop.config(width = 17, height = 2, background = "grey97")
elementsTop.grid(row = 0, column = 0, columnspan = 2)

searchIn = tk.Entry(root, width = 16)
searchIn.grid_forget()

searchOut = tk.Button(root, text = "Search:_______", command = clickedSearch)
searchOut.config(width = 17, height = 2)
searchOut.grid(row = 0, column = 2)

btnSearch = tk.Button(root, text = "Search", command = searchFor)
btnSearch.config(width = 3, height = 2, font = ("Sans", "7"))
btnSearch.grid(row = 0, column = 2)

connectors = tk.Label(root, text = "Connectors: •-------• ")
connectors.config(borderwidth = 1, relief = "solid", height = 2)
connectors.grid(row = 0, column =  4)

electronNeutrons = tk.Label(root, text = "Ⓔ:#   Ⓝ:#")
electronNeutrons.config(borderwidth = 1, relief = "solid", height = 2)
electronNeutrons.grid(row = 0, column = 5)

ELEMENTS = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P",
 "S", "Cl", "Ar", "K", "Ca", "Sc", "ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga",
  "Ge", "As", "Se", "Br", "Kr", "Rb"]

#for i in (ELEMENTS):
	#if i % 2 == 1:
		#column += 1
	#elif i % 2 == 0:
		#column -= 1
		#row += 1

btn1 = tk.Button(root, text = "Start Quiz/Game")
btn1.config(width = 17, height = 2 )
btn1.grid(row = 0, column = 5)

btnH1 = tk.Button(root, text = "H\n\n\n")
btnH1.config(width = 7, font = ("Sans", "11"))
btnH1.grid(row = 1, column = 0)

btnHe2 = tk.Button(root, text = "He\n\n\n")
btnHe2.config(width = 7, font = ("Sans", "11"))
btnHe2.grid(row = 1, column = 1)

btnLi3 = tk.Button(root, text = "Li\n\n\n")
btnLi3.config(width = 7, font = ("Sans", "11"))
btnLi3.grid(row = 2, column = 0)

btnBe4 = tk.Button(root, text = "Be\n\n\n")
btnBe4.config(width = 7, font = ("Sans", "11"))
btnBe4.grid(row = 2, column = 1)

btnB5 = tk.Button(root, text = "B\n\n\n")
btnB5.config(width = 7, font = ("Sans", "11"))
btnB5.grid(row = 3, column = 0)

btnC6 = tk.Button(root, text = "C\n\n\n")
btnC6.config(width = 7, font = ("Sans", "11"))
btnC6.grid(row = 3, column = 1)

btnN7 = tk.Button(root, text = "N\n\n\n")
btnN7.config(width = 7, font = ("Sans", "11"))
btnN7.grid(row = 4, column = 0)

btnO8 = tk.Button(root, text = "O\n\n\n")
btnO8.config(width = 7, font = ("Sans", "11"))
btnO8.grid(row = 4, column = 1)





















root.mainloop()