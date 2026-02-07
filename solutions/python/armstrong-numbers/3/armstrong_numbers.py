def is_armstrong_number(number):
    number_string = str(number)
    power = len(number_string)
    value = sum([int(ch)**power for ch in number_string])
    return number == value

    
