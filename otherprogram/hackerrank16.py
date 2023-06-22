#Problem = https://www.hackerrank.com/challenges/text-wrap/problem
#Text Wrap problem

import textwrap

'''--------------------------------------Method 1 =  Without using textwrap------------------------------------'''
sent = input()
num = int(input())
if len(sent) > 0 and len(sent) < 1000:
    if num > 0 and num < len(sent):
        i = 0	
        li = []
        while  i < len(sent):
            li.append(sent[i])
            i = i+1
            if i%num == 0:
                ans = ''.join(map(str, li)) 
                print(ans)
                li = []
        rem = len(sent)%3
        if rem !=0:
            print(sent[-rem:])
    else:
     raise Exception("Sorry, letter should between 0 and len(sent)")
else:
     raise Exception("Sorry, number should between 0 to 1000")


'''--------------------------------------Method 2 = Using textwrap function------------------------------------'''

def wrap(string, max_width):
    if len(string) > 0 and len(string) < 1000:
        if max_width > 0 and max_width < len(string):
            ans= textwrap.fill(string,max_width)
        else:
            raise Exception("Sorry, letter should between 0 and max_width")
    else:
        raise Exception("Sorry, number should between 0 to 1000")

    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

        