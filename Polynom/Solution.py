def get_numbers(number1, number2):
    out1 = ''
    out2 = ''
    if number1 != 0 and number2 != 0:
        if number1 != 1 and number1 != -1:
            out1 = str(number1)
        if number1 == -1:
            out1 += '-'
        out1 += 'x'
        if number2 != 1:
            out2 = '^' + str(number2)
        out2 += '+'
    return out1 + out2

def match_polynoms(self, other):
    if not isinstance(other, Polynom):
        other = Polynom(other)
    if len(self.coefficients) >= len(other.coefficients):
        while len(other.coefficients) != len(self.coefficients):
            other.coefficients.insert(0, 0)
    else:
        while len(self.coefficients) != len(other.coefficients):
            self.coefficients.insert(0, 0)
    return self, other


class Polynom:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)

    def __str__(self):
        degree = len(self.coefficients) - 1
        out = ''
        while degree > 0:
            out += get_numbers(self.coefficients[len(self.coefficients) - 1 - degree], degree)
            degree -= 1
        if self.coefficients[len(self.coefficients) - 1] != 0:
            return (out + str(self.coefficients[len(self.coefficients) - 1])).replace('+-', '-')
        else:
            return out[:len(out) - 1].replace('+-', '-')

    def __call__(self, x):
        answer = 0
        for i in range(len(self.coefficients)):
            answer += float(self.coefficients[len(self.coefficients) - (i + 1)]) * float(x) ** float(i)
        return answer

    def __add__(self, other):
        self, other = match_polynoms(self, other)
        result_coeff = []
        for i in range(len(self.coefficients)):
            result_coeff.append(self.coefficients[i] + other.coefficients[i])
        return Polynom(*result_coeff)

    def __sub__(self, other):
        self, other = match_polynoms(self, other)
        result_coeff = []
        for i in range(len(self.coefficients)):
            result_coeff.append(self.coefficients[i] - other.coefficients[i])
        return Polynom(*result_coeff)

    def __mul__(self, other):
        self, other = match_polynoms(self, other)
        result_coeff = [0 for i in range((len(self.coefficients) - 1) * 2 + 1)]
        for i in range(len(self.coefficients)):
            for j in range(len(self.coefficients)):
                result_coeff[len(self.coefficients) - (i + 1) + len(self.coefficients) - (j + 1)] += self.coefficients[i] * other.coefficients[j]
        result_coeff.reverse()
        return Polynom(*result_coeff)

    def __eq__(self, other):
        if isinstance(other, Polynom):
            return self.coefficients == other.coefficients
        else:
            return len(self.coefficients) == 1 and self.coefficients[0] == other

a = Polynom(-1,2,4,-5,111,1,1,0,1,1,-4,0,11,12,0)
print(a)