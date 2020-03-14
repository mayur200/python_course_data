#print the multiplication number

table = 1
ans = 1
while table < 26:
	multi=1
	while multi < 11:
		ans= table*multi
		print(str(table) +"*" +str(multi) +"=" +str(ans))
		multi = multi+1
	table = table+1
	if table != 26:
		print("<<<table for:" +str(table) +">>>>>")
		 # print( +table +"*" +multi +"=" +ans )
val = input("Enter your value: ") 
print(val)

