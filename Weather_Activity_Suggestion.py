# 5. Weather Activity Suggestion
#     - Suggest an activity based on the weather (eg. Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowaman).

import random

weather_list = ["sunny", "rainy", "snowy"]
weather = random.choice(weather_list)
print(weather)

if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")