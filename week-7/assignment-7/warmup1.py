with open('data/notes.txt', 'r') as file: 
    line_count = 1  
    for line in file: 
        print(f"Line {line_count}:",line.strip())
        line_count += 1 