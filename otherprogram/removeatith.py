test_str = "GeeksForGeeks"
sent = ''
for word in range(0, len(test_str)):
	if word == 3:
		continue
	sent= sent+test_str[word]
print(sent)



