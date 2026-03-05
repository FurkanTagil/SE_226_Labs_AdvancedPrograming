print("Enter a positie integer between 10 and 100. ")
FizzBuzzCounter = 0
FizzCounter = 0
BuzzCounter = 0
num = 0


while True:
    num = int(input())
    if num>=10 and num<=100:
        break
    print("Invalid input, enter again.")

for x in range(1, num+1):
    if(x%3==0 and x%5==0):
        FizzBuzzCounter +=1
        print("FizzBuzz")
    elif(x%3==0):
        FizzCounter +=1
        print("Fizz")
    elif(x%5==0):
        BuzzCounter +=1
        print("Buzz")
    elif(x%7==0):
        print(x, "is skipped")
    else:
        print(x)

print("--- Summary ---")
print("Fizz count: ", FizzCounter)
print("Buzz count: ", BuzzCounter)
print("FizzBuzz count: ", FizzBuzzCounter)