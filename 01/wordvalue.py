from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        words = [line.strip() for line in file]
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[letter] if letter.isalpha() else 0 for letter in word.upper())

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    score_pairs = [(word, calc_word_value(word)) for word in words]
    return max(score_pairs, key=lambda pair: pair[1])[0]

if __name__ == "__main__":
    pass # run unittests to validate
