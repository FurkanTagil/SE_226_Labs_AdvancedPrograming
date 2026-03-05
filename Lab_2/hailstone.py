num = int(input("Please enter a positive integer greater than 1: "))
counter = 0

while num!= 1:
    if num%2==0:
        num //=2
        counter +=1
        print(num, " ==> ", end=" ")
    else:
        num = (num*3)+1
        counter+=1
        print(num, "==>", end=" ")

print("\nTotal steps: ", counter)