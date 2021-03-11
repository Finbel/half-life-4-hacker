import functions as fun
import numpy as np
from scipy import stats 
from tabulate import tabulate as tab

f = open("input.txt")
words = f.readlines()
words2 = [word[:-1] for word in words[:-1]]
words = words2 + words[-1:]

functions = [fun.naive, fun.improved_dec_tree, fun.random]
names = {functions[0]:"naive",fun.improved_dec_tree:"improved_dec_tree",fun.random:"random"}

guess_matrix = []
for func in functions:
	guesses, time = fun.simulate(words, 100000,func)
	guess_matrix.append(guesses)
print(len(guess_matrix))

p_matrix = []
for i in range(0,len(functions)):
	row = []
	row.append(names[functions[i]])
	for j in range(0,len(functions)):
		s, p = stats.ttest_ind(guess_matrix[i],guess_matrix[j])
		row.append(p)
	p_matrix.append(row)

head = ['functions']+[names[f] for f in functions]
tabular_guesses = []
for i in range(0,len(functions)):
	row = []
	row.append(names[functions[i]])
	row.append(str(np.mean(guess_matrix[i])))
	tabular_guesses.append(row)

tabular_guesses_max = []
for i in range(0,len(functions)):
	row = []
	row.append(names[functions[i]])
	row.append(str(np.amax(guess_matrix[i])))
	tabular_guesses_max.append(row)
print()
print("Max antal gissningar:")
print()
print(tab(tabular_guesses_max, headers=['functions','max number of guesses']))
print()
print("gissningar:")
print()
print(tab(tabular_guesses, headers=['functions','mean number of guesses']))
print()
print("p-värden till Andreas:")
print()
print(tab(p_matrix,headers=head))
print()
print()

