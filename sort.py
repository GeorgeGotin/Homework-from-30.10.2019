n = int(input())
a = []
for i in range(n):
	a.append(int(input()))
for i in range(n):
	for j in range(i,n-i-1):
		if a[j] < a[i]:
			a[j] = a[j] + a[i]
			a[i] = a[j] - a[i]
			a[j] = a[j] - a[i]
		elif a[j] > a[n-1-i]:
			a[j] = a[j] + a[n-i-1]
			a[n-i-1] = a[j] - a[n-i-1]
			a[j] = a[j] - a[n-i-1]
print(a)
