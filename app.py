from edamamAPI_v2 import EdamamData
from Geopify import Geopify
from OpenFoodFacts import OpenFoodFacts
from Spoonacular import Spoonacular

edamamapi = EdamamData()
geopifyapi = Geopify()
openfoodfactsapi = OpenFoodFacts()
spoonacularapi = Spoonacular()
# print final results
def printResults(recipeName, nutriscore, restaurant):
    print('Name: {name}\nNutrition Score: {score}\nRestaurants Nearby:\n'.format(name=recipeName, score = nutriscore))
    count = 0
    if restaurant == None or restaurant == []: #empty restuarant result list check
        print('No Restaurants Found.')
        return
    else:
        if len(restaurant["restaurants"]) >= 3: #arbritrary limit of 3 restaurants nearby to avoid information spam
            for i in range(3):
                print("Name: " + restaurant["restaurants"][i]["name"]) 
                print("Approximate distance: " + str(round(restaurant["restaurants"][i]["miles"] * 1.60934, 2)) + " km") 
                print("Address: " + restaurant["restaurants"][i]["address"]["street_addr"] 
                        + ", " + restaurant["restaurants"][i]["address"]['city']
                        + ", " + restaurant["restaurants"][i]["address"]['state']
                        + ", " + restaurant["restaurants"][i]["address"]['country']
                        + ", " + restaurant["restaurants"][i]["address"]['zipcode'] + "\n")
        else: #if there aren't 3 restaurants (arbritrary number) nearby, only print the number of available restaurants
            for i in range(len(restaurant["restaurants"])):
                print("Name: " + restaurant["restaurants"][i]["name"]) 
                print("Approximate distance (km): " + str(round(restaurant["restaurants"][i]["miles"] * 1.60934, 2)) + " km") 
                print("Address: " + restaurant["restaurants"][i]["address"]["street_addr"] 
                        + ", " + restaurant["restaurants"][i]["address"]['city']
                        + ", " + restaurant["restaurants"][i]["address"]['state']
                        + ", " + restaurant["restaurants"][i]["address"]['country']
                        + ", " + restaurant["restaurants"][i]["address"]['zipcode'] + "\n")
    return
    
print("Team 27 - Chef Coding - Information about your dish and nearby restaurants")
dish = input("Please Enter Desired Dish: ")
postal = input("Please Enter Postal Code: ")
print("API is thinking . . .")

recipes = edamamapi.getRecipeData(dish, 1) # get the recipes

ingredientsInformation = list(recipes.values()) # get the list of ingredients per recipe
recipeNames = list(recipes.keys()) # gets the list of recipe names

recipeIngredients = []
for recipe in ingredientsInformation: #extract the ingredient names
    ingredients = [x[2] for x in recipe]
    recipeIngredients.append(ingredients)

upcCodes = []
for ingredients in recipeIngredients: # get the upc codes from the ingredients
    upcCodes.append(spoonacularapi.mapIngredients(ingredients))

nutriscores = [] 
for codes in upcCodes: #append the openFoodFacts list with nutriscores
    nutriscores.append(openfoodfactsapi.nutriscorecalculator(codes))

cuisines = []
for name in recipes: #collect the cuisine of the food entered
    cuisines.append(edamamapi.getCuisineType(name))

print("According to EdamamAPI, the cuisine of your dish is: " + str(cuisines[0]))

location = geopifyapi.get_address(postal) # find your location

restaurants = {}
for cuisine in cuisines: # search for restuarants based on cuisine
    restaurants.update(spoonacularapi.searchRestaurant(lat=location[0],lng=location[1],cuisine=cuisines[0]))



# Final Results
for i in range(len(recipeNames)):
    printResults(recipeNames[i],nutriscores[i],restaurants)
    print('\n\n')

