import random

yahtzees = 0
for n in range(1, 100000000):
	num1 = random.randrange(1, 7)
	num2 = random.randrange(1, 7)
	num3 = random.randrange(1, 7)
	num4 = random.randrange(1, 7)
	num5 = random.randrange(1, 7)
	if(num1 == num2 and num1 == num3 and num1 == num4 and num1 == num5):
		yahtzees += 1
		print(yahtzees / n)
print(yahtzees / n)
