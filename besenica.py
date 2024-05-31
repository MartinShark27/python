import os.path
#pitane za ime na file (proverka dali syshtesvuva)
fileName = input("Type file name: ")
while not os.path.isfile(fileName):
    print("file not found")
    fileName = input("Type file name: ")
#chetene ot file
m = open(fileName, "rt")
mysteryWord = m.read()
#vizualizirane na dumata s "_"
guessWord = "_"*len(mysteryWord)
print(guessWord)
#opiti za poznavane na bukva -> pravo na 6 greshki
br=6
while br>0 and guessWord != mysteryWord:
    #vyvejdane na bukva
    letter = input("Input a letter ")
    flag = False
    newGuessString = list(guessWord)

    for i in range(len(mysteryWord)):
        if mysteryWord[i] == letter:
            newGuessString[i] = letter
            flag = True
    
#izpechatvane na greshka/dumata s otkritite bukvi
    guessWord = "".join(newGuessString)
    if not flag:
        br-=1
        print(f"You have {br} tries left")
    else:
        print(guessWord)
if br==0:
    print("u lost")
else:
    print("congrats you guessed it")