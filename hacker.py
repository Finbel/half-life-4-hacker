import functions as fun

f = open("input.txt")
words = f.readlines()
words2 = [word[:-1] for word in words[:-1]]
words = words2 + words[-1:]
l=0
length = len(words)
while l!=-1:
	selected = fun.improved_dec_tree(words)
	print(selected + " " + str("1/"+str(len(words))))
	length = len(words)
	l = int(input("likeness? "))
	words = fun.game_update(words,selected,l)
	if(len(words)==0):
		l=-1
	print()
print("game over")