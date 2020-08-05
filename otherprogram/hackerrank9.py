#Problem = https://www.hackerrank.com/challenges/py-set-add/problem
#Depends on set

tot_country = int(input())

distinct_country = set()
if tot_country > -1 and tot_country < 1001:
    for stamp in range(0,tot_country):
        country = input()
        distinct_country.add(country)
    print(len(distinct_country))

        
else:
    raise Exception("numbers should be between 0 to 1000")
