#qauestion = https://www.hackerrank.com/challenges/write-a-function/problem



def is_leap(year):
    leap = False
    
    if year%4 == 0  :
        if year%100 == 0:
            if year%400 != 0:
                return leap
        
            else:
                return True
        else:
            return True
        
        

            
    else:
        return leap
year = int(input())