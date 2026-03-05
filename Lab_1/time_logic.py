num = int(input("Enter a large integer representing a total number of seconds (e.g., 15000). "))

hour = num//3600       # hour = int(num%3600)
remainderMin = num%3600
minutes = remainderMin//60
second =remainderMin%60


print(num , " seconds is " , hour , "hours, " , minutes , "minutes, and " , second , " seconds.")