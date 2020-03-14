'''
Print selected Month from the given number
'''

year = {1:'Jan', 2:'Feb', 3:'March', 4:'Apr', 5:'May', 6:'June', 7:'July', 8:'Aug', 9:'sep', 10:'Oct', 11:'Nov', 12:'Dec'}
print(year[2])


num = 1
months = ('Jan','Feb','March')
print(months[num-1])

'''
Print all the square from the given list 
'''

li_square=[]
li = [1,2,3,4,5]
for num in li:
	square = num*num
	li_square.append(square)
print(li_square)

