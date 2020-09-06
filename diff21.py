def diff21(n):
	if n <= 21:
		return 21-n
	else:
		return (n-21)*2

numbers = [19,10,21,22,25,30,0,1,2,-1,-2,50]

for n in numbers:
	num = diff21(n)
	print(num)