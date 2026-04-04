def factorial(x):

    if x == 0 or x == 1:
        return 1
    
    return x * factorial(x - 1)


num = int(input("Enter a number: "))
print("Factorial:", factorial(num))