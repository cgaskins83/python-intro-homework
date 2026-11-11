"Use a while loop that repeatedly asks the user to enter a positive integer. If the user enters anything that isn't a positive integer, print a message and ask again. Once valid input is received, print it and stop. The example session below shows the format — your inputs and message wording might differ:"

while True:
    user_input = input("Enter a positive integer: ")

    try: 
        value = int(user_input)

        if value > 0: 
            print(f"You entered {value} a positive integer. ")
            break
        elif value < 0: 
            print("This is not a valid entry. Try again. ") 

    except TypeError: 
        print("This is not a valid entry. Try again. ")
    


            