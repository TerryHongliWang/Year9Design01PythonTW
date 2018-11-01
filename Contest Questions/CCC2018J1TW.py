num1 = (input(""))
num2 = (input(""))
num3 = (input(""))
num4 = (input(""))
nope = 0

if num1 == 8 or num1 == 9:
	print("Ignore")
	if num2 == num3:
		print("Ignore")
		if num4 == 8 or num4 == 9:
			print("Ignore")
		else:
			print ("Answer")
	else:
		print("Answer")
else:
	print("Answer")

#Doesn't Work