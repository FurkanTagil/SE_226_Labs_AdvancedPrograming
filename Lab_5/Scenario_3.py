result = 0

def geometric_sum(n, r, i=0):
    """
    This recursive function calculates the geometric series:

        Gn = 1 + r + r^2 + r^3 + ... + r^n

    Logic:
    - The function starts from i = 0 and goes up to i = n.
    - At each recursive call, it adds the term r^i to the global result.
    - Then it calls itself with the next value of i (i+1).
    - The recursion stops when i > n (base case).

    Sign Handling:
    - There is no alternating sign in this series.
    - All terms are positive powers of r.
    """

    global result

    if i > n:
        return

    result += r ** i

    geometric_sum(n, r, i + 1)

n = int(input("Enter n (number of terms): "))
r = int(input("Enter r (common ratio): "))

geometric_sum(n, r)

print("Geometric Sum:", result)