import os
import random

os.chdir("C:/Users/kevin/PythonPrograms/Files")
f = open("BlackJackCards.txt", "r")
all_lines = f.readlines()
r = open("BlackJackMoney.txt", "r")
money_lines = r.readlines()
print("Your Total Money:", money_lines[-1])
a = open("BlackJackMoney.txt", "a")

# Bet
validBet = False
while validBet == False:
    try:
        userBet = input("How much money will you bet (minimum $10): ")
        if int(userBet) in range(10, int(money_lines[-1])+1):
            print("hello")
            validBet = True
        else:
            print("Sorry, that's not an amount you can bet")
    except:
        print("Sorry, that's not an amount you can bet")
# Lists
seen = []
dealerHand = []
playerHand = []
dealerCardValueList = []
playerCardValueList = []


# Deal New Card for the Dealer
def DealerCardDeal():

    generated = False
    while generated == False:
        # Generate Card Number
        randCardNum = random.randrange(14)
        cardNum = all_lines[randCardNum].strip()

        # Generate Card Suit
        randSuitNum = random.randrange(15, 19)
        cardSuit = all_lines[randSuitNum].strip()

        # Join into a single card
        card = cardNum + cardSuit
        if card not in seen:
            dealerHand.append(card)
            generated = True
            seen.append(card)

    # Calculate Card Value
    if cardNum == "J" or cardNum == "Q" or cardNum == "K":
        dealerCardValueList.append(10)
    elif cardNum.isnumeric():
        if int(cardNum) in range(1, 11):
            dealerCardValueList.append(int(cardNum))
    if cardNum == "A" and sum(dealerCardValueList) + 11 <= 21:
        dealerCardValueList.append(11)
    elif cardNum == "A" and sum(dealerCardValueList) + 11 > 21:
        dealerCardValueList.append(1)

    # Card Total
    global dealerCardTotal
    dealerCardTotal = sum(dealerCardValueList)


# Deal New Card for the Player
def PlayerCardDeal():

    generated = False
    while generated == False:
        # Generate Card Number
        randCardNum = random.randrange(14)
        cardNum = all_lines[randCardNum].strip()

        # Generate Card Suit
        randSuitNum = random.randrange(15, 19)
        cardSuit = all_lines[randSuitNum].strip()

        # Join into a single card
        card = cardNum + cardSuit
        if card not in seen:
            playerHand.append(card)
            generated = True
            seen.append(card)

    # Calculate Card Value
    if cardNum == "J" or cardNum == "Q" or cardNum == "K":
        playerCardValueList.append(10)
    elif cardNum.isnumeric():
        if int(cardNum) in range(1, 11):
            playerCardValueList.append(int(cardNum))
    if cardNum == "A" and sum(playerCardValueList) + 11 <= 21:
        playerCardValueList.append(11)
    elif cardNum == "A" and sum(playerCardValueList) + 11 > 21:
        playerCardValueList.append(1)

    # Card Total
    global playerCardTotal
    playerCardTotal = sum(playerCardValueList)

# Deal New Set of Cards for the Player if Split
def PlayerCardDealSplit():

    generated = False
    while generated == False:
        # Generate Card Number
        randCardNum = random.randrange(14)
        cardNum = all_lines[randCardNum].strip()

        # Generate Card Suit
        randSuitNum = random.randrange(15, 19)
        cardSuit = all_lines[randSuitNum].strip()

        # Join into a single card
        card = cardNum + cardSuit
        if card not in seen:
            playerHand2.append(card)
            generated = True
            seen.append(card)

    # Calculate Card Value
    if cardNum == "J" or cardNum == "Q" or cardNum == "K":
        playerCardValueList2.append(10)
    elif cardNum.isnumeric():
        if int(cardNum) in range(1, 11):
            playerCardValueList2.append(int(cardNum))
    if cardNum == "A" and sum(playerCardValueList2) + 11 <= 21:
        playerCardValueList2.append(11)
    elif cardNum == "A" and sum(playerCardValueList2) + 11 > 21:
        playerCardValueList2.append(1)

    # Card Total
    global playerCardTotal2
    playerCardTotal2 = sum(playerCardValueList2)


# Function for Dealer's Hand
def DealerHand():
    print("The Dealer's Hand: ", end="")
    for a in range(len(dealerHand)):
        if a < len(dealerHand) - 1:
            print("{}, ".format(dealerHand[a]), end="")
        elif a == len(dealerHand) - 1:
            print(dealerHand[a], end="")
    print("    (Total is {})".format(dealerCardTotal))


# Function for Player's Hand
def PlayerHand():
    print("Your Hand: ", end="")
    for a in range(len(playerHand)):
        if a < len(playerHand) - 1:
            print("{}, ".format(playerHand[a]), end="")
        elif a == len(playerHand) - 1:
            print(playerHand[a], end="")
    print("    (Total is {})".format(playerCardTotal))


# Function for Player's Hand if Split
def PlayerHandSplit():
    print("Your Hand: ", end="")
    for a in range(len(playerHand2)):
        if a < len(playerHand2) - 1:
            print("{}, ".format(playerHand2[a]), end="")
        elif a == len(playerHand2) - 1:
            print(playerHand2[a], end="")
    print("    (Total is {})".format(playerCardTotal2))

# Print Player's Hand
PlayerCardDeal()
PlayerCardDeal()
PlayerHand()


# Print Dealer's Hand
DealerCardDeal()
DealerCardDeal()
DealerHand()


# Count Number of Turns
count = 0


# Split and Stand Checker
split = False
stand = False
stand2 = False

# Lose Checker
lost = False
splitlose = 0

# Win Checker
win = False

# Valid Input Checker
valid = False
while valid == False:
    # If the player can split
    if str(playerHand[0])[0] == str(playerHand[1])[0] and split == False and int(money_lines[-1]) >= int(userBet)*2:
        userChoice = input("Do you wish to [H]it, [St]and, or [Sp]lit: ")

        # Split
        if userChoice.lower() == "split" or userChoice.lower() == "sp":
            playerHand2 = []
            playerCardValueList2 = []
            playerHand2.append(playerHand[0])
            playerHand.remove(playerHand[0])
            # Increase Count
            count += 1
            # Change Split Value
            split = True
            # Change Valid Value
            valid = True
            # Subtract Money
            a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))

        # Hit
        elif userChoice.lower() == "hit" or userChoice.lower() == "h":

            # Print Player's Hand
            PlayerCardDeal()
            PlayerHand()
            # Increase Count
            count += 1
            # Change Valid Value
            valid = True

        # Stand
        elif userChoice.lower() == "stand" or userChoice.lower() == "st":
            # Increase Count
            PlayerHand()
            count += 1
            # Change Valid Value
            valid = True

        # Check
        else:
            print("Sorry, that's not an option")


    # If the player has split
    if split == True:

        # Deal New Cards
        PlayerCardDeal()
        PlayerCardDealSplit()

        # First  Hand
        while stand == False:
            PlayerHand()
            # Bust
            if playerCardTotal > 21:
                print("You Lost This Hand!")
                lost = True
                splitlose += 1
                # Subtract Money
                a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
                break

            # Blackjack
            if (playerHand[0][0] == "A" and playerCardValueList[1] == 10) or (playerHand[1][0] == "A" and playerCardValueList[0] == 10):
                print("You Won This Hand!")
                # Add Money
                a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))
                win = True
                stand = True
                break

            # Hit or Stand
            userChoice = input("(1) Do you wish to [H]it or [St]and: ")

            # Hit
            if userChoice.lower() == "hit" or userChoice.lower() == "h":

                # Print Player's Hand
                PlayerCardDeal()
                PlayerHand()
                # Change Valid Value
                valid = True

            # Stand
            elif userChoice.lower() == "stand" or userChoice.lower() == "st":
                PlayerHand()
                stand = True
                # Change Valid Value
                valid = True

            # Check
            else:
                print("Sorry, that's not an option")


        # Second Hand
        while stand2 == False:
            PlayerHandSplit()
            # Bust
            if playerCardTotal2 > 21:
                print("You Lost This Hand!")
                splitlose += 1
                lost = True
                # Subtract Money
                a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
                break

            # Blackjack
            if (playerHand[0][0] == "A" and playerCardValueList[1] == 10) or (
                    playerHand[1][0] == "A" and playerCardValueList[0] == 10):
                print("You Won This Hand!")
                # Add Money
                a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))
                win = True
                stand = True
                break

            # Hit or Stand
            userChoice = input("(2) Do you wish to [H]it or [St]and: ")

            # Hit
            if userChoice.lower() == "hit" or userChoice.lower() == "h":

                # Print Player's Hand
                PlayerCardDealSplit()
                PlayerHandSplit()
                # Change Valid Value
                valid = True

            # Stand
            elif userChoice.lower() == "stand" or userChoice.lower() == "st":
                PlayerHand()
                stand2 = True
                # Change Valid Value
                valid = True

            # Check
            else:
                print("Sorry, that's not an option")


    # If the player didn't split
    elif split == False:
        while stand == False:
            # Bust
            if playerCardTotal > 21:
                print("You Lost!")
                lost = True
                # Subtract Money
                a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
                break

            # Blackjack
            if (playerHand[0][0] == "A" and playerCardValueList[1] == 10) or (playerHand[1][0] == "A" and playerCardValueList[0] == 10):
                print("You Won!")
                # Add Money
                a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))
                win = True
                stand = True
                break

            # Hit or Stand
            userChoice = input("Do you wish to [H]it or [St]and: ")

            # Hit
            if userChoice.lower() == "hit" or userChoice.lower() == "h":

                # Print Player's Hand
                PlayerCardDeal()
                PlayerHand()
                # Change Valid Value
                valid = True

            # Stand
            elif userChoice.lower() == "stand" or userChoice.lower() == "st":
                PlayerHand()
                stand = True
                # Change Valid Value
                valid = True

            # Check
            else:
                print("Sorry, that's not an option")

# Dealer
if split == False:
    while dealerCardTotal < 17 and lost == False:
        # Print and Hit Dealer's Hand
        DealerCardDeal()
        DealerHand()
    if dealerCardTotal >= 17 and lost == False:
        if dealerCardTotal > 21 or playerCardTotal > dealerCardTotal:
            print("You Won!")
            # Add Money
            a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))
        elif (dealerCardTotal == 21 and playerCardTotal != 21) or (dealerCardTotal > playerCardTotal and dealerCardTotal < 21):
            print("You Lost!")
            # Subtract Money
            a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
        elif playerCardTotal == dealerCardTotal:
            print("It's a push! No one wins!")


# Dealer When Player Splits
elif split == True:


    if split == False:
        while dealerCardTotal < 17 and lost == False:
            # Print and Hit Dealer's Hand
            DealerCardDeal()
            DealerHand()
        if dealerCardTotal >= 17 and lost == False:
            if dealerCardTotal > 21 or playerCardTotal > dealerCardTotal:
                print("You Won This Hand!")
                # Add Money
                a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))
            elif (dealerCardTotal == 21 and playerCardTotal != 21) or (
                    dealerCardTotal > playerCardTotal and dealerCardTotal < 21):
                print("You Lost This Hand!")
                # Subtract Money
                a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
            elif playerCardTotal == dealerCardTotal:
                print("It's a push! No one wins!")


    while dealerCardTotal < 17 and lost == False:
        # Print and Hit Dealer's Hand
        DealerCardDeal()
        DealerHand()
    if dealerCardTotal >= 17 and lost == False:
        if dealerCardTotal > 21 or playerCardTotal2 > dealerCardTotal:
            print("You Won This Hand!")
            # Add Money
            a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))
        elif (dealerCardTotal == 21 and playerCardTotal2 != 21) or (dealerCardTotal > playerCardTotal2 and dealerCardTotal < 21):
            print("You Lost This Hand!")
            # Subtract Money
            a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
        elif playerCardTotal2 == dealerCardTotal:
            print("It's a push! No one wins!")

f.close()
r.close()
a.close()