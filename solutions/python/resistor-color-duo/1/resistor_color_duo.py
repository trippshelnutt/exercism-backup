resistor_values_by_color = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
    }

def value(colors):
    color1, color2, *rest = colors
    value1 = resistor_values_by_color[color1]
    value2 = resistor_values_by_color[color2]
    return (value1 * 10) + (value2)
