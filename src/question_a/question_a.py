#write functions here, don't add input('') statements here!
def reverse_string(string1):
    reversed_string = ""
    index = len(string1) - 1

    while index >= 0:
        reversed_string += string1[index]
        index -= 1
    return reversed_string

def main():
    while True:
        user_input = input("Enter a string (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            break

        if not user_input.replace(" ", "").isalpha():
            print("No numbers, only put a word thanks")
        else:
            reversed_result = reverse_string(user_input)
            print("Reversed:", reversed_result)
