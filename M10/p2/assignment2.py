'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secret_word_giv
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
def get_guessed_word(secret_word, letters_guessed):
    """This function returns a string that is comprised of letters and underscores, based on what
    letters in letters_guessed are in secret_word."""
    str1 = ""
    for i in secret_word:
        if i not in letters_guessed:
            str1 += " _"
        else:
            str1 += i
    return str1

def is_word_guessed(secret_word, letters_guessed):
    '''is word guessed? '''
    secret_set = set(secret_word)
    intersect = secret_set.intersection(set(letters_guessed))
    return bool(len(intersect) == len(secret_set))
def get_available_letters(letters_guessed):
    """gives the available letters for guess """
    import string
    a_list = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in a_list:
            a_list.remove(i)
    return "".join(a_list)

WORD_LIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORD_LIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # WORD_LIST: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list

def choose_word(word_list):
    """
    WORD_LIST (list): list of words (strings)

    Returns a word from WORD_LIST at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------
