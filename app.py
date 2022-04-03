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


@app.route('/results', methods=["GET", "POST"])
def results():  # put application's code here
    inventory = ['bourbon', 'Cointreau', 'lime juice', 'sweetener', 'ice', 'lime wedge']
    posts = []
    with open('gimmesomeovenRecipes.json', encoding='utf-8') as rawdata:
        data = json.load(rawdata)
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
        posts.append(d)

    return render_template("result/results.html", posts=posts)


if __name__ == '__main__':
    app.run()
