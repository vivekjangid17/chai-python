# 1. Age Group Categorization
#    - Classify a person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+).

age = int(input("Enter Your Age: "))
if(age < 13):
    print("You are a Child.")
elif(age >= 13 and age <= 19):
    print("You are a Teenager.")
elif(age >= 20 and age <= 59):
    print("Your are an Adult.")
else:
    print("You are a Senior Citizen.")
    