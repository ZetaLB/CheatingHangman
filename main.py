# authors Zeta Lenhart-Boyd and Perrin Craig


def getWordLength(wordList):
    while True:
        wordLength = int(input("Type in the length of the word: "))
        while wordLength < 2:
            wordLength = int(input("Type a number greater than 1"))
        for word in wordList:
            if len(word) == wordLength:
                return wordLength
        print("There are no words of this length in the dictionary, try another number: ")

# Prompt the user for whether they want to have a running total of the number of words remaining in the word list
def runningTotal():
    while True:
        yesOrNo = input("Would you like a running total of the number \n 5of words remaining words ? y/n: ")
        if yesOrNo == "y" or yesOrNo == "n":
            return yesOrNo
        else:
            print("Please type 'y' or 'n': ")

# Prompt the user for a single letter guess
def guessALetter(alreadyGuessed):
    while True:
        letterGuess = input("Guess a single letter: ")
        if letterGuess in alreadyGuessed or len(letterGuess) != 1 or not letterGuess.isalpha():
            print("Please type a single letter that has not already been guessed")
        else:
            alreadyGuessed.append(letterGuess)
            return letterGuess

def wordLengthCheck(wordList, inputLength):
    inputLengthWords = []
    for word in wordList:
        if inputLength == len(word):
            inputLengthWords.append(word)
    return inputLengthWords

def playHangman(wordList, guessesCount, wordlength, runningTotal):
    currentPattern = "-" * wordlength
    youWon = False
    alreadyGuessed = []
    while guessesCount > 0 and not youWon:
        if runningTotal == "y":
            print("You have", len(wordList), "possible word(s)")
        print("You have", guessesCount, "guesses left")
        print("These are the letters you have guessed", alreadyGuessed)
        letterGuessed = guessALetter(alreadyGuessed)
        wordFamilies = {}
        for word in wordList:
            # update the pattern for that word based on current pattern and letter guessed
            newPattern = updatePattern(currentPattern,letterGuessed,word)
            # check to see if pattern is exists in wordFamilies
            if newPattern in wordFamilies:
                # if it does add current word to list with that pattern into wordFamily
                wordFamilies[newPattern].append(word)
            else:
                # if it does not add a new pattern and add a list with just that word to wordFamilies
                wordFamilies[newPattern] = [word]
        # find the longest list in wordFamilies
        biggestLength = 0
        biggestPattern = ""
        for pattern in wordFamilies:
            if len(wordFamilies[pattern]) > biggestLength:
                biggestLength = len(wordFamilies[pattern])
                biggestPattern = pattern
        # its pattern becomes new current pattern and its list becomes new word list
        currentPattern = biggestPattern
        wordList = wordFamilies[currentPattern]
        if letterGuessed not in currentPattern:
            guessesCount -= 1
        print(currentPattern)
        if "-" not in currentPattern:
            youWon = True
            print("Conrats you beat the cheating robot !")
            return None
    print("uh oh... you lost :( the word was:", wordList[0])

def updatePattern(pattern, letter, word):
    for index in range(len(word)):
        if word[index] == letter:
            pattern = pattern[0:index] + letter + pattern[index+1:]
    return pattern

# open the file
dictionary = open("dictionary.txt", "r")

# read the file
data = dictionary.read()

# split text when there is a new line
wordList = data.split("\n")
dictionary.close()

numberOfGuesses = int(input("Type in the number of guesses: "))
wordLength = getWordLength(wordList)
yesNo = runningTotal()
newWordList = wordLengthCheck(wordList, wordLength)
playHangman(newWordList, numberOfGuesses, wordLength, yesNo)