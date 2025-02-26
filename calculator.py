import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)


if __name__ == "__main__":
    print("Square root of 9:", square_root(9))
    print("Factorial of 5:", factorial(5))
    print("Natural log of 10:", natural_log(10))
    print("Power of 2^3:", power(2, 3))
