#Andrew Liang
#251308760
import requests as r

class EdamamData:

    #id, key
    def __init__(self) -> None:
        self.__auth = ('0239e831','54b799524a9f296f3ccf9d8bfcc7a602') # changeable here incase of api limit
        self.__cuisineTypes = {} # saves recipe name : cuisine in dictionary
        self.__recipes = {} # saves recipe name : ingredients list in dictionary
    
    def __getRecipeLinks(self, rawData): # converts the raw data into a list of recipe links
        recipeLinks = []
        
        for links in rawData['hits']: # get recipe links
            recipeLinks.append(links['_links']['self']['href']) # adds the links to a list
        
        return recipeLinks

    def __getRecipeData(self, rawLinks, limit): # requests the data for a specific recipe
        recipeData = []
        count = 0
        
        for link in rawLinks: # adds the requested data into a list
            data = r.get(link).json()
            recipeData.append(data)

            count+=1
            if count == limit: # stops the loop once limit is reached
                break

        return recipeData        
    
    def __getRecipeNames(self, rawData): # gets the name of the recipes
        recipeNames = []
        
        for data in rawData: # adds the names to a list
            recipeNames.append(data['recipe']['label'])

        return recipeNames
    
    def __getIngredients(self, rawData): # returns information on ingredients
        totalIngredientsList = []
        interestedParameters = ['quantity', 'measure','food'] # list of relavent information
        
        for data in rawData:
            ingredientsList = [] 
            for ingredients in data['recipe']['ingredients']:
                filteredIngredient = [ingredients[x] for x in interestedParameters] # filters out irrelevant parameters
                ingredientsList.append(filteredIngredient)
            totalIngredientsList.append(ingredientsList) # nesting lists to prepare for zip function

        return totalIngredientsList
    
    def __getCuisineTypes(self, recipeNames, rawData): # gets the cuisine type from raw data
        cuisineTypes = []
        
        for cuisine in rawData:
            cuisineTypes.append(cuisine['recipe']['cuisineType'][0])
        return dict(zip(recipeNames,cuisineTypes)) # zips the list of names with list of cuisine types and casts as dict
    
    def getCuisineType(self, recipeName): # returns the cuisine type based on recipe name
        return self.__cuisineTypes[recipeName]

    def getRecipeData(self, searchKey, limit=1): # gets the recipe data
        if type(limit) == float:
            limit = int(limit)
        elif type(limit) != int: # catches TypeErrors before they happen
            limit = 1
        elif limit > 10:
            limit = 10
        elif limit <=0:
            return {} # returns empty dict when the limit is less than 0
        else:
            pass # limit input passes the checks
        
        # gets links json
        recipeLinks = r.get('https://api.edamam.com/api/recipes/v2?type=public&q={search}&app_id={appId}&app_key={appKey}&field=url'.format(search=searchKey,appId=self.__auth[0],appKey=self.__auth[1])).json()
        
        recipeLinks = self.__getRecipeLinks(recipeLinks) # extracts links from json
        recipeData = self.__getRecipeData(recipeLinks, limit) # gets recipes json from links 
        recipeNames = self.__getRecipeNames(recipeData) # gets names from recipes json
        recipeIngredients = self.__getIngredients(recipeData) # gets ingredients from recipes json
        
        self.__cuisineTypes = self.__getCuisineTypes(recipeNames, recipeData) # gets cuisine types from recipes json
        self.__recipes = dict(zip(recipeNames,recipeIngredients)) # zips the recipe names and ingredients into a dictionary

        return self.__recipes