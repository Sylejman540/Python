from module_5.global_keyword import message

greeting = "Hello"
name = "Sylejman"

def greet():
    global greeting
    greeting = "Goodbye"
    name = "Alice"
    message = f"{greeting}, {name}!"
    print(message)

greet()