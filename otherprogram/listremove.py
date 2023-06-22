li = [12,10,23,20]
remove = [12,10]
for num in remove:
	li.remove(num)
print('remove number from list', li)


#print duplicate element in a list without using any python function
dp_li=[]
incr=0
counti=0
li=[34,34,34,8,45,45,4,80,4,80]
for num in li:
    dupli=num
    while len(li)>incr:
        if dupli==li[incr]:
            counti = counti +1
            incr=incr+1
            if counti>1:
                if num not in dp_li:
                	dp_li.append(num)
        else:
            incr=incr+1
    incr=0
    counti=0

print("duplicate list is>>>", dp_li)