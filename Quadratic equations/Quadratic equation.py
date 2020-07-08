Equation = input()
indexA = Equation.find(" ")
a = float(Equation[0:indexA])
indexC = Equation.rfind("x") + 2
c = float(''.join(Equation[indexC:len(Equation)].split()))
indexB = Equation.find("^") + 3
indexB2 = Equation.rfind("*") - 1
b = float(''.join(Equation[indexB:indexB2].split()))
discriminant = pow(b, 2) - 4 * a * c
if discriminant < 0:
    print("No solution")
if discriminant == 0:
    x = -b / 2 * a
    print(x)
if discriminant > 0:
    x1 = (-b + pow(discriminant, 1 / 2)) / (2 * a)
    x2 = (-b - pow(discriminant, 1 / 2)) / (2 * a)
    print("x1= ", x1 , " ", "x2 = ", x2)

