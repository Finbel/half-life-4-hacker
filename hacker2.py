import numpy as np
f = open("input.txt")
words = f.readlines()
words2 = [word[:-1] for word in words[:-1]]
words = words2 + words[-1:]
likeness = 0
# number of words
n = len(words)
# possible liknesses
m = len(words[0])+1


def likeness(word1, word2):
	return sum(x[0]==x[1] for x in zip(word1,word2))

def eliminates(likeness, row):
	return sum(e != likeness for e in row)

def probability(likeness, row):
	return sum(e == likeness for e in row)/len(row)
#while likeness != -1:

# create likeness matrix
likeness_matrix = np.zeros((n,n))
for i in range(0,n):
	for j in range(0,n):
		likeness_matrix[i][j] = likeness(words[i],words[j]) 

# for i in range(0,n):
# 	for j in range(0,n):
# 		print(str(likeness_matrix[i][j]), end=" ")
# 	print()
# print()

# create elimination matrix
elimination_matrix = np.zeros((n,m))
for i in range(0,n):
	row = likeness_matrix[i]
	for j in range(0,m):
		elimination_matrix[i][j] = eliminates(j,row)

# for i in range(0,n):
# 	for j in range(0,n):
# 		print(str(elimination_matrix[i][j]), end=" ")
# 	print()
# print()

# create probability matrix
probability_matrix = np.zeros((n,m))
for i in range(0,n):
	row = likeness_matrix[i]
	for j in range(0,m):
		probability_matrix[i][j] = probability(j,row)

# for i in range(0,n):
# 	for j in range(0,n):
# 		print(str(probability_matrix[i][j]), end=" ")
# 	print()
# print()

information_vector = np.zeros(n)
for i in range(0,n):
	a = elimination_matrix[i]
	b = probability_matrix[i]
	information_vector[i]=np.dot(a,b)

for i in range(0,n):
	print(words[i] + " " + str(information_vector[i]))

selected = words[np.where(information_vector==max(information_vector))[0][0]] 
words.remove(selected)
print()
print(selected)
print()