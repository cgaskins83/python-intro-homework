numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    lowest_num = numbers[0]
    for num in numbers:
        if lowest_num > num:
            lowest_num = num
    return lowest_num          

def find_max(numbers):
    highest_num = numbers[0]
    for num in numbers:
        if highest_num < num:
            highest_num = num
    return highest_num    

def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

def bubble_sort(numbers):
    new_list = []
    for num in numbers:
        new_list.append(num)
    
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(new_list) - 1):
            if new_list[i] > new_list[i + 1]:
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
                swapped = True
    return new_list

def show_menu():
    menu_options = [ 
    "==== Number Cruncher ===",
    "1. Find minimum",
    "2. Find maximum", 
    "3. Search for a number",
    "4. Sort the list", 
    "5. Quit" 
]

    for options in menu_options:
        print(options)
    
    return int(input("Select a number 1-4 or Select 5 to Quit: ")) 

def main():
    while True:
        user_choice = show_menu()

        if user_choice == 1:
            answer = find_min(numbers)
            print(f"The min number in this list is: {answer}")   
        elif user_choice == 2:
            answer2 = find_max(numbers)
            print(f"The max number in this list is: {answer2}")
        elif user_choice == 3:
                num_search = int(input("Enter a number you would like to search for: "))
                results = search(numbers, num_search)
                if results != -1:
                    print(f"Your number {num_search} has been found in the list at index: {results}! ")
                else:   
                    print(f"Your number {num_search} has not been found in this list! ")  
        elif user_choice == 4:
            reordered_list = (bubble_sort(numbers))
            print(f"Here is your sorted list: {reordered_list}! ")
        else: 
            print("Quitting")
          


main()
    