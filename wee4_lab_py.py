# task 2
# adjacencey list as dictionry
places = ["shop", "house1", "house2", "gym", "uni", "park"]
#each key has a list of values they are connected to
placesDict = {"shop": ["house1", "gym"], 
    "house1": ["uni", "house2", "gym"], 
    "house2": ["gym"], 
    "gym": ["shop", "house1"],
    "uni": ["house1", "park"],
    "park": ["house2"]
}

print(placesDict)
print("")

# task 3
'''
Mazda RX4	        21	    6	160	    110	    3.9	    2.62	16.46	0	1	4
Mazda RX4 Wag	    21	    6	160	    110	    3.9	    na		na		4   na  na
Datsun 710	        22.8	4	108	    93	    3.85	2.32	18.61	1	1	4
Hornet 4 Drive	    21.4	6	258	    110	    3.08	3.215	19.44	1	0	3
Hornet Sportabout	18.7	8	360	    175	    3.15	3.44	17.02	0	0	3
'''
# in this dictionary -1 has been chosen to indicate where there are missing values in the records
# this is because is it mot possible for these measurements to have the value -1, they must be 0 or positive
# therefore -1 as an indicator cannot be confused with a valid value for these measurements of the cars

# for this file a dictionary where the key is the car name and the values are its specification measurements
# it could have been done as a list of dictionaries where all dictionaries had the same keys (name, gears, engine type, etc)
# these would be taken from the header from week 1's lab task
# this was not chosen as there is no header in the given cars.csv
carsDict = {"Mazda RX4": [21, 6, 160, 110, 3.9, 2.62, 16.46, 0, 1, 4], 
    "Mazda RX4 Wag": [21, 6, 160, 110, 3.9, -1, -1, 4, -1, -1], 
    "Datsun 710": [22.8, 4, 108, 93, 3.8, 2.32, 18.61, 1, 1, 4],
    "Hornet 4 Drive": [21.4, 6, 258, 110, 3.08, 3.215, 19.44, 1, 0, 3],
    "Hornet Sportabout": [18.7, 8, 360, 175, 3.15, 3.44, 17.02, 0, 0, 3]
}

# task 4
# dictionary created with for loop for table 1
# unsure of how to do this as each key has different values
# so each iteration would need to add different values for each key
# this could work is table 1 was in a csv file

placesByLoop = {}
for location in places :
    placesByLoop[location] = []

print(placesByLoop)

print("")

# task 5 FOR loop time complexity of Code 1
# the time complexity if O(n)
# the for loop iterates for the amount of elements in the list numbers
# where the amount of elemets is represented by n

# task 6: convert ‘Recipe ingredients around the world’ into a dictionary
# What structure would be appropriate for ‘Flavour compounds"?

#opens worldregions_ingredients.csv in default read mode
recipes = open("worldregions_ingredients.csv")
# this will be a dictionary of dictionaries
recipiesDict = {}

dict = {}
# the header will be used to identify the keys that will be in dictionary saved to recipiesDict
header = recipes.readline()
header_split = header.split(",")

# count is used to limit the iterations of the loop, as there are thousands of records in the file
count  = 0
for line in recipes.readlines():
    line_split = line.split(",")
    # the header will contain the maximum amount of columns, as not all recipes have the same amount of ingredients
    for part in range (0, len(header_split)):
        # a new key-value pair is inserted for each field in the header
        # as long as there is a value in that cell
        # we don't want to add an empty key-value pair to our dictionary
        if (line_split[part] != '' and line_split[part] != '\n') :
            dict.setdefault(header_split[part], line_split[part])
    # the dictionary is added to recipesDict
    # as it needs a unique key, the incrementing recipe number is generated using count + 1
    # so the recipes start from recipe1
    recipiesDict.update({"recipe" + str(count + 1): dict})
    count = count + 1
    # to show proof of this working only 10 rows from worldregions_ingredients.csv will be added to the dictionary
    if (count == 10) :
        break

print(recipiesDict)

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

'''NOTE: this is not a fully implemented adjacency list on  flavourcompounds.csv
The fully working version would include checking the list for when ingredients are repeated eg: 
row 25: kaffir_lime -> kohlrabi 6 and row 36: kaffir_lime -> raw_potato 16
and adding these relationships to the same key
'''

flavours = open("flavourcompounds.csv", "r")
# skips header line
next(flavours)
# this will be a list of dictionaries
flavours_adj_list = []

count  = 0
for line in flavours.readlines():
    line_split = line.split(",")
    flavours_adj_list.append({line_split[0]: [{line_split[1], line_split[2].rstrip()} ] } )
    count = count + 1
    # to show proof of this working only 10 rows will be added to the dictionary
    if (count == 10) :
        break

print(flavours_adj_list)

flavours.close()

print("")

# task 6 Selection Sort time complexity
# the selection sort has a time complexity of O(n^2)
# this is because it has a loop and a nested loop both dependant on 
# the length of the list A, where the size of the list 
# is the amount elements in A, which is decided by the user/programmer
# with n being the amount of user data provided