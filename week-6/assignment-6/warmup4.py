def is_valid_score(score): 
    if score >= 0 and score <= 100: 
        return True
    else: 
        return False

user_score = int(input("Enter your test score: ")) 

if is_valid_score(user_score):
    print("Valid score. ")
else:
    print("Invalid Score - must be between 0 and 100.")    