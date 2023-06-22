#problem =https://www.hackerrank.com/challenges/python-tuples/problem
#Tuples and hash()

if __name__ == '__main__':
    n = int(input())
    integer_map = map(int, input().split()) 
    integer_list = list(integer_map)
    if len(integer_list) < (n+1):
        print(hash(tuple(integer_list)))
    else:
        raise Exception("Sorry, no numbers greater than:", n)
