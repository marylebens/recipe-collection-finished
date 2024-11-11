class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {
            "ingredients": ingredients,
            "instructions": instructions
        }

    def get_recipe(self, name):
        return self.recipes.get(name, "Recipe not found")


# Add your favorite recipe here!
book = RecipeBook()
book.add_recipe(
    "Midnight Ramen",
    ["instant ramen", "egg", "green onions", "hot sauce"],
    "1. Boil water\n2. Cook noodles\n3. Add toppings"
)