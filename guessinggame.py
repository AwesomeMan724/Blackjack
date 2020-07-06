import random
endrange = 100
tries = 5
n = random.randrange(1,endrange+1)
count = 0
while count < tries:
    print("Enter a whole number from 1 to", endrange, ":")
    strusernumber = input()
    try:
        usernumber = int(strusernumber)
        if usernumber in range(1, endrange + 1):
            if usernumber == n:
                print("You Won!")
                break
            else:
                if usernumber < n:
                    print("Try Again (Higher)")
                    count += 1
                    if count == tries:
                        print("You Lose!")
                else:
                    print("Try Again (Lower)")
                    count += 1
                    if count == tries:
                        print("You Lose!")
        else:
            print("I said a whole number from 1 to", endrange, ", you dumbbutt!")
    except:
        print("I said a whole number from 1 to", endrange, ", you dumbbutt!")
print("The correct number was", n)