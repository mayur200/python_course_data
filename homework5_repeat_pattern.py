''''
if patter A = "abba" and B = "dog cat cat dog"
return True
if patter A = "abba" and B = "dog cat cat cat"
return False
if patter A = "abba" and B = "cat cat cat cat"
return False
'''



join_dict={}
words = 'abba'
count=0
for cahr in words:
	if cahr not in join_dict:
		count=count+1
		ke_y = cahr
		print("ke_y",ke_y)
		join_dict[ke_y] = count
print("ans is",join_dict, type(join_dict))
pattern1=[]
for wrd in words:
	if wrd in join_dict:
		pattern1.append(join_dict[wrd])
print(pattern1)
dict_join={}
senti = "dog cat cat dog"
senti1= senti.split(' ')
valuee = 0
print(type(dict_join))
for word in senti1:
	if word not in dict_join:
		valuee = valuee+1
		print("word",word)
		kee = word
		print("kee",kee)
		dict_join[kee] = valuee
print("my ans is", dict(dict_join), type(dict_join))
pattern2=[]
for wrd in senti1:
	if wrd in dict_join:
		# print(dict_join[wrd])
		pattern2.append(dict_join[wrd])
print(pattern2)

if pattern1 == pattern2:
	print("check>>>>>",True)
else:
	print("false>>>>", False)


