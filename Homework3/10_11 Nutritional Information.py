# Kaitlyn Sourignosack
# 1824497

class FoodItem:
    def __init__(self, name, fat, carbs, protein):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):
        if (name != 'None'):
            self.name = name
        else:
            self.name = name
        if (fat > 0.0):
            self.fat = fat
        else:
            self.fat = fat
        if (carbs > 0.0):
            self.carbs = carbs
        else:
            self.carbs = carbs
        if (protein > 0.0):
            self.protein = protein
        else:
            self.protein = protein

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        self.serving = num_servings
        self.calories = calories
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print('Number of calories for {:.2f}'.format(self.serving), 'serving(s): {:.2f}'.format(self.calories))


if __name__ == '__main__':

    c = 0
    attributes = []
    while c < 5:
        attributes.append(input())
        c += 1

    # Variables storing attributes from inputs
    name = attributes[0]
    fat = float(attributes[1])
    carbs = float(attributes[2])
    protein = float(attributes[3])
    servings = float(attributes[4])

    food = FoodItem()
    food.get_calories(servings)
    # printing
    food.print_info()

    print()

    food2 = FoodItem(name, fat, carbs, protein)
    food2.get_calories(servings)
    # printing
    food2.print_info()

