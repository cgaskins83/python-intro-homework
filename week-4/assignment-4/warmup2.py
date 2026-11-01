student = {
    "name": "Christen", 
    "grade": "Junior", 
    "subjects": ["Math", "Science", "P.E", "History", "Choir"]
}
#loops through key/value pair
for key in student.items():
    print(key)

#Adding new key/value pair
student["graduated"] = False
print(student)