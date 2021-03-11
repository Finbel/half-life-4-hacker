import numpy as np
import random as rn
import collections as col
import time




def printWords(words):
	for word in words:
		print(word)
	print()

def likeness(word1, word2):
	return sum(x[0]==x[1] for x in zip(word1,word2))

def update(words,selected,correct):
	l = likeness(selected,correct)
	return [word for word in words if likeness(selected,word)==l]

def game_update(words,selected, l):
	return [word for word in words if likeness(selected,word)==l]

def eliminates(likeness, row):
	return sum(e != likeness for e in row)

def probability(likeness, row):
	return sum(e == likeness for e in row)/len(row)

def random(words):
	return rn.choice(words)

def dec_tree(words):
	# number of words
	n = len(words)
	# possible liknesses
	m = len(words[0])+1

	# create likeness matrix
	likeness_matrix = np.zeros((n,n))
	for i in range(0,n):
		for j in range(0,n):
			likeness_matrix[i][j] = likeness(words[i],words[j])

	# create elimination matrix
	elimination_matrix = np.zeros((n,m))
	for i in range(0,n):
		row = likeness_matrix[i]
		for j in range(0,m):
			elimination_matrix[i][j] = eliminates(j,row)

	# create probability matrix
	probability_matrix = np.zeros((n,m))
	for i in range(0,n):
		row = likeness_matrix[i]
		for j in range(0,m):
			probability_matrix[i][j] = probability(j,row)

	information_vector = np.zeros(n)
	for i in range(0,n):
		a = elimination_matrix[i]
		b = probability_matrix[i]
		information_vector[i]=np.dot(a,b)

	return words[np.where(information_vector==max(information_vector))[0][0]]

def improved_dec_tree(words):
# number of words
	n = len(words)
	# possible liknesses
	m = len(words[0])+1

	# create likeness matrix
	likeness_matrix = np.zeros((n,n))
	information_vector = np.zeros(n)	
	likes = [0,1,2,3,4]
	for i in range(0,n):
		for j in range(0,n):
			likeness_matrix[i][j] = likeness(words[i],words[j])
		information_vector[i] = sum([(n-list(likeness_matrix[i]).count(e))/n for e in likeness_matrix[i]])
	return words[np.where(information_vector==max(information_vector))[0][0]]	


def naive(words):
	wordnumbers = []
	for wordi in words:
		wordnumber = 0
		for index in range(0,len(wordi)):
			for wordj in words:
				if wordj[index] == wordi[index]:
					wordnumber += 1
		wordnumbers.append(wordnumber)

	return words[wordnumbers.index(max(wordnumbers))]

def simulate(words, guesses, func):
	guess_vector = np.zeros(guesses)
	start = time.time()
	for i in range(0,guesses):
		guess = 0
		guessing = True
		correct = rn.choice(words)
		current = words
		while guessing:
			selected = func(current)
			if selected == correct:
				guessing = False
				guess += 1
			else:
				current = update(current,selected,correct)
				guess += 1
		guess_vector[i] = guess
	end = time.time()
	return (guess_vector, end-start)