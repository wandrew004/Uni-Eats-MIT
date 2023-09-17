
import random



def find_combinations_within_margin(foods, target_calories, margin):
    # Sort the list of foods by their calorie values
    
    foods.sort(key=lambda x: x.calories)

    # Initialize a list to store valid combinations
    valid_combinations = []
    random_combination = []
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
    for i in range(3):
        random_combination = random.choice(valid_combinations)
    return random_combination

# Example usage:
# foods = import_food()
# target_calories = stored_data
# margin = 100  # Adjust the margin as needed
# x = 3
# valid_combinations = find_combinations_within_margin(foods, target_calories, margin)
# for i in range(x):
#   random_combination = random.choice(valid_combinations)
#   print(random_combination)


# keep_alive()