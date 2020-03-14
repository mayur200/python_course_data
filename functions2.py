#count the number of character in the given list of word


def max_string(string_list):
	print(string_list)
	i=0
	maxi=0
	temp=0
	while i < len(string_list):
		print(len(string_list[i]))
		if len(string_list[i])>maxi:
			maxi = len(string_list[i])
			larg = string_list[i]
			print("maximum number is",string_list[i])
		else:
			break;
		i = i+1
	return larg
li = ['abc', 'defc', 'ghoooo']
print("maximum character is", max_string(li))