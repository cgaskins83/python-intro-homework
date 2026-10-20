user_age = int(input("What is your age? "))

if user_age <= 12:
    print("You are an Child.")
elif user_age >= 13 and user_age <= 17:
    print("You are a Teen.")
elif user_age >= 18 and user_age <= 64: 
    print("You are an Adult.")
else:
    print("You are a Senior.")