a = int(input("Please enter first number:\n"))
b = int(input("Please enter second number:\n"))
operand = input("Please enter an operand from the list: '+', '-', '/', '*'\n")

if operand == '+':
    print(a+b)
elif operand == '-':
    print(a-b)
elif operand == '/':
    print(a/b)
elif operand == '*':
    print(a*b)
else:
    print("Something is not yes, try again!!11!!")
