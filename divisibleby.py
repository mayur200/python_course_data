# Check if the given number is divisible by 5 / divisible by 3 / divisible by both/not divisible by both

a = 5
if a%3 == 0 and a%5 ==0:
	print("divisible by both")
elif a%5 == 0:
	print("divisible 5")
elif a%3 == 0:
	print("divisble by 3")
else:
	print("not divisble by both")


#Print only odd element from list of given integers

li= [1,2,3,4,5,6,7,8]

for no in li:
	if no%2 != 0:
		print(no)

#count number or string without using len function
number = 0
char = "Mayur   Pardeshi"
li = list(char)
for char in li:
	if char != ' ':
		number = number + 1
print(number)

#print only those charcter whose element start with vowel or not
li = ['abc','python', 'eclare']
for no in li:
	if no[0] == 'a' or no[0] == 'e' or no[0] == 'i' or no[0] == 'u':
		print(no)
print("----------")
for x in li:
	if x[0] in ['a', 'e', 'o', 'u']:
		print(x)


