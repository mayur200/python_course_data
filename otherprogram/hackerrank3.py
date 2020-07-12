'''question = https://www.hackerrank.com/challenges/nested-list/problem'''

number_of_nested_lists = int(input())
i = 0
data = []
al_lst = []
sort = []
while(i < number_of_nested_lists):
    while len(data) < 2:
        name = input()
        marks = float(input())
        data.append(name)
        data.append(marks)
        sort.append(marks)
        print(data)
    print("out_of_if")
    al_lst.append(data)
    data = []
    i = i + 1
print("al_lst",al_lst)
all_marks = [i[1] for i in al_lst]
sort_marl = sorted(set(sort))
larg_2nd = sort_marl[1]
abt = []
for s in al_lst:
    if s[1] == larg_2nd:
        print("second largest",s[0])
        abt.append(s[0])
tpl = sorted(set(abt))
for w in tpl:
    print(w)
