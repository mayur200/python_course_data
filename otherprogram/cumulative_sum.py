li = [10,20,30,40,50]
cum=[]
ans = 0
for num in range(0,5):
	ans = li[num]+ans
	cum.append(ans)
print(cum)


a="what is python"
b=a.split()
b.reverse()
c=" ".join(b)
print(c)
