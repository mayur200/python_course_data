#question = https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())

n_l = input()
lst = n_l.split()
if len(lst)>n or len(lst)<n :
    raise Exception("Sorry, no numbers below "+str(n)+" and above "+str(n))
num_lst = []
for num in lst:
    if num != " ":
        num_lst.append(int(num))
sort_ed = sorted(set(num_lst))
# print("sorted", sort_ed)
print(sort_ed[-2])