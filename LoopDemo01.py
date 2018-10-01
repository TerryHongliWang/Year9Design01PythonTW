#Example !:
print("0")
print("1")
print("2")
print("3")
print("4")
print("*******")

#start from first number, check if less than second number and go up by third number
#first number default 0, third number default 1, only need middle number
for i in range(0, 10, 1):
	print(i)

#negative always check for more than
for i in range(10, -1, -1):
	print(i)

#use function len
print("*******")
mky = "Monkey"
for i in range(len(mky)):
	print(mky[i])

print("*******")
mky = "Monkey"
for i in range(len(mky) -1, -1, -1):
	print(mky[i])

print("*******")
for i in range(0, len(mky), 2):
	print(mky[i])
