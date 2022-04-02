from urllib import response
import requests 
from bs4 import BeautifulSoup 
import json

arr = []



head = "https://www.gimmesomeoven.com/all-recipes/?fwp_paged="

for i in range (1,2):
    pagelink = head + str(i)
    response = requests.get(pagelink).content
    allPage = BeautifulSoup(response, "html.parser")
    recipes = allPage.findAll("div", {"class": "teaser-post-sm"})
    for each in recipes:
        response = requests.get(each.a["href"]).content
        recipePage = BeautifulSoup(response, "html.parser")
        #print(recipePage)
        #print(f"link {i} : " + each.a["href"])
        title = recipePage.find("h1", {"class": "posttitle"}).text
        
        images = recipePage.findAll("img", {"class": "size-full"})
        
        for image in images:
            if 'www.gimmesomeoven.com' in image['src']:
                print(image['src'])
                img = image["src"]
                break

        yields = recipePage.find("span", {"class": "tasty-recipes-yield"}).text
       
            
        ing = []
        instructions = []
        ingList = recipePage.find("div", {"class": "tasty-recipes-ingredients"}).ul
        for ingredient in ingList.findAll('li'):
            ing.append(ingredient.text)
        instructionList = recipePage.find("div", {"class": "tasty-recipes-instructions"})
        
        for step in instructionList.findAll('li'):
            instructions.append(step.text)
        
        recipeObject = {
            "name": title,
            "servings": yields,
            "ingredients": ing,
            "instructions": instructions,
            "link": str(each.a["href"]),
            "image": str(img)
        }
        arr.append(recipeObject)

with open('RecipeData.json', 'w',encoding='utf-8') as outfile: json.dump(arr, outfile, ensure_ascii=False, indent=4)  
