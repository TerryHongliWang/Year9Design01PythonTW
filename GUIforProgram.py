import tkinter as tk


def clickedSearch():
	print("test")

	searchOut.grid_forget()
	searchIn.grid(row = 0, column = 7, columnspan = 2)
	btnSearch.grid(row = 0, column = 7)

def searchFor():
	temp = searchIn.get()
	print(temp)
	if len(searchIn.get()) == 0:
		searchIn.grid_forget()
		searchOut.grid(row = 0, column = 7)
	btnSearch.grid(row = 0, column = 7)

quizClicked = 2

def clickedQuiz(quizClicked):
	print("quiz started")

	if quizClicked % 2 == 0:
		quizStart1.grid(row = 1, column = 12)
		quizStart2.grid(row = 2, column = 12)
		quizClicked += 1 
	if quizClicked % 2 == 1:
		quizStart1.grid_forget()
		quizStart2.grid_forget()
		quizClicked -= 1

def clickedBtn():
	#print(event)
	print("f")
	#currentDisplay.append(ELEMENTS[data[0]])
	#print (currentDisplay)

def boom():
	print("i")

root = tk.Tk()
root.geometry("1440x1080")
root.config(background = "floralwhite")

elementsTop = tk.Label(root, text = "Elements:")
elementsTop.config(width = 49, height = 2, background = "grey97")
elementsTop.grid(row = 0, column = 0, columnspan = 7)

searchIn = tk.Entry(root, width = 16)
searchIn.config()
searchIn.grid(columnspan = 2)
searchIn.grid_forget()

searchOut = tk.Button(root, text = "Search:_______", command = clickedSearch)
searchOut.config(width = 17, height = 2, background = "cadetblue1")
searchOut.grid(row = 0, column = 7, columnspan = 2)

#btnSearch = tk.Button(root, text = "Search", command = searchFor)
#btnSearch.config(width = 17, height = 2, font = ("Sans", "7"), background = "grey")
#btnSearch.grid(row = 1, column = 6, columnspan = 2)

connectors = tk.Label(root, text = "Connectors:                             ")
connectors.config(borderwidth = 1, relief = "solid", width = 28, height = 2, background = "mistyrose")
connectors.grid(row = 0, column =  10, columnspan = 2)

btnConnect = tk.Label(root, text = "   •‒‒‒‒‒‒‒‒‒•")
btnConnect.config(width = 11, height = 1, background = "mistyrose")
btnConnect.grid(row = 0, column = 11)

electrons = 0
neutrons = 0
electrons = str(electrons)
neutrons = str(neutrons)
textdisplay = "Ⓔ: " + str(electrons)+ "    Ⓝ: " + str(neutrons)
electronNeutrons = tk.Label(root, text = textdisplay)
electronNeutrons.config(borderwidth = 1, relief = "solid", height = 2, width = 11)
electronNeutrons.grid(row = 0, column = 12)

elementsCont = tk.Canvas(root)
elementsCont.config(height = 17, width = 7)
elementsCont.grid(row = 1, column = 0)

currentDisplay = ["C", "O", "O"]

carbonDioxide = ["C", "O", "O"]
water = ["H", "O", "O"]

COMPOUNDS = (carbonDioxide, water)

print (currentDisplay.count("C"))

#compoundSide = tk.Label(root, text = )

displayed = tk.Label(root, text = str(currentDisplay))
displayed.config(height = 2, width = 37, background = "floralwhite", foreground = "deeppink3", font = ("Sans", "27"))
displayed.grid(row = 1, column = 2, columnspan = 11)

data = [0]

ELEMENTS = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P",
 "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga",
  "Ge", "As", "Se", "Br", "Kr", "Rb" , "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
   "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd",
    "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
     "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
     "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg",
      "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

ELEINDEX = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", 
"17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32",
"33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48",
 "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64",
  "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
   "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96",
    "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110",
     "111", "112", "113", "114", "115", "116", "117", "118"]


btnElements = []

for i in range(0,len(ELEMENTS)-6, 7):

	btnElements.append(tk.Button(root, text = ELEMENTS[i] + "\n" + ELEINDEX[i], width = 7,
	 command = clickedBtn, highlightcolor = "black", highlightbackground = "#ff7777", highlightthickness = 0,
	  relief = "flat", foreground = "#373737"))
	btnElements[i].grid(row = i+2, column = 0)
	#btnElements.append(tk.Label(root, text = ELEINDEX[i], width = 7, highlightcolor = "black", highlightbackground = "#ff7777", highlightthickness = 0, relief = "flat", foreground = "#ad3737"))
	#btnElements[i].grid(row = i+1, column = 0)
	btnElements.append(tk.Button(root, text = ELEMENTS[i+1] + "\n" + ELEINDEX[i+1], width = 7,
	 command = clickedBtn, highlightcolor = "black", highlightbackground = "#ff7000", highlightthickness = 0,
	  relief = "flat", foreground = "#373737"))
	btnElements[i+1].grid(row = i+2, column = 1)
	btnElements.append(tk.Button(root, text = ELEMENTS[i+2] + "\n" + ELEINDEX[i+2], width = 7,
	 command = clickedBtn, highlightcolor = "black", highlightbackground = "#fff777", highlightthickness = 0,
	  relief = "flat", foreground = "#373737"))
	btnElements[i+2].grid(row = i+2, column = 2)
	btnElements.append(tk.Button(root, text = ELEMENTS[i+3] + "\n" + ELEINDEX[i+3], width = 7,
	 command = clickedBtn, highlightcolor = "black", highlightbackground = "#7fff00", highlightthickness = 0,
	  relief = "flat", foreground = "#373737"))
	btnElements[i+3].grid(row = i+2, column = 3)
	btnElements.append(tk.Button(root, text = ELEMENTS[i+4] + "\n" + ELEINDEX[i+4], width = 7,
	 command = clickedBtn, highlightcolor = "black", highlightbackground = "#00f7ff", highlightthickness = 0,
	  relief = "flat", foreground = "#373737"))
	btnElements[i+4].grid(row = i+2, column = 4)
	btnElements.append(tk.Button(root, text = ELEMENTS[i+5] + "\n" + ELEINDEX[i+5], width = 7,
	 command = clickedBtn, highlightcolor = "black", highlightbackground = "#0007ff", highlightthickness = 0,
	  relief = "flat", foreground = "#373737"))
	btnElements[i+5].grid(row = i+2, column = 5)
	btnElements.append(tk.Button(root, text = ELEMENTS[i+6] + "\n" + ELEINDEX[i+6], width = 7, 
		command = clickedBtn, highlightcolor = "black", highlightbackground = "#7700ff", highlightthickness = 0,
	  relief = "flat", foreground = "#373737"))
	btnElements[i+6].grid(row = i+2, column = 6)



btnQuiz = tk.Button(root, text = "Start Quiz/Game", command = clickedQuiz)
btnQuiz.config(width = 17, height = 2 )
btnQuiz.grid(row = 0, column = 13)

quizStart1 = tk.Label(root, text = "Find the compound:\n")
quizStart1.config(width = 17, height = 2, font = ("Sans", "12"))

quizStart2 = tk.Label(root, text = "Carbon Dioxide")
quizStart2.config(width = 17, height = 1, font = ("Sans", "12", "bold"))













 








root.mainloop()