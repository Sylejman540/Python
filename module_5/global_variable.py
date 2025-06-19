from pyexpat.errors import messages

greeting = "Hello"

def greet(name):
    message = f"{greeting}, {name}"
    print(message)

greet("Sylejman")