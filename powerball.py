import random
list = []
for x in range(1,11):
    for b in range(1,7):
        n = random.randrange(1,61)
        list.append(n)
        if b < 6:
            print (n, " ", end = '')
        else:
            print (n)
for a in range(1,61):
    if list.count(a) != 0:
        print(a, "appears", list.count(a), "times!")
print (len(list))
