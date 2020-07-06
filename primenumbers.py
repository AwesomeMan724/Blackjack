begin = 3
end = 101
print("2")
for a in range(begin,end):
	isPrime = True
	for z in range(2,int(a**1/2)):
		if a % z == 0:
			isPrime = False
			break
	if isPrime:
		print(a)
