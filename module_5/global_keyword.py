from pyexpat.errors import messages

greeting = "Hello"

def greet(name):
    global message
    message = f"{greeting}, {name}"
    print(message)

greet("Sylejman")

print(message)

message = f"{greeting}, student!"
print(message)