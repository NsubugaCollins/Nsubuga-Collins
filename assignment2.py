while True:
    try:
        # Ask user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Try dividing them
        result = num1 / num2

    except ValueError:
        # Handles non-numeric input
        print("Invalid input! Please enter numeric values.")

    except ZeroDivisionError:
        # Handles division by zero
        print("Cannot divide by zero. Try again.")

    else:
        # Runs only if no exception occurs
        print(f"Result: {num1} / {num2} = {result}")
        break  # Exit the loop after successful division
