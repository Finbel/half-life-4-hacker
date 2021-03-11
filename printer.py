import functions as fun
import numpy as np
from fractions import Fraction

f = open("input.txt")
words = f.readlines()
words2 = [word[:-1] for word in words[:-1]]
words = words2 + words[-1:]

print("words", end="")
for word in words:
	print("|"+word,end="")
print()
print(":--|:--|:--|:--|:--|:--|:--")
n=len(words)
likeness_matrix = np.zeros((n,n))
for i in range(0,n):
	for j in range(i,n):
		likeness_matrix[i][j] = fun.likeness(words[i],words[j])

for i in range(0,n):
	print("**"+words[i]+"**",end="")
	for j in range(0,n):
		print("|"+str(int(likeness_matrix[i][j])),end="")
	print()

elimination_matrix = np.zeros((n,5))
for i in range(0,n):
	row = likeness_matrix[i]
	for j in range(0,5):
		elimination_matrix[i][j] = fun.eliminates(j,row)
print()
print("w\l|0|1|2|3|4")
print(":--|:--|:--|:--|:--|:--")
for i in range(0,n):
	print("**"+words[i]+"**",end="")
	for j in range(0,5):
		print("|"+str(int(elimination_matrix[i][j])),end="")
	print()

probability_matrix = np.zeros((n,5))
for i in range(0,n):
	row = likeness_matrix[i]
	for j in range(0,5):
		probability_matrix[i][j] = fun.probability(j,row)
print()
print("w\l|0|1|2|3|4")
print(":--|:--|:--|:--|:--|:--")
for i in range(0,n):
	print("**"+words[i]+"**",end="")
	for j in range(0,5):
		a = Fraction(probability_matrix[i][j]).limit_denominator()
		if a.numerator == 0:
			print("|"+ str(a.numerator),end="")
		else:
			print("|"+ str(a.numerator) + "/" + str(a.denominator),end="")
	print()

information_vector = np.zeros(n)
for i in range(0,n):
	a = elimination_matrix[i]
	b = probability_matrix[i]
	information_vector[i]=np.dot(a,b)*6

print()
print("words|expected to eliminate")
print(":--|:--:")
for i in range(0,n):
	print(words[i] + "|" + str(round(information_vector[i],4)))