# 2. Movie Ticket Pricing
   # - Movie tickets are priced based on age: $12 for adults (18 and over) , $8 for children.      Everyone gets a $2 discount on Wednesday.

# ------ My Code ------
   
age = int(input("Enter a age: "))
day = input("Enter day: ")

# if age >= 18:
#     price = 12
#     if day=="Wednesday":
#         price = price - 2
#         print(price)
#     else:
#         print(price)
# else:
#     price = 8
#     if day=="Wednesday":
#         price = price - 2
#         print(price)
#     else:
#         print(price)
        
# ------- Video's solution ---------

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2
    
print("Ticket price for you is $",price)

