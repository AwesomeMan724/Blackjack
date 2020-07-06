import os
import random

# Play Again
playAgain = True
while playAgain == True:

    # Files
    os.chdir("C:/Users/kevin/PythonPrograms/Files")
    f = open("BlackJackCards.txt", "r")
    all_lines = f.readlines()
    r = open("BlackJackMoney.txt", "r")
    money_lines = r.readlines()
    a = open("BlackJackMoney.txt", "a")

    # Bet
    print("Your Total Money:", money_lines[-1])
    validBet = False
    while validBet == False:
        try:
            userBet = input("How much money will you bet (minimum $10 and even number): ")
            if int(userBet) in range(10, int(money_lines[-1]) + 1) and int(userBet)%2 == 0:
                validBet = True
            else:
                print("Sorry, that's not an amount you can bet")
        except:
            print("Sorry, that's not an amount you can bet")

    # List of Hands
    handList = []

    handCount = 1
    winCount = 0
    loseCount = 0
    stand = False

    # Check for Duplicate Cards
    seen = []

    # Deal Card
    def CardDeal():
        generated = False
        while generated == False:
            # Generate Card Number
            randCardNum = random.randrange(1, 14)
            cardNum = all_lines[randCardNum].strip()

            # Generate Car d Suit
            randSuitNum = random.randrange(15, 19)
            cardSuit = all_lines[randSuitNum].strip()

            # Join into a single card
            card = cardNum + cardSuit
            if card not in seen:
                generated = True
                seen.append(card)
                return card

    # Calculate Hand Total
    def HandTotal(hand):
        global cardTotal
        cardTotal = []
        for x in range(len(hand)):
            if hand[x][0] == "J" or hand[x][0] == "Q" or hand[x][0] == "K":
                cardTotal.append(10)
            elif hand[x][-2].isnumeric():
                if int(hand[x][0]) in range(2, 10):
                    cardTotal.append(int(hand[x][0]))
                elif int(hand[x][0:2]) == 10:
                    cardTotal.append(10)
        for x in range(len(hand)):
            if hand[x][0] == "A" and sum(cardTotal) + 11 <= 21:
                cardTotal.append(11)
            elif hand[x][0] == "A" and sum(cardTotal) + 11 > 21:
                cardTotal.append(1)
        handTotal = sum(cardTotal)
        return handTotal

    # Split Hand
    def SplitHand(hand):
        global newHand
        newHand = []
        newHand.append(hand[1])
        hand.remove(hand[1])
        return newHand

    # Print Hand
    def PrintHand(hand):
        print("Your Hand: ", end="")
        for a in range(len(hand)):
            if a < len(hand) - 1:
                print("{}, ".format(hand[a]), end="")
            elif a == len(hand) - 1:
                print(hand[a], end="")
        print("    (Total is {})".format(HandTotal(hand)))

    # Dealer Print Hand
    def AltPrintHand(hand):
        print("Dealer's Hand: ", end="")
        for a in range(len(hand)):
            if a < len(hand) - 1:
                print("{}, ".format(hand[a]), end="")
            elif a == len(hand) - 1:
                print(hand[a], end="")
        print("    (Total is {})".format(HandTotal(hand)))

    # Split Print Hand
    def SplitPrint(handNum, hand):
        print(handNum, end="")
        for a in range(len(hand)):
            if a < len(hand) - 1:
                print("{}, ".format(hand[a]), end="")
            elif a == len(hand) - 1:
                print(hand[a], end="")
        print("    (Total is {})".format(HandTotal(hand)))


    # Print Dealer's Hand
    dealerHand = []
    dealerHand.append(CardDeal())
    dealerHand.append(CardDeal())
    print("Dealer's Hand:", dealerHand[0])


    #playerHand = ["4S", "4H"]
    playerHand = []
    playerHand.append(CardDeal())
    playerHand.append(CardDeal())
    handList.append(playerHand)
    PrintHand(playerHand)

    finish = False
    win = False
    lose = False
    split = False
    surrender = False

    def HandAction(hand):

        global finish
        global win
        global lose
        global winCount
        global loseCount
        global surrender
        global userBet
        win = False
        lose = False
        finish = False
        # Win Check
        if (hand[0][0] == "A" and cardTotal[0] == 10) or (hand[1][0] == "A" and cardTotal[0] == 10):
            print("You Won!")
            # Add Money
            a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))
            winCount += 1
            finish = True
            win = True

        while finish == False:
            # Lost Check
            if HandTotal(hand) > 21:
                print("You Busted! You Lose!")
                # Subtract  Money
                a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
                loseCount += 1
                finish = True
                lose = True
                break

            # User Input
            userChoice = input("Do you wish to Surrender(X), Double(D), Hit(H) or Stand(S): ")

            # Surrender
            if userChoice.lower() == "surrender" or userChoice.lower() == "x":
                a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet) // 2)))
                print("You Surrendered!")
                surrender = True
                break

            # Double
            elif userChoice.lower() == "double" or userChoice.lower() == "d":
                if int(userBet)*2 <= int(money_lines[-1]):
                    print("You're bet is now", int(userBet)*2)
                    userBet = int(userBet)*2
                    hand.append(CardDeal())
                    PrintHand(hand)
                    finish = True
                    stand = True
                    if HandTotal(hand) > 21:
                        print("You Busted! You Lose!")
                        # Subtract  Money
                        a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
                        loseCount += 1
                        finish = True
                        lose = True
                        break
                    else:
                        break
                else:
                    print("You don't have enough money to double!")

            # Hit
            if userChoice.lower() == "hit" or userChoice.lower() == "h":
                hand.append(CardDeal())
                PrintHand(hand)

            # Stand
            elif userChoice.lower() == "stand" or userChoice.lower() == "s":
                PrintHand(hand)
                finish = True
                break

            # Else
            else:
                print("Sorry, that's not an option")

    def SplitHandAction(hand):

        global finish
        global win
        global lose
        global handCount
        global stand
        global surrender
        global userBet
        win = False
        lose = False
        finish = False

        global split
        split = False
        if hand[0][0] == hand[1][0] and split == False and int((money_lines)[-1])>= int(userBet)*2:

            while finish == False:
                # User Input
                userChoice = input("Do you wish to Surrender(X), Double(D), Hit(H), Stand(S) or Split(P): ")

                # Split
                if userChoice.lower() == "p" or userChoice.lower() == "Split":
                    SplitHand(hand)
                    handCount += 1
                    hand.append(CardDeal())
                    newHand.append(CardDeal())
                    handList.append(newHand)
                    # Print Hands
                    PrintHand(hand)
                    PrintHand(newHand)
                    print("\n", end="")
                    # Hand 1
                    SplitPrint("Hand 1: ", hand)
                    print("Hand 1: ", end="")
                    SplitHandAction(hand)
                    if split == False:
                        HandAction(hand)
                    print("\n", end="")
                    # Hand 2
                    SplitPrint("Hand 2: ", newHand)
                    print("Hand 2: ", end="")
                    SplitHandAction(newHand)
                    if split == False:
                        HandAction(newHand)
                    split = True
                    break

                # Surrender
                if userChoice.lower() == "surrender" or userChoice.lower() == "x":
                    a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet)//2)))
                    print("You Surrendered!")
                    surrender = True
                    break

                # Double
                elif userChoice.lower() == "double" or userChoice.lower() == "d":
                    if int(userBet)*2 <= int(money_lines[-1]):
                        print("You're bet is now", int(userBet)*2)
                        userBet = int(userBet)*2
                        hand.append(CardDeal())
                        PrintHand(hand)
                        finish = True
                        stand = True
                        if HandTotal(hand) > 21:
                            print("You Busted! You Lose!")
                            # Subtract  Money
                            a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
                            loseCount += 1
                            finish = True
                            lose = True
                            break
                        else:
                            break
                    else:
                        print("You don't have enough money to double!")


                # Hit
                elif userChoice.lower() == "hit" or userChoice.lower() == "h":
                    hand.append(CardDeal())
                    PrintHand(hand)
                    finish = True
                    break

                # Stand
                elif userChoice.lower() == "stand" or userChoice.lower() == "s":
                    PrintHand(hand)
                    finish = True
                    stand = True
                    break

                # Else
                else:
                    print("Sorry, that's not an option")

    SplitHandAction(playerHand)
    if split == False and stand == False:
        HandAction(playerHand)

    if split == True and surrender == False:
        if handCount != winCount and handCount != loseCount:
            # Dealer's Turn
            finish = False
            while finish == False:
                AltPrintHand(dealerHand)
                if HandTotal(dealerHand) <= 16:
                    dealerHand.append(CardDeal())
                elif (HandTotal(dealerHand) >= 17 and HandTotal(dealerHand) < 21) or HandTotal(dealerHand) == 21:
                    finish = True
                elif HandTotal(dealerHand) > 21:
                    finish = True

        # Results
        for x in range(len(handList)):
            win = False
            lose = False
            if (handList[x][0][0] == "A" and cardTotal[0] == 10) or (handList[x][1][0] == "A" and cardTotal[0] == 10):
                win = True
            elif HandTotal(handList[x]) > 21:
                lose = True
            if win == False and lose == False:
                if (dealerHand[0][0] == "A" and cardTotal[0] == 10) or (dealerHand[1][0] == "A" and cardTotal[0] == 10):
                    print("Hand {}: ".format(x + 1), end="")
                    print("You Lose!")
                    # Subtract  Money
                    a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
                    finish = True
                    split = True
                    break
                elif HandTotal(dealerHand) > 21:
                    print("Hand {}: ".format(x + 1), end="")
                    print("The Dealer Busted! You Won!")
                    # Add Money
                    a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))
                    split = True
                    break
                elif HandTotal(handList[x]) > HandTotal(dealerHand):
                    print("Hand {}: ".format(x + 1), end="")
                    print("You Won!")
                    # Add Money
                    a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))
                    split = True
                elif HandTotal(handList[x]) < HandTotal(dealerHand):
                    print("Hand {}: ".format(x + 1), end="")
                    print("You Lost!")
                    # Subtract  Money
                    a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
                    split = True
                elif HandTotal(handList[x]) == HandTotal(dealerHand):
                    print("Hand {}: ".format(x + 1), end="")
                    print("It's a push! No One Wins!")
                    split = True

    elif surrender == False:

        # Dealer's Turn
        finish = False
        while win == False and lose == False and finish == False:
            AltPrintHand(dealerHand)
            if HandTotal(dealerHand) <= 16:
                dealerHand.append(CardDeal())
            elif (HandTotal(dealerHand) >= 17 and HandTotal(dealerHand) < 21) or HandTotal(dealerHand) == 21:
                finish = True
            elif HandTotal(dealerHand) > 21:
                finish = True

        if (dealerHand[0][0] == "A" and cardTotal[0] == 10) or (dealerHand[1][0] == "A" and cardTotal[0] == 10):
            print("You Lose!")
            # Subtract  Money
            a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))
            finish = True
        elif HandTotal(dealerHand) > 21:
            print("The Dealer Busted! You Won!")
            win = True
            # Add Money
            a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))

        elif HandTotal(playerHand) > HandTotal(dealerHand) and win == False and lose == False:
            print("You Won!")
            # Add Money
            a.write("\n{}".format(str(int(money_lines[-1]) + int(userBet))))

        elif HandTotal(playerHand) < HandTotal(dealerHand) and win == False and lose == False:
            print("You Lost!")
            # Subtract  Money
            a.write("\n{}".format(str(int(money_lines[-1]) - int(userBet))))

        elif HandTotal(playerHand) == HandTotal(dealerHand) and win == False and lose == False:
            print("It's a push! No One Wins!")


    # Play Again
    choiceMade = False
    while choiceMade == False:
        playAgain = input("Play Again? [Y]es / [N]o: ")
        if playAgain.lower() == "y" or playAgain.lower() == "yes":
            playAgain = True
            print("\n")
            choiceMade = True
        elif playAgain.lower() == "n" or playAgain.lower() == "no":
            print("Bye!")
            choiceMade = True
            exit()
        else:
            print("Sorry, that's not an option!")
    f.close()
    r.close()
    a.close()