
a = int(input("What would you like your first number to be?"))
b = int(input("What would you like your second number to be?"))

#addition
def addition(a,b):
    c=a+b
    return c
def subtraction(a,b):
    c=a-b
    return c
def multiplication(a,b):
    c=a*b
    return c
def division_result(a,b):
    c=a/b
    return c
def ratio(a,b,format='Decimal'):
    if format == 'Decimal':
        c = f"The ratio of {a} to {b} is {a/b}:1"
    if format == 'Percentage':
        c = f"{a} is {a/addition(a,b) * 100}% of {b}"
    return c