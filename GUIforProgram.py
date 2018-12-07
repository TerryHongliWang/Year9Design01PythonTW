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

def clickedQuiz(quizClicked):
	print("quiz started")

	if quizClicked % 2 == 0:
		quizStart1.grid(row = 1, column = 7)
		quizStart2.grid(row = 2, column = 7)
		quizClicked += 1 
	if quizClicked % 2 == 1:
		quizStart1.grid_forget()
		quizStart2.grid_forget()
		quizClicked -= 1

def boom():
	print("i")

root = tk.Tk()
root.geometry("1080x720")
root.config(background = "floralwhite")

elementsTop = tk.Label(root, text = "Elements:")
elementsTop.config(width = 17, height = 2, background = "grey97")
elementsTop.grid(row = 0, column = 0, columnspan = 2)

searchIn = tk.Entry(root, width = 16)
searchIn.config()
searchIn.grid(columnspan = 2)
searchIn.grid_forget()

searchOut = tk.Button(root, text = "Search:_______", command = clickedSearch)
searchOut.config(width = 17, height = 2, background = "cadetblue1")
searchOut.grid(row = 0, column = 2, columnspan = 2)

btnSearch = tk.Button(root, text = "Search", command = searchFor)
btnSearch.config(width = 17, height = 2, font = ("Sans", "7"), background = "grey")
btnSearch.grid(row = 1, column = 2, columnspan = 2)

connectors = tk.Label(root, text = "Connectors:                             ")
connectors.config(borderwidth = 1, relief = "solid", width = 28, height = 2, background = "mistyrose")
connectors.grid(row = 0, column =  5, columnspan = 2)

btnConnect = tk.Label(root, text = "   •‒‒‒‒‒‒‒‒‒•")
btnConnect.config(width = 11, height = 1, background = "mistyrose")
btnConnect.grid(row = 0, column = 6)

electrons = 0
neutrons = 0
electrons = str(electrons)
neutrons = str(neutrons)
textdisplay = "Ⓔ: " +str(electrons)+"    Ⓝ: " + str(neutrons)
electronNeutrons = tk.Label(root, text = textdisplay)
electronNeutrons.config(borderwidth = 1, relief = "solid", height = 2, width = 11)
electronNeutrons.grid(row = 0, column = 7)

elementsCont = tk.Canvas(root)
elementsCont.config(height = 17, width = 7)
elementsCont.grid(row = 1, column = 0)

ELEMENTS = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P",
 "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga",
  "Ge", "As", "Se", "Br", "Kr", "Rb"]

ELEINDEX = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
 "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32",
  "33", "34", "35", "36", "37"]

btnElements = []


for i in range(0,len(ELEMENTS)-1, 2):
	btnElements.append(tk.Button(root, text = ELEMENTS[i] + "\n\n" + ELEINDEX[i] + "\n", width = 7,
	 command = boom, highlightcolor = "black", highlightbackground = "#ff7777", highlightthickness = 0,
	  relief = "flat", foreground = "#ad3737"))
	btnElements[i].grid(row = i+1, column = 0)
	#btnElements.append(tk.Label(root, text = ELEINDEX[i], width = 7, highlightcolor = "black", highlightbackground = "#ff7777", highlightthickness = 0, relief = "flat", foreground = "#ad3737"))
	#btnElements[i].grid(row = i+1, column = 0)
	btnElements.append(tk.Button(root, text = ELEMENTS[i+1] + "\n\n\n", width = 7, command = boom))
	btnElements[i+1].grid(row = i+1, column = 1)


btnQuiz = tk.Button(root, text = "Start Quiz/Game", command = clickedQuiz)
btnQuiz.config(width = 17, height = 2 )
btnQuiz.grid(row = 0, column = 8)

quizStart1 = tk.Label(root, text = "Find the compound:\n")
quizStart1.config(width = 17, height = 2, font = ("Sans", "12"))

quizStart2 = tk.Label(root, text = "Carbon Dioxide")
quizStart2.config(width = 17, height = 1, font = ("Sans", "12", "bold"))













 








root.mainloop()