for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0 and num % 7 == 0:
        print("Fizzbang")
    elif num % 5 == 0 and num % 7 == 0:
        print("Buzzbang")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 7 == 0:
        print("Bang")
    else:
        print(num)
