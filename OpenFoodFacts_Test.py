from OpenFoodFacts import OpenFoodFacts
api = OpenFoodFacts()
def checkQueryInput(query):
    result = api.nutriscorecalculator(query)
    if input is None and result == 0:  
        return True
    elif input is not None and isinstance(result, (int, float)):  
        return True
    else: 
        return False


###################Test#######################
class TestQuery:
    def test_checkQueryInput_good(self):
        query = []
        expected = True
        actual = checkQueryInput(query)

        assert actual == expected


    def test_checkQueryInput_good(self):
        query = [3017624010701, 9300650271135, 2324343434]
        expected = True
        actual = checkQueryInput(query)

        assert actual == expected


    def test_checkQueryInput_good(self):
        query = [None]
        expected = True
        actual = checkQueryInput(query)

        assert actual == expected

    def test_checkQueryInput_good(self):
        query = ["jkhklj"]
        expected = True
        actual = checkQueryInput(query)

        assert actual == expected
        