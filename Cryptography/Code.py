# Simplified Euclidean algorithm

import sys
from fractions import gcd
from math import floor

def simplifiedGCD(a, b):
	if (b == 0):
		return a
	a = a % b
	return simplifiedGCD(b, a)

def simplifiedMod(a, b):
	return a - b * floor(a / b)

# Find the inverse of a under mod b.
def inverseMod(a, b):
	for i in range(1, b + 1):
		if (a * i) % b == 1:
			return i
	return -1
print(inverseMod(17, 60))
