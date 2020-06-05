import re
from string import ascii_lowercase

def letters_in_word(letters, word):
    """Return True if any of letters are in word"""
    for l in letters:
        if l in word:
            return True
    return False
    

def word_finder(allowed_letters):
    """Return a list of words that meet the spelling bee criteria.
        * The words may only contain the allowed_letters.
        * The first letter in allowed_letters is the key letter. Returned words
          must contain it.
        * Words must be for characters or more in length.
    """
    
    key_letter = allowed_letters[0] # first letter is "key." it must be contained
    bad_letters = re.sub(f'[{allowed_letters}]', '', ascii_lowercase) # get all un-allowed letters

    with open('data/norvig_word_list.txt') as f: # http://norvig.com/ngrams/word.list
        word_list = [word.strip() for word in f.readlines()]

    good_words = list()
    for word in word_list:
        word = word.lower()

        if len(word) < 4:
            continue 
        if key_letter not in word:
            continue
        if letters_in_word(bad_letters, word):           
            continue
        good_words.append(word)

    good_words.sort(key=len)
    
    return good_words

def find_pangrams(good_words):
    """Return a list of pangrams (ie words containing all allowed letters)
        from a list of words"""
    
    # there are 7 letters in the game, any word with 7 unique letters is a pangram
    return [w for w in good_words if len(set(w)) == 7]