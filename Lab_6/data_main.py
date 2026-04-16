from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)

data = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

parts = data.split(",")

parts = strip_whitespaces(parts)

numbers = []
valid = True

for p in parts:
    if p.replace('.', '', 1).replace('-', '', 1).isdigit():
        numbers.append(float(p))
    else:
        valid = False
        break

if not valid:
    print("Data Error: Please make sure you only enter numbers separated by commas.")
else:
    numbers = remove_duplicates(numbers)

    print("Cleaned and unique data:", numbers)
    print("--------------------")
    print("Mean:", round(calculate_mean(numbers), 2))
    print("Maximum:", find_maximum(numbers))
    print("Minimum:", find_minimum(numbers))