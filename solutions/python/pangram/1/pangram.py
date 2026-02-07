def is_pangram(sentence):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    lower_sentence = sentence.lower()
    filter_sentence = filter(lambda a: a.isalpha(), lower_sentence)
    sentence_set = set(filter_sentence)
    return sentence_set == alphabet_set
