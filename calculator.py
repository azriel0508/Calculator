import art #Do not forget to download art.py

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {  # Dictionary for the operations
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def get_number(prompt): #Found this solution from stack overflow! (Allows the user to input if did not input a number)
    """Helper function to get a valid number from the user.""" #Docstring!!
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
          
def calculator():
    print(art.logo)

    # Start the first calculation
    num1 = get_number("What is the first number?: ")

    while True:
        # Print out available operations
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        # Check if the operation is valid
        if operation_symbol not in operations:
            print("Invalid operation. Please try again.")
            continue

        num2 = get_number("What is the next number?: ")

        # Perform the operation
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        check2 = True
        while check2:
            # Ask if user wants to continue or start a new calculation
            choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \nTo turn off the calculator, enter 'stop':\n")

            if choice == "y":
                num1 = answer  # Continue with the result as the next number
                check2 = False  # Exit inner loop to continue
            elif choice == "n":
                print("\n" * 20)  # Clear the screen
                calculator() #HOW DO I FIX RECURSION PROBLEM????
            elif choice == "stop":
                print("Turning off the calculator... Thank you!")
                check2 = False
                return  # Stop the program
            else:
                print("Invalid choice, please type 'y', 'n', or 'stop'.")
                check2 = True  # Keep asking until a valid choice is made

# Start the calculator
calculator()
