def is_isogram(string):
    filtered_string = list(filter(lambda a: a.isalpha(), string.lower()))
    filtered_string_set = set(filtered_string)
    return len(filtered_string) == len(filtered_string_set)
