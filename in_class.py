

#my code
numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
guess = int(input("Guess a number to see if it's in the array: "))
for number in numbers:
    if guess == number:
        print(f"Your number, {guess}, is in the array at !")
        break
    else:
        print(f"Your number, {guess}, is not in the array.")

#class code
numbers = [10, 20, 30, 5]
number_to_search = int(input("Enter your number to search:"))
for index in range(0, len(numbers)):
    if number_to_search == numbers[index]:
        found_index = index
        break

if found_index >= 0:
    print(f"Found at index {found_index}")
else:
    print("Not found")
