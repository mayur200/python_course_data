# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# collections.namedtuple()


from collections import namedtuple

x = int(input())
header = list(input().split())
Timesheet = namedtuple('Timesheet', header)
marks = []
for num in range(0, x):
    val1, val2, val3, val4 = input().split()
    xyz = Timesheet(val1, val2, val3, val4)
    marks.append(int(xyz.MARKS))

avg= sum(marks)/x
print(avg)