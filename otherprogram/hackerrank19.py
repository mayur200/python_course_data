# https://www.hackerrank.com/challenges/itertools-permutations/problem
# itertools.permutations()


from itertools import permutations

char, sep = input().split()
order_list = []
if char.isupper():
    if int(sep) > 0 and int(sep) < (len(char)+1):
        lst = permutations(char,int(sep))
        for pair in lst:
            order_list.append(pair)
        order_list.sort()
        for sop in order_list:
            for word in sop:
                print(word, end="")
            print("")
    else:
        raise Exception("sep should be 0<sep<=char")
        
else:
    raise Exception("Please input UPPER CASE character")
