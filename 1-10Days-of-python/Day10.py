#Function with Outputs
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("RohIth","ITagi"))
#Multiple return values
def format_name(f_name, l_name):
    if f_name=="" or l_name=="":
        return "you have to give valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_name = format_name(input("What is your frist name"),input("What is your last name"))

print(formatted_name)

""" Write a program that returns True or False whether if a given year is a leap year.A normal year has 365 days, leap years have 366, with aWn extra day in February. This is how you work out whether if a particular year is a leap year. on every year that is divisible by 4 with no remainder
 except every year that is evenly divisible by 100 with no remainder  unless the year is also divisible by 400 with no remainder"""
  
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
#Doc String
def my_function(num):
    """Multiplies a number by itself."""
    return num * num
#Calculator program using def function
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
