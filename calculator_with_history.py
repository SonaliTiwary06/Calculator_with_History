# File to store calculation history
HISTORY_FILE="history.txt"

def show_history():
                                         # Show the calculation history from history.txt.
                                         # Opens file in append+read mode (a+) so that:
                                         # - If the file doesn't exist, it will be created.
                                         # - Can read the content immediately after opening.
    file=open(HISTORY_FILE, "a+")
    lines=file.readlines()
    if len(lines) ==0:
        print("No history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()       

def clear_history():
                                          # Clear all stored calculations.
                                          # Opens file in write mode (w) which automatically deletes old content.
    file=open(HISTORY_FILE, "w")
    file.close()
    print("History cleared")

def save_to_history(equation,result):
                                         # Save the given equation and result into the history file.
    file=open(HISTORY_FILE,"a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
                                         # Parse user input, perform calculation, and save result to history.
    parts=user_input.split()             ## Split input into 3 parts: number, operator, number
    if len(parts) != 3:
        print("Invalid input, Use format: number operator number (e.g. 3 + 7)")
        return
    
    num1= float(parts[0])                 ## Convert numbers from string to float
    op=parts[1]
    num2= float(parts[2])

# Perform calculation based on operator
    if op == "+":
        result= num1 + num2
    elif op == "-":
        result= num1 - num2
    elif op == "*":
        result= num1 * num2 
    elif op == "/":
        if num2==0:
            print("cannot divide by zero")
            return
        result= num1 / num2
    else:
        print("Invalid operator. Use only + - * /")
        return
    
    # If result is a whole number (e.g., 8.0), convert to int (8)
    if int(result) == result:
        result=int(result)
        # Show result to user
        print("Result:" , result)
        # Save the calculation to history
        save_to_history(user_input,result)

def main():
                                            # Main program loop for the calculator.
                                            # User can:
                                            # - Perform calculations
                                            # - View history (type 'history')
                                            # - Clear history (type 'clear')
                                            # - Exit program (type 'exit')
    print("---------Simple calculator (type history , clear , exit)")
    while True:
        user_input=input("Enter the calculation (+ _ * /) or command (history , clear , exit)")
        if user_input=="exit":
            print("Good bye")
            break
        elif user_input== "history":
            show_history()
        elif user_input== "clear":
            clear_history()
        else:
            calculate(user_input)

main()                    # Start the program
