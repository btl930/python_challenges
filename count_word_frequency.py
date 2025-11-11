from collections import Counter
import string
test_file = "count_word_frequency.txt"

def count_words(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
        file_dict = dict()
        translator = str.maketrans('', '', string.punctuation)
        normalized_file = file_content.strip().lower().translate(translator)
        file_list = normalized_file.split()
        return Counter(file_list)      

test_file = count_words(test_file)
print(test_file)