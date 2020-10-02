# Problem : https://www.hackerrank.com/challenges/swap-case/problem


import re 
regexp = re.compile('[^a-zA-Z]+')
def swap_case(s):
    if len(s) < 1001:
        newstring = ''
        for a in s:
            if a.isupper() == True:
                newstring+=a.lower()
            if a.islower() == True:
                newstring += a.upper()
            if regexp.search(a):
                newstring += a
                
    else:
        raise Exception("Charater length should be less than 100")
    return newstring



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)