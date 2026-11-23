import os 
import csv 

from datetime import datetime 

path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(path):
    print("Error file not found")
else: 
    food_expenses = []
    total = 0.0 
    with open(path, 'r') as file:
        reader = csv.DictReader(file) 
        for row in reader: 
            row['amount'] = float(row['amount'])
            if row['category'] == "Food": 
               food_expenses.append(row)
               total += row["amount"]
    today = datetime.now()
    with open("food_report.txt", "w") as file:
        file.write(f"Food Expense Report - generated {today.strftime('%B %d, %Y')} \n")
    
        for food in food_expenses:
            file.write(f"{food['date']}: ${food['amount']:.2f} \n")

        file.write(f"Total: ${total:.2f} \n")    