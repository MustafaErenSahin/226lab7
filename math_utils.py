def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("divisor can not be 0")

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

if __name__ == "__main__":
    print(add(12, 3))
    print(subtract(12, 3))
    print(multiply(12, 3))
    print(divide(12, 3))
    print(power(12, 3))
    print(mod(12, 3))
