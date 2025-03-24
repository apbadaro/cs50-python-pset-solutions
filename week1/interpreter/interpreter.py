'''
Week 1 - Conditionals | Problem Set 1

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression
and then calculates and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user’s input will be formatted as x y z,
with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
'''


def main():

    expression = input("Expression: ")

    # Split the input into three parts: first number (x), operator (y), second number (z)
    x, y, z = expression.split()

    # Convert x and z to floats
    x = float(x)
    z = float(z)

    if y == "+":
        # ",1" will print a floating-point value formatted to one decimal place
        print(round(x + z, 1))
    elif y == "-":
        print(round(x - z, 1))
    elif y == "*":
        print(round(x * z, 1))
    elif y == "/":
        print(round(x / z, 1))


if __name__ == "__main__":
    main()

