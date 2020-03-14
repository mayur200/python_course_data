
#return the list of words which is longer than the given number
def filter_long_words(li_word,num):
	long_word=[]
	for word in li_word:
		if len(word)>4:
			long_word.append(word)
	return long_word


li=['abc','mayurpardeshi','rashaastar','kari']
num=4
print(filter_long_words(li,num))

print(">>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
#check if the give senetence has all 26 alphabets or not
def panagram_or_not(capob):
	count=0
	atoz = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for item in atoz:
		if item not in capob:
			return "Is not a panagram"
	return "It is not a panagram"
capob = 'qwertyuiopasdfghjklzxcvbn m'
print(panagram_or_not(capob))																								
 