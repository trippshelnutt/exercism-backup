def reverse(text):
    characters_with_index = list(enumerate(text))
    reversed_characters_with_index = reversed(characters_with_index)
    reversed_characters = map(lambda n: n[1], reversed_characters_with_index)
    return ''.join(reversed_characters)
