from flask import Flask, render_template
import json

app = Flask(__name__)
recipes = []


class Recipe:
    def __init__(self, name, servings, ingredients, instructions, link, image):
        self.name = name
        self.servings = servings
        self.ingredients = ingredients
        self.instructions = instructions
        self.link = link
        self.image = image
        self.score = 0


#
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("result/home.html")

@app.route("/inventory", methods=["GET", "POST"])
def inv():
    return render_template("inventory.html")



@app.route('/results', methods=["GET", "POST"])
def results():  # put application's code here
    with open('inventory.json', encoding='utf-8') as inv:
        inventory =json.load(inv)


    posts0 = []
    posts1 = []
    posts2 = []
    posts3 = []
    allRecipe = []
    with open('gimmesomeovenRecipes.json', encoding='utf-8') as rawdata:
        data = json.load(rawdata)
    count = 0

    for d in data:
        # print(d)

        recipeD = Recipe(d['name'], d['servings'], d['ingredients'], d['instructions'], d['link'], d['image'])

        cnt = 0
        #print(inventory)
        for a in inventory:
            i = a['name']
            #print(i)
            #print(recipeD.ingredients)
            for r in recipeD.ingredients:
                if i in r:
                    cnt += 1
                    break

        recipeD.score = int(cnt / len(recipeD.ingredients)*100)
        if recipeD.score > 100:
            recipeD.score = 100
        #print(cnt)
        #print(len(recipe.ingredients))
        #print(score)
        print(recipeD.score)
        #break





        allRecipe.append(recipeD)

    allRecipe = sorted(allRecipe, key=lambda x: x.score, reverse=True)
    for recipe in allRecipe:




        if count == 0:
            posts0.append(recipe)
            count +=1
        elif count == 1:
            posts1.append(recipe)
            count +=1
        elif count == 2:
            posts2.append(recipe)
            count +=1
        elif count == 3:
            posts3.append(recipe)
            count =0
    print(len(posts0))



    return render_template("result/results.html", posts0=posts0,posts1=posts1,posts2=posts2,posts3=posts3)


if __name__ == '__main__':
    app.run()
