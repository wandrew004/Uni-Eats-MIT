class food:
  def __init__(self, name, calories, fat, carbs, sugar, protein):
    self.name = name
    self.calories = calories
    self.fat = fat
    self.carbs = carbs
    self.sugar = sugar
    self.protein = protein
  def __str__(self):
    return self.name + " - Calories : " + str(self.calories) + ", Fat: " + str(self.fat) + ", Carbs: " + str(self.carbs) + ", Sugar: " + str(self.sugar) + ", Protein: " + str(self.protein) + "."