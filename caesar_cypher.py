user_text = input("Please enter your text.").strip()
user_key = int(input("Please enter your key."))

def caesar_cypher(text, shift):
    new_text = ""
    for letter in text:
        if letter.isupper():
            new_text += chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        elif letter.islower():
            new_text += chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_text += letter
    return new_text

user_text = caesar_cypher(user_text, user_key)
print(user_text)

