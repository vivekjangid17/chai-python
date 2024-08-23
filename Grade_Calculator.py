# 3. Grade Calculator
    # - Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69),      F(below 60).
    
# ------ My Code ------

score = int(input("Enter your score: "))

if score > 100:
    print("Please enter a valid score.")
    exit()
if score >=90:
    print("Grade A")
elif score >=80:
    print("Grade B")
elif score >=70:
    print("Grade C")
elif score >=60:
    print("Grade D")
elif score <60:
    print("Grade F")
    