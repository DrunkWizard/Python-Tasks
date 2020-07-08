import re
import math
class SquareEquationException(Exception):
    pass

def solve_square_equation(expr: str)-> list:
    expr = re.sub(r"\s+", "", expr)
    valid_check(expr)
    arguments = parse_arguments(expr)
    a = arguments[0]
    b = arguments[1]
    c = arguments[2]
    discriminant = b ** 2 - 4 * a * c
    if (discriminant < 0):
        raise SquareEquationException("Discriminant < 0!")
    elif (discriminant == 0):
        result = [(-1 * b) / (2 * a)]
    else:
        if (a == 0):
            result = [-c / b]
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            result = [x1, x2]
    print(sorted(list(set(result))))
    return sorted(list(set(result)))

def parse_arguments(equation):
    a_pattern = r"\A(\+|\-)?\d*"
    b_pattern1 = r"(\+|\-)*\d*\*?([a-z]|[A-Z])(\+|\-)"
    b1 = re.search(b_pattern1, equation).group()
    b_pattern2 = r"(\+|\-)*\d*"
    c_pattern = r"(\+|\-)*\d*\Z"
    a = float(re.search(a_pattern, equation).group())
    b = float(re.search(b_pattern2, b1).group())
    c = float(re.search(c_pattern, equation).group())
    result = []
    result.append(a)
    result.append(b)
    result.append(c)
    return result

def valid_check(equation):
    equation_pattern = r"(\+|\-)?\d*(\*)?([a-z]|[A-Z])(\^){1}2{1}(\+|\-)*\d*\*?([a-z]|[A-Z])(\+|\-)*\d*$"
    match = re.search(equation_pattern, equation)
    if match is None:
        raise SquareEquationException("String isnt equation!")
    match = match.group()
    print(match)

print(solve_square_equation("+1*x^2+2*x+1"))