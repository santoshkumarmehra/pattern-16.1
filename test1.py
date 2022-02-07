n=int(input("enter no = "))
t=1
for i in range(n,0,-1):
	x=t
	for j in range(1,i+1):
		if (i==n or j==1):
			print(x,end=" ")
			x=x+1
		elif j==i:
			print(n,end="")
		else:
			print(" "*(2),end="")
	t=t+1
	print()