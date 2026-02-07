def square(number):
    if not valid_number(number):
        raise ValueError("square must be between 1 and 64")
    return pow(2, number - 1)


def total():
    return sum(map(square, chessboard_squares()))

def valid_number(number):
    return 1 <= number <= 64

def chessboard_squares():
    return range(1, 65)