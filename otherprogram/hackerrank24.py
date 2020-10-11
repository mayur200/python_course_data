#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Collections.OrderedDict()

from collections import OrderedDict

items = int(input())
total_list = OrderedDict()
# for item in range(0,items):
for item in range(0,items):
    lst_item = list(input().split())
    item_name_lst = lst_item[0:-1]               #select all item in list expecct last item
    item_name = " ".join(item_name_lst)          #Convert the list in string
    net_price = lst_item[-1]
    if item_name in total_list:
        total_list[item_name] = total_list[item_name] + int(net_price)
    else:
        total_list[item_name] = int(net_price)
for food in total_list:
    print(food, total_list[food])




