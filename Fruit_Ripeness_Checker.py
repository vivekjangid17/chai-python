# 4. Fruit Ripeness Checker
    # - Determine if a fruit is ripe, overripe, or unique based on its color. (eg. Banana: green: unripe, Yellow: ripe, Brown: Overripe).abs
    
import random

fruit = "Banana"

if fruit == "Banana":
    color = ["green","yellow","brown"]
    col1 = random.choice(color)
    print(col1)

    if col1 == "green":
        print("The fruit is unripe.")
    elif col1 == "yellow":
        print("The fruit is ripe.")
    if col1 == "brown":
        print("The fruit is overripe.")