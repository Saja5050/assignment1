# Command-Line Application

## Overview
This project is a command-line application that allows users to execute various operations on their input. The application provides a menu with different options, allowing the user to choose an operation, input data for analysis, and view the result. It continues running until the user decides to exit.

## Exercise Description
Create a console application that enables users to insert commands for various operations. The program will display a menu, take user input, perform the chosen operation, and display the result. This loop continues until the user selects the exit option.

## Features
- **User Interaction**:
  - Display a menu of available operations.
  - Prompt the user to select an operation by entering a corresponding number.
  - Prompt the user to enter input for analysis.
- **Operations**:
  - **Palindrome Check**: Verify if the input reads the same forwards and backwards.
  - **Lowercase Check**: Confirm if all characters in the input string are lowercase.
  - **Digit Check**: Verify if all characters in the input are numeric digits.
  - **Length Check**: Check if the input exceeds a predefined length threshold.
  - **Empty Check**: Determine if the input is an empty string.
  - **Exit Program**: Allow the user to exit the application.
- **Execution**:
  - Perform the operation selected by the user.
  - Display the result of the operation.
  - Handle invalid selections by informing the user and prompting for a new choice.
  - Keep displaying the menu until the user selects to exit.
- **Error Handling**:
  - At least one error-handling mechanism is included to manage unexpected input.

## Requirements
1. **Python 3.x**

## Getting Started
1. Clone this repository or download the source code.
2. Open your terminal and navigate to the project directory.
3. Run the application:
   ```bash
   python app.py

