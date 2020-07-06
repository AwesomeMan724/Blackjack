import random
list = []
countlist = []
sets = 11
numbers = 61

for a in range (1,numbers):
    countlist.append(0)
    
for x in range(1,sets):
    count = 0
    numlist = []
    while count < 6:
        n = random.randrange(1,numbers)
        if n not in numlist:
            list.append(n)
            numlist.append(n)
            countlist[n - 1] += 1
            
            if count < 5 :
                print (n, "", end = '')
            else:
                print (n)
                
            count += 1

    
            
for c in range (1, numbers):
    if countlist[c-1] != 0:
        print (c, "appears", countlist[c-1], "times!")
        
print(len(list))

