import requests

class OpenFoodFacts:
    import requests
    def nutriscorecalculator(self, ingredients):
        data = []
        ingredients = list(map(str, ingredients))
        for i in ingredients:
            response = requests.get("https://world.openfoodfacts.net/api/v2/product/"+ i+ "?fields=nutriscore_data")
            
            response = str(response.text)
            response = response.replace('[','')
            response = response.replace(']','')
            response = response.replace('{','')
            response = response.replace('}','')
            response = response.replace("'",'')
            response = response.split(",")
            

            mydict = {}#getting the score of all the data for eggs to get average score for eggs
            for i in response:
                if "score" in i:
                    if "nutri" in i:
                        if i in mydict:
                            mydict[i]+=1
                    else:
                        mydict[i]=1

            
            if len(mydict)> 0:
                keysList = list(mydict.keys())
                finalstr = str(keysList)
                pairs = finalstr[1:-1].split(', ')

                result_dict = {}
                for pair in pairs:
                    key, value = pair.split(':')
                    key = key.strip('"')
                    value = value.rstrip("'")
                    value = int(value)
                    if key in result_dict:
                        result_dict[key].append(value)
                    else:
                        result_dict[key] = [value]

                
                value_list = list(result_dict.values())
                sum_score = (sum(value_list[0]))/len(value_list[0])
                data.append(sum_score)


                
            else:
                data.append("Data not avaliable")
        #print(data)#We can iun comment this function to see for how many items data is missing. If the data is missing for all the entries a default zero will be shown.
        
        total_score = sum(item for item in data if isinstance(item, (int, float)))
    
        

        return total_score
    
    
#ingridients = [3017624010701,None ,9300650271135, 2324343434]
#print(OpenFoodFacts().nutriscorecalculator(ingridients))



