def NOD(a,b):
	r = a % b
	while r != 0:
		a = b
		b = r
		r = a % b
	return b
	
a = int(input())
b = int(input())
print(NOD(a,b))
