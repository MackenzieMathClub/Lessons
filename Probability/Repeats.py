import random

REPEAT_COUNT = 3
repeats = 0
for n in range(1, 10000000):
	nums = []
	nums.append(random.randrange(1, 7))
	nums.append(random.randrange(1, 7))
	nums.append(random.randrange(1, 7))
	nums.append(random.randrange(1, 7))
	nums.append(random.randrange(1, 7))

	hasRepeat = False
	for i in range(1, 7):
		if (nums.count(i) == REPEAT_COUNT):
			hasRepeat = True
	if (hasRepeat):
		repeats += 1
		print(repeats / n)

print(repeats / n)
