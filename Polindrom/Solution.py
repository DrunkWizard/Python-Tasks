def is_polyndrom (n: int) -> int:
    result = []
    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range (2, 36):
        x = n
        y = ''
        while (x > 0):
            num = symbols[x % i]
            x = x//i
            y += num
        if (y == y[::-1]):
            result.append(i)
    if (len(result) == 0):
        return 0
    elif (len(result) == 1):
        return result[0]
    else:
        min = 37
        for i in range (0, len(result)):
            if(result[i] < min):
                min = result[i]
        return min
print(is_polyndrom(1))