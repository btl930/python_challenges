#Reverse string by slicing
user_name = "Hello World"

def reverse_string(string):
    reverse_string = string[::-1]
    return reverse_string

user_name = reverse_string(user_name)
print(user_name)

#Reverse string using a for loop
user_name = "Hello World"

def reverse_string(string):
    reverse_string = ""
    for char in string:
        reverse_string = char + reverse_string
    return reverse_string

user_name = reverse_string(user_name)
print(user_name)