# https://www.hackerrank.com/challenges/collections-counter/problem
# collections.Counter()

from collections import Counter
x = int(input())
lst_shoe_no = list(map(int,input().split()))

if len(lst_shoe_no)<(x+1):
    dict_shoe = Counter(lst_shoe_no)
    no_cst = int(input())
    i = 0
    shoe_price = []
    while i < no_cst:
        shoe_no, price = map(int,input().split())
        if shoe_no in dict_shoe:
            dict_shoe[shoe_no] =  dict_shoe[shoe_no] -1
            if dict_shoe[shoe_no] > -1:
                shoe_price.append(price)
        i = i+1
    # print(dict_shoe)
    # print(shoe_price)
    print(sum(shoe_price))
else:
    raise Exception("Please input UPPER CASE character")

