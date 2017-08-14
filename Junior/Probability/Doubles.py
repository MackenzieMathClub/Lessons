import random

sums = [0, 0, 0, 0, 0]

for n in range(1, 1000000):
	num1 = random.randrange(1, 3)
	num2 = random.randrange(1, 3)
	sums[num1 + num2] += 1

for i in range(2, len(sums)):
	print(i, sums[i] / n)
