#from EdamamAPI import EdamamData
from edamamAPI_v2 import EdamamData

#api = EdamamData()
api = EdamamData()

def checkQueryInput(query, limit = 1):
    result = api.getRecipeData(query, limit)
    if input == None and result == None: #if no input is given, and output is none this is expected
        return True
    elif input != None and result != None: #if input is given, and output is given this is expected
        return True
    else: # if input != None and output == None, or if input == None and output != None
        return False

def checkOutputCount(query, limit):
    if limit == len(api.getRecipeData(query, limit)): #if the limit given matches dict size of output, expected output
        return True
    else:
        return False #if the limit given does not match size of dict, unexpected output
    
####################TEST####################

class TestQuery:
    def test_checkQueryInput_good(self):
        query = 'chicken'
        expected = True # output expected
        actual = checkQueryInput(query)

        assert actual == expected
    
    def test_checkQueryInput_badA(self):
        query = 1234
        expected = True # should return empty list
        actual = checkQueryInput(query)

        assert actual == expected

    def test_checkQueryInput_badB(self):
        query = None
        expected = True # should return empty list therefore
        actual = checkQueryInput(query)

        assert actual == expected

    def test_checkQueryInput_bad(self):
        query = '1274y27ehquirh283ygiqw'
        expected = True # output expected
        actual = checkQueryInput(query)

        assert actual == expected

class TestOutputCount:    
    def test_checkOutputCount_good(self):
        limit = 3
        expected = True
        actual = checkOutputCount('chicken',limit)

        assert actual == expected

    def test_checkOutputCount_badA(self):
        limit = '123abc'
        expected = False
        actual = checkOutputCount('chicken',limit)

        assert actual == expected

    def test_checkOutputCount_badB(self):
        limit = None
        expected = False
        actual = checkOutputCount('chicken',limit)

        assert actual == expected
    
    def test_checkOutputCount_badC(self):
        limit = {'test':123}
        expected = False
        actual = checkOutputCount('chicken',limit)

        assert actual == expected
    
    
    def test_checkOutputCount_outOfBoundsLower(self):
        limit = -10
        expected = False
        actual = checkOutputCount('chicken',limit)

        assert actual == expected

    def test_checkOutputCount_outOfBoundsUpper(self):
        limit = 20
        expected = False
        actual = checkOutputCount('chicken',limit)

        assert actual == expected
    
    def test_checkOutputCount_boundsLower(self):
        limit = 0
        expected = True
        actual = checkOutputCount('chicken',limit)

        assert actual == expected
    
    def test_checkOutputCount_boundsUpper(self):
        limit = 10
        expected = True
        actual = checkOutputCount('chicken',limit)

        assert actual == expected
