def is_isogram(string):
    filtered_string = list(filter(lambda a: a.isalpha(), string.lower()))
    return len(filtered_string) == len(set(filtered_string))
