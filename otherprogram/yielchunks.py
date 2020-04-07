#Break a list into chunks of size N in Python
#https://www.geeksforgeeks.org/break-list-chunks-size-n-python/



my_list = ['geeks', 'for', 'geeks', 'like', 
           'geeky','nerdy', 'geek', 'love', 
               'questions','words', 'life','life','saer']
num_li = len(my_list)/5 
num_li =int(num_li)+1

print(">>>>>>>>>>>>>",num_li)
board = []   
for li in range(0,3):
    board.append([])
    
s = 0
e = 5
for li in range(len(board)):
    if s < 6 and e < 12:
        print(s,"---------",e)
        for n in range(s,e):
            start = s 
            end = e
            board[li].append(my_list[n])
    s = s +5
    e = e +5

for li in range(len(board)):
    for n in range(end, len(my_list)):
        print("ppppp",len(my_list))
        if len(board[li]) != 5:
            print("under li",li)
            board[li].append(my_list[n])
            



print(board)
        
    

