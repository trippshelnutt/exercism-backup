def convert(number):
    result = ''    

    if is_divisible_by(number, 3):
        result += 'Pling'
    if is_divisible_by(number, 5):
        result += 'Plang'
    if is_divisible_by(number, 7):
        result += 'Plong'

    return result if len(result) else str(number)

def is_divisible_by(number, divisor):
    return number % divisor == 0
