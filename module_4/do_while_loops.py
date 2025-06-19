while True:
    user_input = input("Enter a positive number: ")
    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break

    print("Invalid input, please try again.")
    print("You have entered a postive number: ", number)
