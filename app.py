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


#
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("result/home.html")

@app.route("/inventory", methods=["GET", "POST"])
def inv():
    return render_template("inventory.html")



@app.route('/results', methods=["GET", "POST"])
def results():  # put application's code here
    inventory = ['bourbon', 'Cointreau', 'lime juice', 'sweetener', 'ice', 'lime wedge']
    posts0 = []
    posts1 = []
    posts2 = []
    posts3 = []
    with open('gimmesomeovenRecipes.json', encoding='utf-8') as rawdata:
        data = json.load(rawdata)
    count = 0
    for d in data:
        # print(d)

        recipe = Recipe(d['name'], d['servings'], d['ingredients'], d['instructions'], d['link'], d['image'])
        # cnt = 0
        # for i in inventory:
        #     print(i)
        #     print(recipe.ingredients)
        #     for r in recipe.ingredients:
        #         if i in r:
        #             cnt += 1
        #             break
        # score = cnt / len(recipe.ingredients)
        # print(cnt)
        # print(len(recipe.ingredients))
        # print(score)
        # break
        if count == 0:
            posts0.append(d)
            count +=1
        elif count == 1:
            posts1.append(d)
            count +=1
        elif count == 2:
            posts2.append(d)
            count +=1
        elif count == 3:
            posts3.append(d)
            count =0
    print(len(posts0))



    return render_template("result/results.html", posts0=posts0,posts1=posts1,posts2=posts2,posts3=posts3)


if __name__ == '__main__':
    app.run()
