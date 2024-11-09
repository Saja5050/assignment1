# Function to display the main menu options
def display_menu():
    print("\nSelect an operation:")
    print("1. Palindrome Check")
    print("2. Lowercase Check")
    print("3. Digit Check")
    print("4. Length Check")
    print("5. Empty Check")
    print("6. Exit")

# Function to check if a given string is a palindrome
def is_palindrome(input_str):
    return input_str == input_str[::-1]  # Checks if the string reads the same forwards and backwards

# Function to check if all characters in a string are lowercase
def is_lowercase(input_str):
    return input_str.islower()  # Returns True if all characters are lowercase

# Function to check if a string contains only digits
def is_digit(input_str):
    return input_str.isdigit()  # Returns True if all characters are digits

# Function to check if the length of the input exceeds a predefined threshold
def is_length_exceed(input_str, threshold=5):
    return len(input_str) > threshold  # Adjust threshold as needed (default is 5)

# Function to check if the input string is empty
def is_empty(input_str):
    return len(input_str) == 0  # Returns True if the string is empty

# Main function to run the application
def main():
    while True:
        display_menu()  # Show the menu options to the user

        # Error handling: Prompt user for choice and handle non-integer input
        try:
            choice = int(input("Enter the number of your choice: "))
        except ValueError:
            # Inform the user and loop back to display the menu again
            print("Invalid input. Please enter a number between 1 and 6.")
            continue  # Restart the loop if input is invalid

        # Immediately check if the choice is within the valid range
        if choice < 1 or choice > 6:
            # Show an error message and go back to the menu
            print("Invalid choice. Please select a number between 1 and 6.")
            continue  # Restart the loop

        # Execution: Exit the program if the user chooses option 6
        if choice == 6:
            print("Exiting the application. Goodbye!")
            break

        # Prompt the user for input string only if the choice is valid
        input_str = input("Enter an input: ")

        # Execute the corresponding operation based on user choice
        if choice == 1:
            # Palindrome Check
            print("Palindrome Check:", "Yes" if is_palindrome(input_str) else "No")
        elif choice == 2:
            # Lowercase Check
            print("Lowercase Check:", "Yes" if is_lowercase(input_str) else "No")
        elif choice == 3:
            # Digit Check
            print("Digit Check:", "Yes" if is_digit(input_str) else "No")
        elif choice == 4:
            # Length Check with a predefined threshold (e.g., 5 characters)
            threshold = 5  # Change this value to adjust the length limit
            print("Length Exceeds Threshold:", "Yes" if is_length_exceed(input_str, threshold) else "No")
        elif choice == 5:
            # Empty Check
            print("Empty Check:", "Yes" if is_empty(input_str) else "No")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
