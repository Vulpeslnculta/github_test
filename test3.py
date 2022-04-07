import math


def addition(args):
    """
    This function adds two numbers
    """
    return args[0] + args[1]


def subtraction(args):
    """
    This function subtracts two numbers
    """
    return args[0] - args[1]


def multiplication(args):
    """
    This function multiplies two numbers
    """
    return args[0] * args[1]


def division(args):
    """
    This function divides two numbers
    """
    return args[0] / args[1]


def modulo(args):
    """
    This function returns the remainder of two numbers
    """
    return args[0] % args[1]


def power(args):
    """
    This function returns the first number raised to the power of the second number
    """
    return args[0] ** args[1]


def square_root(args):
    """
    This function returns the square root of a number
    """
    return args[0] ** 0.5


def square(args):
    """
    This function returns the square of a number
    """
    return args[0] ** 2


def cube(args):
    """
    This function returns the cube of a number
    """
    return args[0] ** 3


def absolute_value(args):
    """
    This function returns the absolute value of a number
    """
    return abs(args[0])


def factorial(args):
    """
    This function returns the factorial of a number
    """
    if args[0] == 0:
        return 1
    else:
        return args[0] * factorial(args[0] - 1)


def sin(args):
    """
    This function returns the sine of a number
    """
    return math.sin(args[0])


def cos(args):
    """
    This function returns the cosine of a number
    """
    return math.cos(args[0])


def tan(args):
    """
    This function returns the tangent of a number
    """
    return math.tan(args[0])


def asin(args):
    """
    This function returns the arcsine of a number
    """
    return math.asin(args[0])


def acos(args):
    """
    This function returns the arccosine of a number
    """
    return math.acos(args[0])


def atan(args):
    """
    This function returns the arctangent of a number
    """
    return math.atan(args[0])


def log(args):
    """
    This function returns the logarithm of a number
    """
    return math.log(args[0])


def log10(args):
    """
    This function returns the logarithm of a number
    """
    return math.log10(args[0])


def exp(args):
    """
    This function returns the exponential of a number
    """
    return math.exp(args[0])


def floor(args):
    """
    This function returns the floor of a number
    """
    return math.floor(args[0])


def ceil(args):
    """
    This function returns the ceiling of a number
    """
    return math.ceil(args[0])


def main(args):
    """
    This function is the main function of the program
    """
    print("Welcome to the calculator!")
    print("Enter the first number:")
    num1 = float(input())
    print("Enter the second number:")
    num2 = float(input())
    print("Enter the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Power")
    print("7. Square Root")
    print("8. Square")
    print("9. Cube")
    print("10. Absolute Value")
    print("11. Factorial")
    print("12. Sine")
    print("13. Cosine")
    print("14. Tangent")
    print("15. Arcsine")
    print("16. Arccosine")
    print("17. Arctangent")
    print("18. Logarithm")
    print("19. Logarithm 10")
    print("20. Exponential")
    print("21. Floor")
    print("22. Ceiling")
    print("23. Quit")
    operation = int(input())
    if operation == 1:
        print(num1, "+", num2, "=", addition([num1, num2]))
    elif operation == 2:
        print(num1, "-", num2, "=", subtraction([num1, num2]))
    elif operation == 3:
        print(num1, "*", num2, "=", multiplication([num1, num2]))
    elif operation == 4:
        print(num1, "/", num2, "=", division([num1, num2]))
    elif operation == 5:
        print(num1, "%", num2, "=", modulo([num1, num2]))
    elif operation == 6:
        print(num1, "^", num2, "=", power([num1, num2]))
    elif operation == 7:
        print(num1, "^", 0.5, "=", square_root([num1]))
    elif operation == 8:
        print(num1, "^", 2, "=", square([num1]))
    elif operation == 9:
        print(num1, "^", 3, "=", cube([num1]))
    elif operation == 10:
        print(num1, "=", absolute_value([num1]))
    elif operation == 11:
        print(num1, "=", factorial([num1]))
    elif operation == 12:
        print(num1, "=", sin([num1]))
    elif operation == 13:
        print(num1, "=", cos([num1]))
    elif operation == 14:
        print(num1, "=", tan([num1]))
    elif operation == 15:
        print(num1, "=", asin([num1]))
    elif operation == 16:
        print(num1, "=", acos([num1]))
    elif operation == 17:
        print(num1, "=", atan([num1]))
    elif operation == 18:
        print(num1, "=", log([num1]))
    elif operation == 19:
        print(num1, "=", log10([num1]))
    elif operation == 20:
        print(num1, "=", exp([num1]))
    elif operation == 21:
        print(num1, "=", floor([num1]))
    elif operation == 22:
        print(num1, "=", ceil([num1]))
    elif operation == 23:
        print("Goodbye!")
        return
    else:
        print("Invalid operation!")


main([])
