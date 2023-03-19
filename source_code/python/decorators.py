def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")
    return wrapper


def adding_data_adition(func):
    def wrapper(*args):
        print(f"El resultado de la suma de los numeros {args} es: ")
        return func(*args)
    return wrapper


@announce
def hello():
    print("Hello, world!")

@adding_data_adition
def sum(*args):
    result = 0
    for i in args:
        result += i
    return result

hello()
resultado = sum(2,8)
print(resultado)


