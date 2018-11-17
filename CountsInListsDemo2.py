hydrogenCount = 0
oxygenCount = 0
sulfurCount = 0

hydrogen = 1
oxygen = 8
sulfur = 16

unknownCompound1 = [hydrogen, hydrogen, sulfur, oxygen, oxygen, oxygen, oxygen]

for i in unknownCompound1:
	if i == hydrogen:
		hydrogenCount = hydrogenCount + 1
	elif i == oxygen:
		oxygenCount = oxygenCount + 1
	elif i == sulfur:
		sulfurCount = sulfurCount + 1

if hydrogenCount == 2 and sulfurCount == 1 and oxygenCount == 4:
	print("This is Sulfuric Acid")
elif hydrogenCount == 2 and sulfurCount == 1 and oxygenCount == 3:
	print("This is Sulfurous Acid")