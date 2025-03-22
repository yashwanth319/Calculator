def reverse_string(user_input):
    return user_input[::-1]

# Accept user input
user_text = input("Enter a string to reverse: ")
reversed_text = reverse_string(user_text)

print(f"Reversed String: {reversed_text}")
