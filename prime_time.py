user_number = int(input("Please enter a number."))

def is_prime(number):
    if number < 2:
      return False
   
    if number == 2:
      return True
   
    for i in range(2, (number - 1)):
      if number % i == 0:
        return False
    
    return True
      
user_number = is_prime(user_number)
print(user_number)

    
