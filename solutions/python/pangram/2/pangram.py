import string

def is_pangram(sentence):
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence.lower())
    return sentence_set >= alphabet_set
