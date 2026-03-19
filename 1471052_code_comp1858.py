# TASK 1.2

#opens worldregions_ingredients.csv in default read mode
recipes = open("worldregions_ingredients.csv")
# this will be a dictionary of dictionaries

print("TASK 1.2: worldregions_ingredients dataset into a dictionary\n") 

recipesDict = {}

# the header will be used to identify the keys that will be in dictionary saved to recipesDict
header = recipes.readline()
header_split = header.split(",")

# count is used to limit the iterations of the loop, as there are thousands of records in the file
count  = 0
for line in recipes.readlines():
    line_split = line.split(",")
    dict = {}
    # the header will contain the maximum amount of columns, as not all recipes have the same amount of ingredients
    for part in range (0, len(line_split)):
        # a new key-value pair is inserted for each field in the header
        # as long as there is a value in that cell
        # we don't want to add an empty key-value pair to our dictionary
        if (line_split[part] != '' and line_split[part] != '\n') :
            dict.update({header_split[part]: line_split[part]})
    # the dictionary is added to recipesDict
    # as it needs a unique key, the incrementing recipe number is generated using count + 1
    # so the recipes start from recipe 1 to recipe n
    count = count + 1
    recipesDict.update({"recipe " + str(count): dict})

'''
# this shows how the user could choose a specific recipe from the dictionary
print(recipesDict["recipe 1"])

print("")

count = 0
# to show proof of this working 10 rows from worldregions_ingredients.csv will be printed to the terminal
for recipe in recipesDict.items():
    print(recipe)
    count += 1
    if (count >= 10):
        break
'''
    

recipes.close()

print("")

# What structure would be appropriate for Flavour compounds"?
# I believe flavourcompounds.csv would be best represented as an adjacenecy list
# Where ingredients have relationships with other ingredients, and each relationship has a flavour components number. 
# This could be stored as an undirected, weighted list where the weight is the favour component number. 

''' example using the first 10 rows of data
# Ingredient 1      Ingredient 2	Number of shared flavour compounds
black_sesame_seed	rose_wine	    3
fennel	            wild_berry	    5
comte_cheese	    grape	        57
nira	            raw_beef	    1
corn_mint_oil	    parsnip_fruit	2
soybean	            vegetable_oil	1
bell_pepper	        naranjilla	    5
chervil	            crayfish	    1
corn_mint	        cream_cheese	3
european_cranberry	thai_pepper	    12
'''

'''NOTE: this is an implemented adjacency list on flavourcompounds.csv
The working version includes checking the list for when ingredients are repeated eg: 
row 25: kaffir_lime -> kohlrabi 6 and row 36: kaffir_lime -> raw_potato 16
and adding these relationships to the same key
'''
print("TASK 1.2: flavourcompounds dataset into an adjacency list\n") 

flavours = open("flavourcompounds.csv", "r")
# skips header line
next(flavours)
# this will be a dictionary of dictionaries
flavours_adj_list = {}

for line in flavours.readlines():
    line_split = line.split(",")
    # checks that the key exists
    # if it doesnt the value can be added
    # if it does then the current values it has needs to kept while adding the new flavour + weighting
    if (flavours_adj_list.get(line_split[0]) is None):
        flavours_adj_list[line_split[0]] = [(line_split[1], line_split[2].rstrip())]
    else:
        flavours_adj_list.get(line_split[0]).append((line_split[1], line_split[2].rstrip()))

flavours.close()

'''
# this shows how the user could choose a specific recipe from the dictionary
print(flavours_adj_list["black_sesame_seed"])
print("")

count = 0
# to show proof of this working 5 rows from the adjacency list will be printed
for pairing in flavours_adj_list.items():
    print(pairing)
    print("")
    count += 1
    if (count >= 2):
        break

'''

print("")

# TASK 1.3
# enter these ingredients when prompted to receive 4 recipes from the algorithm
# this allows enough recipes for the algorithms to be tested while not becoming confusing to read
# ['chicken', 'black pepper', 'sesame oil', 'olive oil', 'rice', 'green tea', 'butter', 'flour', 'eggs', 'cinnamon', 'sugar', 'honey'] => 4

print("TASK 1.3: finding the best matching recipe in worldregions_ingredients\n") 

user_ingredients = []
cont = True

ingredient = input("What ingredient would you like in your recipe? Enter one: ")
user_ingredients.append(ingredient)
choice = input("Would you like to continue and add another ingredient? Enter Y/N: ")

while (cont is True):
    if (choice == "Y"):
        ingredient = input("What ingredient would you like in your recipe? Enter one: ")
        user_ingredients.append(ingredient)
        choice = input("Would you like to continue and add another ingredient? Enter Y/N: ")
    if (choice == "N"):
        cont = False
    elif (choice != "Y"):
        print("You have not chosen correctly. Please choose if you would like to add another ingredient or not.")
        choice = input("Would you like to continue? Enter Y/N: ")

print(user_ingredients)
print("")

ingredients = []

# this takes the from recipesDict the values of the values of its keys
# eg: {recipe 1: {world_region: Africa, ingredient 1: cumin, ...}}
# becomes {world_region: Africa, ingredients 1: cumin, ... }
# becomes Africa, cumin, ...

for recipe in recipesDict.values():
    recipe_ing = []
    for parts in recipe.values():
        recipe_ing.append(parts)
    ingredients.append(recipe_ing)

'''
As there are thousands of recipes in the file 
I want to limit the recipes included in the returned final list of matching recipes
As it would not make sense of have a list of 10 ingredients and allow recipes that only match two of them and this would be too many recipes
But then to have a list of 2 ingredients and not allow recipes that only match one of them would not make sense

I will only include recipes that have at least a 50% match with the user provided ingredient list

This will result in a returned list of recipes that reasonably follows the set criteria 
and doesnt overwhelm the user by presenting thousands of recipes
'''

ingredient_match = []

match_limit = round(len(user_ingredients)//2)
print("The minimum number of matching ingredients a recipe must contain is " + str(match_limit) + ".\n")

for recipe in ingredients:
    match_count = 0
    for user_ingredient in user_ingredients:
        if (" " in user_ingredient):
            user_ingredient = user_ingredient.replace(" ","_")
        if (user_ingredient in recipe):
            match_count += 1
    if (match_count >= match_limit):
        ingredient_match.append([recipe, match_count])

ingredient_match.sort(key = lambda x: x[1], reverse=True)

print("These are your recipes that contain at least half the ingredients you want to use:")
print(ingredient_match[0])

print("These are the total number of recipes found:")
print(len(ingredient_match))

print("")

# TASK 1.4

print("TASK 1.4: finding the recipe ingredient_match\n") 

# from selected recipes takes only the ingredients
if (len(ingredient_match) > 0):
    recipe_ingredients = [] 

    for recipe in ingredient_match:
        input = recipe[0][1:] 
        recipe_ingredients.append(input)

    # take user ingredients and find all combinations
    from itertools import combinations

    scores = []
    i = 0

    for recipe in recipe_ingredients:
        pairs = list(combinations(recipe, 2))
        recipe_score = [i]
        score = 0
        for pair in pairs:
            match = flavours_adj_list.get(pair[0])
            # avoids case where user enters an ingredient that is not in the flavour datasheet
            if (match != None):
                for flavour_pair in match:
                    if (pair[1] == flavour_pair[0]):
                        score = score + int(flavour_pair[1])
                        break 
        recipe_score.append(score)
        scores.append(recipe_score)
        i += 1
                
    scores.sort(key = lambda x: x[1], reverse=True)

    best_recipe = scores[0][0]

    print("This is the recipe with the highest flavour score.")
    print(ingredient_match[best_recipe]) 
    print("It has total flavour score of " + str(scores[0][1]) + ".")
    print("It contains " + str(ingredient_match[best_recipe][1]) + " ingredients from the ingredients you requested.")

else:
    print("As there are no recipies with at least a reasonable match I cannot find you the recipe with the best flavour score.")
