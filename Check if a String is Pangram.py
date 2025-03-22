import string

def is_pangram(sentence):
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence.lower())
    return alphabet_set.issubset(sentence_set)

# Example usage
user_input = input("Enter a sentence: ")
if is_pangram(user_input):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
