"""
Python basics, Problem Set, hangman.py
Name: Yen
Collaborators: None
Time spent: 2 hours
"""

# ---------------------------------------------------------------------------- #
#                                 Hangman Game                                 #
# ---------------------------------------------------------------------------- #


# -------------------------------- Helper code ------------------------------- #
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
    with open(WORDLIST_FILENAME, "r") as inFile:
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# ---------------------------- end of helper code ---------------------------- #


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_set, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far, assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed, False otherwise
    """

    for letter in secret_set:
        if letter not in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
        which letters in secret_word have been guessed so far.
    """
    res = ""

    for char in secret_word:
        if char in letters_guessed:
            res += char
        else:
            res += "_ "

    return res


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    """
    all_letters = list(string.ascii_lowercase)

    for char in letters_guessed:
        index = ord(char) - 97
        all_letters[index] = ""

    return "".join(all_letters)


def check_valid_guess(character, avail_letters):
    """
    character: user input
    returns:
    - 0 if character is alphabetical and hasn't been guessed so far (in avail_letters).
    - 1 if character is not alphabetical
    - 2 if the character has already been guessed
    """

    avail_set = set(avail_letters)
    all_letters = set(string.ascii_letters)

    if character in avail_set:
        return 0

    elif character not in all_letters:
        return 1

    else:
        return 2


def general_hangman(mode, secret_word):
    """
    mode: 'normal' mode, or 'with hints' mode

    secret_word: string, the secret word to guess.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
    partially guessed word so far.

    * If the guess is the symbol * and the mode is 'with hints', print out all words in wordlist that matches the current guessed word.
    """

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long" % len(secret_word))

    # initialize warnings, score, guess count, available letters and letters guessed
    score = 0
    guess_count = 6
    warning_count = 3
    avail_letters = get_available_letters("")
    letters_guessed = set()
    resulting_guess = ""
    secret_set = set(secret_word)

    # the game loops until the guess count == 0
    while guess_count > 0:
        print("--------------------------------")
        print("You have %d guesses left." % guess_count)
        print("Available letters: ", avail_letters)
        guess = input("Please guess a letter: ").lower()
        guess_validity = check_valid_guess(guess, avail_letters)

        # if guess == * and is with hints mode: display hint
        if guess == "*" and mode == "with hints":
            hint_words = show_possible_matches(resulting_guess)
            if len(hint_words) == 0:
                print("No Matches Found")
            else:
                hint_words = " ".join(hint_words)
                print(hint_words)
            continue

        # if guess not alphabetical or already been guessed -> warning
        if guess_validity != 0:
            warning_count -= 1
            resulting_guess = get_guessed_word(secret_word, letters_guessed)

            # if non-alpha
            if guess_validity == 1:
                print("Oops! That is not a valid letter.")
            # if already been guessed
            else:
                print("Oops! You've already guessed that letter.")

            # if still have more warnings
            if warning_count > 0:
                print(
                    "You have %d warnings left: %s" % (warning_count, resulting_guess)
                )

            # if no more warnings
            else:
                guess_count -= 1
                warning_count = 3
                print(
                    "You have no warnings left so you lose one guess: %s"
                    % resulting_guess
                )

        # if valid guess
        else:
            letters_guessed.add(guess)

            # the '_ _' format after the guess
            resulting_guess = get_guessed_word(secret_word, letters_guessed)

            # check if guess character in secret word
            if guess in secret_set:
                print("Good guess: %s" % resulting_guess)

            else:
                vowels = {"a", "e", "i", "o", "u"}
                # if guess is vowel, deduct an extra guess count
                if guess in vowels:
                    guess_count -= 1
                guess_count -= 1
                print("Oops! That letter is not in my word: %s" % resulting_guess)

            # check if the resulting guess is the secret word
            check_if_secret = is_word_guessed(secret_set, letters_guessed)

            if check_if_secret:
                score = guess_count * len(secret_set)
                print("--------------------------------")
                print("Congratulations, you won!")
                print("Your total score for this game is:", score)
                break

        # update avail letters
        if guess_validity == 0 or guess_validity == 2:
            avail_letters = get_available_letters(letters_guessed)
    if not check_if_secret:
        print("Sorry, you ran out of guesses. The word was", secret_word)


def hangman(secret_word):
    """
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
    """
    general_hangman("normal", secret_word)


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # remove spaces from my word
    my_word = my_word.replace(" ", "")

    # if diff length, return False immediately
    if len(my_word) != len(other_word):
        return False

    # two pointers in my_word and other_word to compare
    for i in range(len(my_word)):
        my_char = my_word[i]
        other_char = other_word[i]

        if my_char != other_char:
            if my_char != "_":
                return False

    # after iterating through 2 words,return True
    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word

    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.

    """
    res = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            res.append(word)
    return res


def hangman_with_hints(secret_word):
    """
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
    """
    general_hangman("with hints", secret_word)


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
