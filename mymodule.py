#mymodule for CI/CD 

def add(a,b):
    return a + b


def divide(a,b):
    return a / b


def subtract(a,b):
    return a - b


def multiply(a,b):
    return a * b

  
def sqrt(a):
    if a < 0:
        raise ValueError("Cannot compute square root of negative number")
    return a ** 0.5