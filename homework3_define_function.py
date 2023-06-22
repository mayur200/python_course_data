#return true if  list of one number is found in second list

def duplicate_number(list1,list2):
	for num in list1:
		if num in list2:
			return True
		else:
			return False

li1 = [1,2,3,4,5]
li2 = [0,6,7,8,9]
print(duplicate_number(li1,li2))


#write a function find_longest_word() that takes a list of words and returns the longest word

def find_longest_word(words):
	maxi=0
	word = 0
	pos = 0
	while word<len(words):
		if len(words[word])> maxi:
			maxi = len(words[word])
			pos = word
		word = word+1
	return words[pos]

li = ['best','powerful', 'ShivajiMaharaj']
print("the largest word in list is",find_longest_word(li))






