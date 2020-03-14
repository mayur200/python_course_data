#concatinate word using function
def display(s):
	return s + 'd'

print(display('xyz'))
print("-----------------")

#print the square of a number

def square(sq):
	return sq*sq

print(square(5))

#print the maximum number in a list
print("-----------------")

def max_num(a,b,c):
	if a>b and a>c:
		return a
	elif b>c:
		return b
	else:
		return c

print(max_num(1,2,3))


######################################################
# print the max number form the list
print(">>>>>>>>>>>>>>>>>>>>>")

def max_lis(a):
    i=0
    maxi=0
    temp=0
    while i<= len(a)-1:
        if a[i]>maxi:
            maxi = a[i]
            print("greater is", a[i])
        else:
            temp=a[i]
            a[i] = a[i+1]
        i=i+1
    return maxi
list = [34,58,8, 70]
print("maximum number is", max_lis(list))

#factorial question

print("factorial question")


def fact_num(num):
	fact = 1
	for i in range(1,num+1):
		fact = fact*i
	return fact
print(fact_num(5))







