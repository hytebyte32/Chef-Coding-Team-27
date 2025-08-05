from Spoonacular import *
class Test:

#mapIngredients function testing
    def test_UPC_good(self):
        input = ['flour','bacon','oil']
        actual = Spoonacular().mapIngredients(ingredients=input)
        #can also test if you know the API-provided UPC codes, 
        #but we assume that they can change and therefore only test 
        #if the API response is a list
        #expected = ['4018905311233', '044700023280', '036023004022']

        assert isinstance(actual,list)
        #assert actual == expected

    def test_UPC_empty(self):
        input = []
        actual = Spoonacular().mapIngredients(ingredients=input)
        expected = []

        assert actual == expected

    def test_UPC_None(self):
        input = None
        actual = Spoonacular().mapIngredients(ingredients=input)
        expected = TypeError

        assert actual == expected

    def test_UPC_notfound(self):
        input = ["safjkdkbdvbl"]
        actual = Spoonacular().mapIngredients(ingredients=input)
        expected = []

        assert actual == expected

#searchRestaurants function testing
    def test_searchRestarant_good(self):
        lat=43.00441722228767
        lng=-81.27617531329763
        cuisine= "italian"
        actual = Spoonacular().searchRestaurant(lat=lat,lng=lng,cuisine=cuisine)
        expected = "King Richie's Pizzeria"

        assert actual["restaurants"][0]["name"] == expected

    def test_searchRestaurant_missingCuisine(self):
        lat=43.00441722228767
        lng=-81.27617531329763
        cuisine= ""
        actual = Spoonacular().searchRestaurant(lat=lat,lng=lng,cuisine=cuisine)
        expected = "King Richie's Pizzeria"

        assert actual["restaurants"][0]["name"] == expected

    def test_searchRestaurant_invalidCuisine(self):
        lat=43.00441722228767
        lng=-81.27617531329763
        cuisine= "sbhdkdjkasas"
        actual = Spoonacular().searchRestaurant(lat=lat,lng=lng,cuisine=cuisine)
        expected = "King Richie's Pizzeria"

        assert (actual["restaurants"][0]["name"] == expected)
        
    def test_searchRestaurant_missingLat(self):
        lat=""
        lng=-81.27617531329763
        cuisine= "italian"
        actual = Spoonacular().searchRestaurant(lat=lat,lng=lng,cuisine=cuisine)
        expected = ValueError

        assert actual["restaurants"][0]["name"] == expected
    
    def test_searchRestaurant_missingInfo(self):
        lat=""
        lng=""
        cuisine= ""
        actual = Spoonacular().searchRestaurant(lat=lat,lng=lng,cuisine=cuisine)
        expected = []

        assert actual["restaurants"][0]["name"] == expected
    
    def test_searchRestaurant_None(self):
        lat= None
        lng= None
        cuisine= None
        actual = Spoonacular().searchRestaurant(lat=lat,lng=lng,cuisine=cuisine)
        expected = []

        assert actual["restaurants"][0]["name"] == expected
    
    def test_searchRestaurant_lowerBound(self):
        lat = -9999
        lng = -9999
        cuisine = "italian"
        actual = Spoonacular().searchRestaurant(lat=lat,lng=lng,cuisine=cuisine)
        expected = ValueError

        assert actual["restaurants"][0]["name"] == expected
    
    def test_searchRestaurant_higherBound(self):
        lat = 9999
        lng = 9999
        cuisine = "italian"
        actual = Spoonacular().searchRestaurant(lat=lat,lng=lng,cuisine=cuisine)
        expected = ValueError
        
        assert actual["restaurants"][0]["name"] == expected