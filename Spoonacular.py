import spoonacular as sp

class Spoonacular:
    api = sp.API("9206df35ad5d48ad87146c55ab8d7ed6")
    #api = sp.API("e0c6fc118f264704998dc0dcd1af1dd8")
    #api = sp.API("e47aaf18142a4cb0acb42625045b57a2")
    def mapIngredients(self, ingredients):
        #Map ingredients to UPC codes
        #ingredients = ["eggs","Bacon","vinegar","oil","flour"]
        response = self.api.map_ingredients_to_grocery_products(ingredients=ingredients,servings=1)
        data = response.json() # .json returns a list with a dict inside
        upc_code = [] #stores all the UPC codes
        for i in range(len(data)):
            if len(data[i]["products"]) != 0:
                upc_code.append(data[i]["products"][0]["upc"])
        
        return upc_code

    #print(upc_code)

    def searchRestaurant(self, lat, lng, cuisine):
        #Search Restaurants (using custom API definition)
        #refer to https://spoonacular.com/food-api/docs#Search-Restaurants

        #lat=43.00441722228767
        #lng=-81.27617531329763
        #distance = 0
        try:
            print("Searching API")
            response = self.api.search_restaurants(lat=lat,lng=lng,cuisine=cuisine)
            data = response.json() # .json returns a list with a dict inside    
        except: 
            print("API was unable to find a restaurant nearby or timed out. Try again?")
        else: 
            return data

            '''print("Here are the top restaurants nearby:")
            if len(data["restaurants"]) >= 10:
                for i in range(10):
                    print("Name: " + data["restaurants"][i]["name"]) 
            else:
                for i in range(len(data["restaurants"])):
                    print("Name: " + data["restaurants"][i]["name"]) '''

           





