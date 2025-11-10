import string

test_word = input("Please input the word you would like to test.")

def is_palindrome(input):
    translator = str.maketrans('', '', string.punctuation)
    normalized_string = input.lower().replace(" ", "").translate(translator)
    print(normalized_string)
    return normalized_string == normalized_string[::-1]

if is_palindrome(test_word) is True:
    print(f"{test_word} is a palindrome!")
else:
    print(f"{test_word} is NOT a palindrome.")