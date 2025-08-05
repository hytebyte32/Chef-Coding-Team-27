**Project Description**

This project integrates multiple public APIs to answer discover where the healthiest food options available are given location and desired food, based on nutritional data from multiple sources. To do this, we combine location-based vendor data from Geoapify with nutritional insights from Spoonacular, Edamam, and Open Food Facts. The system identifies food items or dishes served nearby and evaluates their healthiness using ingredient-level nutrition analysis and Nutri-Score ratings.

**Scope**

This project focuses on real-world food discovery by finding healthier food options available near you. The system helps users make informed decisions when dining out or ordering in, by analyzing food offerings at nearby locations.

**APIS Used**

https://developer.edamam.com/edamam-recipe-api

https://apidocs.geoapify.com/

https://openfoodfacts.github.io/openfoodfacts-server/api/

https://spoonacular.com/food-api

**Usage**

Public container image: https://hub.docker.com/r/hchiang9/team27-chef-coding/tags
Note: Due to user input within the program, the program must be run through Docker on
Command Prompt, not Docker Desktop. The –i flag must be used when running this Docker
container ex. docker run -i hchiang9/team27-chef-coding:latest

1. Run the program, either through downloading code to run locally or through Docker
as mentioned

![](img/step1.png)

2. Enter a dish that you would like to find the Nutri-score (indicating how healthy it is)
and your postal code.

&nbsp; &nbsp; &nbsp; &nbsp; a. Dish name is not case-sensitive

&nbsp; &nbsp; &nbsp; &nbsp; b. Postal code is not case-sensitive, HOWEVER ensure that it is in the form of (letter)(number)(letter)(SPACE) (number)(letter)(number). Ex. N6A 3K7

![](img/step2.png)

3. Let the program run. If the APIs are successful in finding a recipe for your dish, they
will display a recipe followed by details of up to 3 restaurants nearby that may serve
your dish.

&nbsp; &nbsp; &nbsp; &nbsp; a. Note: Results may vary with dish name and location. Restaurants are searched through your location and the cuisine of the user-entered dish. 

![](img/step3.png)

**Project Credits**

Muhammad Ahmad: Integrated OpenFoodFacts API and it's corresponding tests

Kwan Nok Lau: Integrated Geoapify API and it's corresponding tests

Harold Chiang: Integrated Spoonacular API, it's corresponding tests, responsible for packaging project into docker container, helped with debugging, and wrote usage documentation 

Andrew Liang: Integrated Edamam API, it's corresponding tests, consolidated all other modules into a single application, and helped with debugging
