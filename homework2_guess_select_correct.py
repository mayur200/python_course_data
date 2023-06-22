'''
If the guess number by user is correct then print "Your guess is correct" if the the ans is less than the actual number
 then "Your guess was less than the answer" or if ans is greater than the guess then print "Your guess was greater than the answer"
 do this until user give correct answer
 '''

num=0
correct_number=20
while num!=correct_number:
    num=int(input("Guess the number: "))
    if num < correct_number:
        print("Your guess was less than the answer")
    elif num > correct_number:
        print("Your guess was greater than the answer")
if num == correct_number:
    print("Your guess is correct")
