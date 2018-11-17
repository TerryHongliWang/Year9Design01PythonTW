carbonCount = 0
oxygenCount = 0

carbon = 6
oxygen = 8

carbonDioxide = [carbon, oxygen, oxygen]

for i in carbonDioxide:
	if i == carbon:
		carbonCount = carbonCount + 1
	elif i == oxygen:
		oxygenCount = oxygenCount + 1

print(carbonCount)
print(oxygenCount)
