from keep_alive import keep_alive
import random

class food:
  def __init__(self, name, serving, calories):
    self.name = name
    self.serving = serving
    self.calories = calories
  def __str__(self):
    return self.name + " - Serving size: " + self.serving + ", Calories : " + str(self.calories) + "."
f1 = food("Creamy Tomato Basil Soup", "8fl oz", 200)
f2 = food("Moroccan Chickpea Soup", "6fl oz", 100)
f3 = food("Classic Cheese Pizza", "1/8cut", 250)
f4 = food("Middle Eastern Chicken Wrap", "1 each", 480)
f5 = food("Korean Beef Taco", "1 each", 200)
f6 = food("Korean Mushroom Sandwich", "1serving", 360)
f7 = food("White Pizza", "1/8 cut", 470)
f8 = food("Rotisserie Whole Chicken", "1piece", 430)
f9 = food("Roasted Veggie Panini", "1sandwich", 400)
f10 = food("Vegetable Kohapuri", "8fl oz", 400)
f11 = food("Pepperoni Flatbread", "1/6 cut", 340)
f12 = food("Fresh Pasta", "1/2 cup", 310)
f13 = food("VEGAN APPLE CRISP", "1each", 280)
f14 = food("Turkey Burger Patty ", "1each", 190)
f15 = food("Pepperoni Flatbread", "1/6 cut", 340)
f16 = food("Vegan Cheese Pizza", "1/8 cut", 260)
f17 = food("Sargent Choice Chicken Stir-Fry with Mango Sauce", "1each", 200)
f18 = food("Chocolate Chip Cookie", "1each", 130)
f19 = food("Grilled Herbed Orange Chicken", "1each", 160)
f20 = food("Gardenburger Black Bean Burger", "1each", 110)
f21 = food("Chicken Tinga", "3oz", 160)


def find_combinations_within_margin(foods, target_calories, margin):
    # Sort the list of foods by their calorie values
    foods.sort(key=lambda x: x.calories)

    # Initialize a list to store valid combinations
    valid_combinations = []

    n = len(foods)

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            # Calculate the total calories for the current triplet
            total_calories = foods[i].calories + foods[left].calories + foods[right].calories

            # Calculate the difference from the target calories
            difference = abs(total_calories - target_calories)

            # If the difference is within the margin, add the combination to the list
            if difference <= margin:
                valid_combinations.append([foods[i].name, foods[left].name, foods[right].name])

            if total_calories < target_calories:
                left += 1
            else:
                right -= 1

    return valid_combinations

# Example usage:
foods = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14]
target_calories = 700
margin = 100  # Adjust the margin as needed

valid_combinations = find_combinations_within_margin(foods, target_calories, margin)

random_combination = random.choice(valid_combinations)

print(random_combination)


keep_alive()