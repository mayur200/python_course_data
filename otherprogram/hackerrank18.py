#https://www.hackerrank.com/challenges/designer-door-mat/problem
#designer-door-mat problem


row, col = input().split()
col = int(col)
row = int(row)
if row > 5 and row < 101 and col > 15 and col < 303:
    inc = 3
    half =  row/2
    middle = int(half) +1
    i = 0
    x = (col-inc)/2
    y = inc
    xx = 3
    yy = col- 3
    wlm_strt = (col-7)/2
    wlm_end = wlm_strt + 7
    wlm = "WELCOME"
    wel_lst =[]
    for rw in range(1,(row+1)):
        lst =[]
        lwr =[]
        for cm in range(1,(col+1)):
            # ---------.|.---------
            # ------.|..|..|.------
            # ---.|..|..|..|..|.---
            if rw < middle:                 
                if cm < x+1:
                    print("-", end="")                                        
                if cm > x and cm < (x+y)+1:                      
                    if len(lst) < 1 or len(lst) >2:                             
                        lst = []
                        lst.append('.')
                        print(".", end="")
                    elif len(lst) == 1:
                        lst.append('|')
                        print("|", end="")
                    else:
                        lst.append('.')
                        print(".",end="")
                if cm > x+y:                                    
                    print("-", end="")
            # -------WELCOME-------
            elif rw == middle:                                  
                if cm < (wlm_strt+1):
                    print("-", end="")
                elif cm > wlm_strt and cm < (wlm_end+1):
                    if "WELCOME" in wel_lst:
                        pass
                    else:
                        wel_lst.append("WELCOME")
                        print("WELCOME", end="")
                else:
                    print("-", end="")
            # ---.|..|..|..|..|.---
            # ------.|..|..|.------
            # ---------.|.---------   
            else:
                if cm < xx+1:
                    print("-", end="")
                    # print(cm,">",xx+3)
                if cm > xx-1 and cm < yy:
                    if len(lwr) < 1 or len(lwr) >2:
                        lwr = []
                        lwr.append('.')
                        print(".", end="")
                    elif len(lwr) == 1:
                        lwr.append('|')
                        print("|", end="")
                    else:
                        lwr.append('.')
                        print(".",end="")
                if cm > yy:
                    print("-", end="")
        #usefull when jumping to next row            
        x = x-3
        y =  col-(x*2)
        if rw > middle:
            xx = xx+3
            yy = col-xx
    
        print("")
else:
    raise Exception("Sorry number is not in range")
