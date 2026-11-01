#list of students 

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]




#Loop through list and track highest score 
    
highest_score = 0 
highest_scorer = ""

for student in students:
    score = student["score"]

    if score > highest_score:
        highest_score = score
        highest_scorer = student["name"]


#Calculate the Class avg
total = 0 

#set to collect subjects 
subjects_offered = set()

high_scorers = []

for student in students: 
    score = student["score"]
    name = student["name"]

    if score > 75: 
        high_scorers.append(name)


for student in students: 
    total += student["score"]     
# Add Class Subjects
    subject = student["subject"]
    subjects_offered.add(subject)

average = total / len(students) 


print(f"Top scorer: {highest_scorer} ({highest_score})")
print(f"Class average: {average}")  
print(f"Subjects offered: {subjects_offered} ")
print(f"High scorers: {high_scorers} ")