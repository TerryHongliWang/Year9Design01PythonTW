import os

print("°°°°°°°Slope Calculator°°°°°°°")
#Python always assumes that your input is a
#a string unless you tell it. 
#To make a numeric type you have two options
#decimals - float
#integers - int


os.system("say This is my slope calculator")
#Input - CHANGE
x1 = input("What is your first x(x1): ")
x1 = int(x1) #casting

y1 = input("What is your first y(y1): ")
y1 = int(y1)

x2 = input("What is your second x(x2): ")
x2 = int(x2)

y2 = input("What is your second y(y2): ")
y2 = int(y2)


#Process
rise = x2 - x1
run = y2 - y1

if run == 0:
	fSlope = "undefined"
else:
	fSlope = rise/run #real numbers are called float

#Three types to consider
#Strings - Store collections of characters
# result = str(<value>)
#integers - Store integer values
# result = int(<value>)
#floats - Store real numbers
# result = float(<value>)



#Output
print("Your slope is m = "+str(rise)+"/"+str(run))
print("Your slope as a decimal is",fSlope)
print("Your rise is:" +str(rise))
print("Your run is:" +str(run))











