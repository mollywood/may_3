test_string = input("Input a word to see if it's a palindrome: ")
letters = []

# turns word into an array of the individual letters
for char in test_string:
    letters.append(char)

# turns array backwards
srettel = letters[::-1]

#test if the backwards letters are equal to the test_string
if letters == srettel:
    print("It's a palindrome!")
else:
    print("Not a palindrome")
