import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
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

wordlist = load_words()

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for a in secret_word:
        for i in letters_guessed:
            if a == i:
                break
        if i != a:
            return False
    if i == a:
        return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    s = ""
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for a in secret_word:
        for i in letters_guessed:
            if a == i:
                s += a + " "
                break
        if a != i:
            s += " _ "
    return s



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = string.ascii_lowercase
    s = ""
    for n in result:
        if n not in letters_guessed:
            s += n
    return "Available Letters: " + s

def point(guesses_remaining, secret_word):
    unique_letter_list = ""

    for i in secret_word:
        if i not in unique_letter_list:
            unique_letter_list += i
    unique_letter_len = len(unique_letter_list)

    total_score = unique_letter_len * guesses_remaining
    return "Your total score for this game is: " + str(total_score)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_length = (len(secret_word))
    attempt = 6
    warning = 3
    letters_list = []
    print("Welcome to Hangman!")
    print("I'm thinking of a word that is " + str(word_length) + " letters long")
    print("You have " + str(warning) + " warnings left.")

    while attempt > 0 :
        print("-----------")
        print("you have " + str(attempt) + " guesses left")
        print(get_available_letters(letters_list))
        letter = input("Please Guess a Letter: ")
        letter = letter.lower()

        if letter not in string.ascii_lowercase:
            warning -= 1
            print("Oops! That is not a valid letter." + "You have " + str(warning) + " warnings left:")
            if warning <= 0:
                attempt -= 1
                if attempt <= 0:
                    print("\nGAMEOVER!")
        else:
            if letter in letters_list:
                print("word has already been guest")
                continue
            else:
                letters_list.append(letter)
                if letter not in secret_word:
                    print("Oops that is not a letter in my word!", end = " ")
                    attempt -= 1
                    if letter == 'a' or letter == "e" or letter == 'o' or letter == 'u' or letter == 'i':
                        attempt -= 1
                    if attempt <= 0:
                        print("\nGAMEOVER!")
                        print("The word was: " + secret_word)
                        break
                    print(get_guessed_word(secret_word, letters_list))
                else:
                    print("Good Guess!", end = " ")
                    print(get_guessed_word(secret_word, letters_list))
                    if is_word_guessed(secret_word, letters_list) == True:
                        print("-----------")
                        print("Congratulation, You Won!")
                        print(point(attempt, secret_word))
                        print("-----------")
                        break

secret_word = choose_word(wordlist)
hangman(secret_word)
