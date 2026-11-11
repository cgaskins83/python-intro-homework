#Start with a hardcoded list of names. Ask the user to enter a name. Loop through the list and print whether the name was found and at what index — or a not-found message if it isn't in the list. The examples below show the format for two different searches — your names, index, and message wording might differ

names = ["Teresa", "Mark", "Devin", "Matt", "Duncan", "Jessica"]
user_input = input("Enter a name to search: ")
index = 0
found = False
for i in range(len(names)):
    if names[i] == user_input: 
        found = True
        break
if found:
    print(f"Found {user_input} at index: {i} ")
else:
    print(f"{user_input} was not found on the list")    
    

    