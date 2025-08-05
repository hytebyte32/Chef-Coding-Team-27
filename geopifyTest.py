from Geopify import Geopify

api = Geopify()

def checkQueryInput(query):
    result = api.get_address(query)
    if input == None and result == None: #if no input is given, and output is none this is expected
        return True
    elif input != None and result != None: #if input is given, and output is given this is expected
        return True
    else: # if input != None and output == None, or if input == None and output != None
        return False

def checkCoordinates(latitude, longtitude):
    if 37 <= latitude <= 38 and -123 <= longtitude <= -122:
        return True
    else:
        return False
    
def checkOutput(address):
    geocoder = Geopify()
    result = geocoder.get_address(address)
    if input == None and result == None: #if no input is given, and output is none this is expected
        return True
    elif input != None and result != None: #if input is given, and output is given this is expected
        return True
    else: # if input != None and output == None, or if input == None and output != None
        return True

####################TEST####################

class TestQuery:

    def test_checkQueryInput_good(self):
        query = 'N6G5R6'
        expected = True
        actual = checkQueryInput(query)
        assert actual == expected

    def test_checkQueryInput_badA(self):
        query = 1234
        expected = True
        actual = checkQueryInput(query)
        assert actual == expected

    def test_checkQueryInput_badB(self):
        query = None
        expected = True
        actual = checkQueryInput(query)

        assert actual == expected

    def test_checkQueryInput_bad(self):
        query = 'asdfaf'
        expected = False
        actual = checkQueryInput(query)
        assert actual == expected

class TestOutput:

    def test_get_coordinates_success(self):
        geocoder = Geopify()
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        latitude, longtitude = geocoder.get_address(address)
        result = checkCoordinates(latitude,longtitude)  # Ensure latitiude and longitude is within the range
        expected = True
        assert result == expected
      

    def test_get_coordinates_empty_address(self):
        geocoder = Geopify()
        address = None
        result = geocoder.get_address(address)
        expected = False
        assert result == expected

    def test_get_coordinates_invalid_address(self):
        geocoder = Geopify()
        address = "Tsddasdfafsdf"
        result = geocoder.get_address(address)
        expected = False
        assert result == expected  # Assuming status code 400 for invalid address
