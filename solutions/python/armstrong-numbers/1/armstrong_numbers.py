def is_armstrong_number(number):
    individual_numbers = list(map(int, list(str(number))))
    power = len(individual_numbers)
    value = sum(map(lambda i: i**power, individual_numbers))
    return number == value

    
