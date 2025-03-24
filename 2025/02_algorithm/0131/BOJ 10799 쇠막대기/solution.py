data = input()
stack = []
acc = 0
ans = 0
for i in range(len(data)):
	ele = data[i]
	if ele =='(':
		stack.append(ele)
	else :
		stack.pop()
		if i!=0 and data[i-1]=='(':
			ans += len(stack)
		else : ans += 1
print(ans)