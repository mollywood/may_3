test_num = int(input("Enter a number here to test if it's a prime number: "))


if test_num > 1:
    for i in range(2, (test_num - 1)):
        if (test_num % i) == 0:
            print(f"{test_num} is a prime number.")
        else:
            print("This is not a prime number.")
else:
    print("This is not a prime number.")
