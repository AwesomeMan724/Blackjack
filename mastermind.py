import random
tries = 10
trycount = 0
diglist = []
infolist = []

# Generate random code (4-digit) number
for a in range(1, 5):
    dig = str(random.randrange(1, 7))
    diglist.append(dig)
n = ''.join(diglist)
#print(n)

while trycount < tries:
    try:
        digmax = True
        list = [0, 0, 0, 0]
        list2 = [0, 0, 0, 0]
        num = input("Enter a 4 digit number:")
        maxreached = False
        outrange = False

        for t in range(0, 4):
            if int(num) not in range(1000, 10000):
                outrange = True
                digmax = False
        if outrange:
            print(num, end="")
            print("\nI said a 4 digit number!")
            maxreached = False
        if digmax:
            for k in range(0, 4):
                if int(num[k]) > 6 or int(num[k]) <= 0:
                    maxreached = True
                    digmax = False
        if maxreached:
            print(num, end="")
            print("\nSorry, each digit can only be from 1 to 6!")

        while digmax:
            if num == n:
                print(num, end="")
                print("\nYou Won!")
                print("You won in", trycount+1, "tries!")
                trycount = 10
                break
            else:
                corplace = 0
                wroplace = 0
                for z in range(0, 4):
                    if num[z] == n[z]:
                        corplace += 1
                        list[z] += 1
                        list2[z] += 1
                for x in range(0, 4):
                    for y in range(0, 4):
                        if num[x] == n[y] and list[y] == 0 and list2[x] == 0:
                            wroplace += 1
                            list[y] += 1
                            list2[x] += 1
                    if x == 3:
                        data = num + "     " + str(corplace) + "     " + str(wroplace)
                        infolist.append(data)
                        c = 0
                        for b in range(0, trycount):
                            print(infolist[c])
                            c += 1
                        print(num, end="")
                        print("    ", corplace, "    ", end="")
                        print(wroplace)
                        if trycount == tries - 1:
                            print("\nYou Lose!")
                            print(n)
                        else:
                            print("\nYou have", tries - 1 - trycount, "tries remaining")
                            print("\nTry Again")
                trycount += 1
            digmax = False
    except:
        print("\nI said a 4 digit number!")