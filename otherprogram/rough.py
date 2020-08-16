# 
most = ['John', 'is', 'the', 'son', 'of', 'John',
        'second', 'Second', 'son', 'of', 'John',
        'second', 'is', 'William', 'second']


def to_upper_case(s):
    return str(s).lower()


map_iterator = list(map(to_upper_case, most))

uniq = {}
for word in map_iterator:
	if word not in uniq:
		n=0
		for each in map_iterator:
			if word == each:
				n = n+1
		uniq[word]=n
        

Keymax = max(uniq, key=uniq.get)
print("max value>>>>>>>>",Keymax)

