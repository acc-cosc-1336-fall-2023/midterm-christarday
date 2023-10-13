from question_c import get_assessment_value, get_tax_assessed

while True:
        try:
            actual_value = float(input("Enter the actual value of the property (or 'quit' to exit): $"))
            if actual_value < 0:
                print("Invalid input. Please enter a non-negative numeric value.")
                continue
            if actual_value == 0:
                print("Assessment Value: $0.00")
                print("Property Tax: $0.00")
            else:
                assessment_value = get_assessment_value(actual_value)
                property_tax = get_tax_assessed(assessment_value)

                print(f"Assessment Value: ${assessment_value:.2f}")
                print(f"Property Tax: ${property_tax:.2f}")

        except ValueError:
            user_input = input("Invalid input. Please enter a numeric value (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break 