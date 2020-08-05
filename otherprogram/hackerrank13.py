#problem:https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem


a= int(input())
b= int(input())
c = int(input())
d = int(input())

if a> 0 and a < 1001 and b>0 and a<1001 and c>0 and c<1001 and d>0 and d<1001 :
    ans = pow(a,b) + pow(c,d)
    print(ans)
else:
    raise Exception("Sorry number should be between 0 to 1000")