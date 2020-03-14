#Using while loop print number till 10
count = 0
while count < 11:
	print(count)
	count = count +1

print("--------------")

#print the sum of element in a list using while loop
li = [10,25,5]
num = 0
count = 0
x = 0

while count < (len(li)):
	num = li[x] + num
	x = x +1
	count = count+1
print(num)



