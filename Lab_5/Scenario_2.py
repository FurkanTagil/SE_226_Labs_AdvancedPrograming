def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

absolute = lambda x: x if x >= 0 else -x


def exp_x(x, n):
    result = 0

    for i in range(n):
        sign = (-1) ** i
        numerator = x ** (2 * i)
        denominator = factorial(2 * i)

        term = sign * (numerator / denominator)

        term = absolute(term)

        result += term

    return result


x = int(input("Enter x: "))
n = int(input("Enter n: "))

print("Result:", exp_x(x, n))