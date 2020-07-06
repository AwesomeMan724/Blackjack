import os
import random

os.chdir("C:/Users/kevin/PythonPrograms/Files")
f = open("HangmanDictionary.txt", "r")
all_lines = f.readlines()

# Choosing a difficulty level
difficultyChosen = False
while not difficultyChosen:
    difficulty = input("Choose a difficulty level (Easy, Medium, or Hard):")
    if difficulty == "Easy" or difficulty == "easy":
        randnum = (random.randrange(7))
        word = all_lines[randnum].strip()
        difficultyChosen = True
    elif difficulty == "Medium" or difficulty == "medium":
        randnum = (random.randrange(8, 15))
        word = all_lines[randnum].strip()
        difficultyChosen = True
    elif difficulty == "Hard" or difficulty == "hard":
        randnum = (random.randrange(16, 23))
        word = all_lines[randnum].strip()
        difficultyChosen = True
    else:
        print("That's not a difficulty level!")

# Printing asterisks
# print(word)
letterList = []
for x in range(len(word)):
    letterList.append("*")
    if word[x] == " ":
        letterList[x] = " "
    print(letterList[x], end="")

# The meat and potatoes
won = False
consecCorrect = False
zeroList = []
trycount = 0
noSpaceword = word.replace(" ", "")
while won == False:
    singleLetter = True
    rawUserLetter = input("\nPlease enter single a letter:")
    userLetter = rawUserLetter.lower()

    # Checks
    if len(userLetter) != 1:
        print("I said a single letter!")
        singleLetter = False
    if userLetter == " ":
        print("I said a single letter!")
        singleLetter = False
    alpha = userLetter.isalpha()
    if alpha == False:
        print("I said a single letter!")
        singleLetter = False

    if singleLetter == True:
        if userLetter not in word:
            print(userLetter, "is not in the word")
            consecCorrect = False
            trycount += 1
        if userLetter in word and consecCorrect == False:
            consecCorrect = True
            trycount += 1
        while userLetter in word:
            letterPosition = word.find(userLetter)
            letterList[letterPosition] = userLetter
            word = word.replace(userLetter, "0", 1)
            zeroList.append("0")
        for x in range(len(word)):
            if x < len(word) - 1:
                print (letterList[x], end="")
            elif x == len(word) - 1:
                print(letterList[x])

        # print(word)
        if len(zeroList) == len(noSpaceword):
            if trycount > 1:
                print("You won in", trycount, "tries!")
                won = True
            elif trycount == 1:
                print("You won in 1 try!")
            won = True
        if won == False:
            print("You have used", trycount, "tries")