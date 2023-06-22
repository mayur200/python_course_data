# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# itertools.combinations_with_replacement()

from itertools import combinations_with_replacement

word, num = map(str,input().split())
lexi = list(combinations_with_replacement(word,int(num)))
sorted_lexi = []
for tup in lexi:
    full_sort = sorted(tup)
    np = ""
    wordi = np.join(full_sort)
    sorted_lexi.append(wordi)
sort_lst = sorted(sorted_lexi)
for srt in sort_lst:
    print(srt)
    


