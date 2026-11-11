numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

menu_options = [ 
    "==== Number Cruncher ===",
    "1. Find minimum",
    "2. Find maximum", 
    "3. Search for a number",
    "4. Sort the list", 
    "5. Quit" 
]

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
    return data

while True:
    for options in menu_options:
        print(options)
    
    user_input = int(input("Select a number 1-4 or Select 5 to Quit: ")) 
    if user_input == 1: 
        lowest_num = numbers[0]
        for num in numbers:
            if lowest_num > num: 
                lowest_num = num
        print(f" The min number in this list is: {lowest_num}" )

    elif user_input == 2: 
        highest_num = numbers[0]
        for num in numbers:
            if highest_num < num:
                highest_num = num
        print(f"The max number in this list is: {highest_num}" )         
        
    elif user_input == 3:
        num_search = int(input("Enter a number you would like to search for: "))
        results = linear_search(numbers, num_search)
        if results != -1:
            print(f"Your number {num_search} has been found in the list at index: {results}! ")
        else:
            print(f"Your number {num_search} has not been found in this list! ")

    elif user_input == 4:
        reordered_list = (bubble_sort(numbers))
        print(f"Here is your sorted list: {reordered_list}! ")
    else: 
        print("Quitting")
        break    
    