import string
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------




def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    word_length = 0
    word = ""
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for  i in my_word:
        if i == " ":
            continue
        else:
            word += i
            word_length += 1

    if word_length == len(other_word):
        for num in range(word_length):
            if word[num] == "_":
                continue
            elif word[num] != other_word[num]:
                return False
    else:
        return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    word_list = ""
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for words in wordlist:
        if match_with_gaps(my_word, words) == True:
            word_list += " " + words
    return "Possible words: " + words



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_length = (len(secret_word))
    attempt = 6
    warning = 3
    letters_list = ""
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
            if letter == "*":
                show_possible_matches(letters_list)
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
                letters_list += letter
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


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
