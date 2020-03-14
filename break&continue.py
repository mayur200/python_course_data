#break the loop

li = [1,2,3,-1,4,5]
for elem in li:
	if elem == -1:
		break
	else:
		print(elem)

#continue the loop>>>>>>>>>>

print("continue the loop>>>>>>>>>>")
lis = [1,2,3,-1,4,5]
for elem in lis:
	if elem == -1:
		continue
	else:
		print(elem)

