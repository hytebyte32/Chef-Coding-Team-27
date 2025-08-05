import requests

class Geopify:
    
    API_KEY = "16bd0f7134a9497cbace91ab45013c70"

    def get_address(self,address):
        # Build the API URL
        url = f"https://api.geoapify.com/v1/geocode/search?text={address}&limit=1&apiKey={self.API_KEY}"

        # Send the API request and get the response
        response = requests.get(url)

        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON data from the response
            data = response.json()

            # Extract the first result from the data
            result = data["features"][0]

            # Extract the latitude and longitude of the result
            latitude = result["geometry"]["coordinates"][1]
            longitude = result["geometry"]["coordinates"][0]

            #print(f"Latitude: {latitude}, Longitude: {longitude}")
            return latitude,longitude
        else:
            #print(f"Request failed with status code {response.status_code}")
            return {response.status_code}
