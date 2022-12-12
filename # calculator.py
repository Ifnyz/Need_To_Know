# Define the main function
def main():
    # Prompt the user to enter an arithmetic expression
    expression = input('Enter an arithmetic expression (e.g. 2 + 3): ')

    # Evaluate the expression and print the result
    result = eval(expression)
    print(f'The result is: {result}')

# Call the main function
main()