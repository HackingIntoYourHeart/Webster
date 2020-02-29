import sys
import os
import os.path
from os import path
from itertools import permutations

def array2String(array):
	string = "" 
	return (string.join(array)) 

def reverse(string): 
	str = "" 
	for i in string: 
		str = i + str
	return str
	
def isFile(path):
	if os.path.isdir(path):
		return False
	elif os.path.isfile(path):
		return True
	else:
		return 3

endl = "\n"
terms = []

if len(sys.argv) > 1:
	termList = sys.argv[1]
	if isFile(termList) and path.exists(termList):
		with open(termList) as readFileLines:
			for line in readFileLines:
				terms.append(line.strip().lower())
	else:
		print("File not found.\n")
		exit()

else:
	while(True):
		term = raw_input("Term: ")
		if term == "":
			break
		else:
			terms.append(term)

reverseWord = True;
caps=True
fcaps=True
ecaps=True

min_len = input("Minimum password length: ")
max_len = input("Maximum password length: ")
permutation_len = input("Permutation length: ")

# Permute terms
output = raw_input("Name of output file: ")
output = open(output, 'a')

word = ""
word1 = ""
word2 = ""
word3 = ""
word4 = ""
word5 = ""
word6 = ""

for t in range(permutation_len + 1):
	perm = list(permutations(terms, t))
	for i in perm:
		if len(array2String(i)) < max_len and len(array2String(i)) > min_len:
			word = array2String(i)
			#print word

			if reverseWord == True:
				word1 = reverse(word)

			if word[0].isalpha():
				
				if fcaps == True:
					word2 = (word[0].swapcase() + word[1:])
					#print word2
				
				if reverseWord == True:
					word3 = reverse(word2)
					#print word3
				
				if ecaps == True:
					word4 = (word[0] + word[1:].swapcase())
					#print word4
				
				if reverseWord == True:
					word5 = reverse(word4)
					#print word5

			if caps == True:
				word6 = word.swapcase()
				#print word6

			if word != "":
				output.writelines(word + endl)
				print(word)
			if word1 != "":
				output.writelines(word1 + endl)
				print(word1)
			if word2 != "":
				output.writelines(word2 + endl)
				print(word2)
			if word3 != "":
				output.writelines(word3 + endl)
				print(word3)
			if word4 != "":
				output.writelines(word4 + endl)
				print(word4)
			if word5 != "":
				output.writelines(word5 + endl)
				print(word5)
			if word6 != "":
				output.writelines(word6 + endl)
				print(word6)

output.close()
	
	
	
