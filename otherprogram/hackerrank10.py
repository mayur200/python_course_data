#problem = https://www.hackerrank.com/challenges/python-mod-divmod/problem

dividend = int(input())
divisor = int(input())
if divisor != 0 :
    sep = divmod(dividend,divisor)
    print(sep[0])
    print(sep[1])
    print(sep)
else:
    raise Exception("please enter positive")
    
