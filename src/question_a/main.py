
question_a import reverse_string 

def main():
    while True:
        user_input = input("Enter a string (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            break
        
        reversed_result = question_a.reverse_string(user_input)
        print(f"Reversed string: {reversed_result}")

if __name__ == "__main__":
    main()




