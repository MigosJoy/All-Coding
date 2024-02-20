# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)


import random
import string


WORDLIST_FILENAME = '/Users/jsspace/All-Coding-Local/All-Coding/Python/MIT_EDX_CS_Python_Intro/Unit_3/words.txt'


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    letter_in = 0
    test = len(secretWord)
    for i in secretWord:
        if i in lettersGuessed:
            letter_in += 1
    if letter_in == test:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    display_letters = ''
    for i in secretWord:
        if i in lettersGuessed:
            display_letters += i
        else:
            display_letters += '_ '
    return display_letters


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    original_letters = string.ascii_lowercase
    available_letters = ''
    for letter in original_letters:
        if letter in lettersGuessed:
            available_letters += ''
        else:
            available_letters += letter
    return available_letters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secretWord)) + ' letters long.')
    GuessesRemaining = 8
    lettersGuessed = []
    while GuessesRemaining >= 0:
        print('-------------')
        if GuessesRemaining == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            break
        else:
            print('You have ' + str(GuessesRemaining) + ' guesses left.')
            print('Available letters: ' + getAvailableLetters(lettersGuessed))
            letterGuessed = str(input("Please guess a letter: "))
            if letterGuessed in lettersGuessed:
                print("Oops! You've already guessed that letter: " +
                      getGuessedWord(secretWord, lettersGuessed))
            elif letterGuessed in secretWord:
                lettersGuessed += letterGuessed
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print('--------------')
                    print('Congratulations, you won!')
                    break
            else:
                lettersGuessed += letterGuessed
                print("Oops! That character is not in my word: " +
                      getGuessedWord(secretWord, lettersGuessed))
                GuessesRemaining -= 1


hangman(secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
