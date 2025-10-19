# Get first number (with error handling)
while True:
    try:
        num1 = float(input("Pick first your number: "))
        break
    except ValueError:
        print("Thats not a number! Try again.")

# Get operator (validate it)
while True:
    operator = input("Pick your operator, choose from + - * /: ")
    if operator in['+', '-', '*', '/']:
        break
    else :
        print("Thats not an operator! Try again.")

# Get second number (with error handling)
while True:
    try:    
        num2 = float(input("Pick your second number: "))
        break
    except ValueError:
        print("Thats not a number! Try again.")

# Perform first calculation
if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)

# --- Main loop to keep calculating with the result ---
while True:
    # Ask for a new operator or exit
    operator = input("Pick your operator, or type 'exit' to leave, choose from + - * /: ")
    if operator == 'exit': # stop the loop if user types exit
        print("Goodbye")
        break
    if operator not in ['+', '-', '*', '/']:
        print("Invalid operator, try again!")
        continue # go back to top of while loop    
    while True: 
        try:
            num2 = float(input("Pick your second number: "))
            break # valid → exit number input loop
        except ValueError: 
            print("Thats not a number!") # invalid → repeat
    
     # Protect against division by zero
    if operator == '/' and num2 == 0:
        print("You can't divide by zero! Try again.")
        continue  # skip calculation and restart loop
    
    if operator == '+':
        result = result + num2
        print(result)
    elif operator == '-':
        result = result - num2
        print(result)
    elif operator == '*':
        result = result * num2
        print(result)
    elif operator == '/':
        result = result / num2
        print(result)
    
