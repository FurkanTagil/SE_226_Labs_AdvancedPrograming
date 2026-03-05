n = int(input("Please enter a number between 3 and 9: "))

while n < 3 or n > 9:
    n = int(input("Invalid input, enter again: "))

for x in range(1, 2*n):

    if x <= n:
        k = x
    else:
        k = 2*n - x

    print("*" * k)