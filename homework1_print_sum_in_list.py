#print the sum of list such that x[23,34,567] ans should be x[2+3+3+4+5+6+7]

x = [12,23, 12]
ls = []
for l in x:
	i=l
	while i>0:
		digit=i%10
		i=i/10
		ls.append(int(digit))
print("sum",sum(ls))
