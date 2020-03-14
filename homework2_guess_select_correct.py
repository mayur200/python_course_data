'''
If the guess number by user is correct then print "Your guess is correct" if the the ans is less than the actual number
 then "Your guess was less than the answer" or if ans is greater than the guess then print "Your guess was greater than the answer"
 do this until user give correct answer
 '''

a=0
right=20
while a!=right:
    a=int(input("Guess the number: "))
    if a < right:
        print("Your guess was less than the answer")
    elif a > right:
        print("Your guess was greater than the answer")
if a == right:
	print("Your guess is correct")
