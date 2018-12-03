import tkinter as tk


def clickedSearch():
	print("test")

	searchOut.grid_forget()
	searchIn.grid(row = 0, column = 2, columnspan = 2)
	btnSearch.grid(row = 0, column = 2)

def searchFor():
	temp = searchIn.get()
	print(temp)
	if len(searchIn.get()) == 0:
		searchIn.grid_forget()
		searchOut.grid(row = 0, column = 2)
	btnSearch.grid(row = 0, column = 2)

quizClicked = 2

def clickedQuiz():
	print("quiz started")

	if quizClicked % 2 == 0:
		quizStart1.grid(row = 1, column = 7)
		quizStart2.grid(row = 2, column = 7)
		quizClicked += 1 
	if quizClicked % 2 == 1:
		quizStart1.grid_forget()
		quizStart2.grid_forget()
		quizClicked -= 1

root = tk.Tk()
root.geometry("1080x720")

elementsTop = tk.Label(root, text = "Elements:")
elementsTop.config(width = 17, height = 2, background = "grey97")
elementsTop.grid(row = 0, column = 0, columnspan = 2)

searchIn = tk.Entry(root, width = 16)
searchIn.grid(columnspan = 2)
searchIn.grid_forget()

searchOut = tk.Button(root, text = "Search:_______", command = clickedSearch)
searchOut.config(width = 17, height = 2)
searchOut.grid(row = 0, column = 2, columnspan = 2)

btnSearch = tk.Button(root, text = "Search", command = searchFor)
btnSearch.config(width = 3, height = 2, font = ("Sans", "7"))
btnSearch.grid(row = 0, column = 2)

connectors = tk.Label(root, text = "Connectors:                             ")
connectors.config(borderwidth = 1, relief = "solid", width = 28, height = 2)
connectors.grid(row = 0, column =  5, columnspan = 2)

btnConnect = tk.Label(root, text = "   •‒‒‒‒‒‒‒‒‒•")
btnConnect.config(width = 11, height = 1, background = "white")
btnConnect.grid(row = 0, column = 6)

electrons = 0
neutrons = 0
electrons = str.electrons
neutrons = str.neutrons

electronNeutrons = tk.Label(root, text = "Ⓔ:", electrons, "Ⓝ:", neutrons)
electronNeutrons.config(borderwidth = 1, relief = "solid", height = 2)
electronNeutrons.grid(row = 0, column = 7)

ELEMENTS = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P",
 "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga",
  "Ge", "As", "Se", "Br", "Kr", "Rb"]

btnElements = []

elCol = 0
elRow = 1

#for i in range(len(ELEMENTS), 1):
	#if i % 2 == 1:
		#elRow += 1
		#elCol -= 1
	#elif i % 2 == 0:
		#elCol += 1
	#btnElements.append(tk.Button(root, text = ELEMENTS[i-1])
	#btnElements[i-1].config(width = 7, font = ("Sans", "11"))
	#btnElements[i-1].grid(row = elRow, column = elCol)


btnQuiz = tk.Button(root, text = "Start Quiz/Game", command = clickedQuiz)
btnQuiz.config(width = 17, height = 2 )
btnQuiz.grid(row = 0, column = 7)

quizStart1 = tk.Label(root, text = "Find the compound:\n")
quizStart1.config(width = 17, height = 2, font = ("Sans", "12"))

quizStart2 = tk.Label(root, text = "Carbon Dioxide")
quizStart2.config(width = 17, height = 1, font = ("Sans", "12", "bold"))


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