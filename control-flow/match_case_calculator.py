first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = first_number + second_number
    case '-':
        result = first_number - second_number
    case '*':
        result = first_number * second_number
    case '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Cannot divide by zero."
    case _:
        result = "Invalid operation."

print("The result is", result)
