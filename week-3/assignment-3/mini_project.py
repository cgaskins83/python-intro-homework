day = input("What day of the week is it? ").lower()
time =input("What time of day is it? Morning, Afternoon, or Evening? ").lower()

if day == "monday"  and time == "morning":
    print("It's Monday morning, lets have breakfast.")
elif day == "monday" and time == "afternoon":
    print("Suggestion: lets have lunch.")
elif day == "monday" and time == "evening":
    print("Sugguestion: lets have dinner.")
elif day == "friday"  and time == "morning":
    print("Suggestion: lets rides bikes in the park.")
elif day == "friday" and time == "afternoon":
    print("Suggestion: lets go swimming in the pool.")
elif day == "friday" and time == "evening":
    print("Suggestion: lets go to the movies.")
elif day == "sunday" and time == "morning":
    print("Suggestion: lets go to the gym.")
elif day == "sunday" and time == "afternoon":
    print("Suggestion: lets go for a swim in the pool")
elif day == "sunday" and time == "evening":
    print("Suggestion: lets have a family dinner and then play with the dogs.")
else:
    if day != "monday" and day != "friday" and day != "sunday":
        print("Sorry, I don't recognize that day. Try: Monday, Friday, Sunday")
    else:
        print("Sorry, I don't recognize that time. Try: Morning, Afternoon, Evening")
