#problem = https://www.hackerrank.com/challenges/python-power-mod-power/problem

a= int(input())
b= int(input())
c = int(input())

if a> 0 and a < 11 and b>0 and a<11 and c>1 and c<1001 :
    print(pow(a,b))
    print(pow(a,b,c))
else:
    raise Exception("Sorry number should be between 0 to 1000")