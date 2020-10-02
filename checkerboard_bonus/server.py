#Created by Shelley Ophir
#Coding Dojo Oct 2, 2020
#practice linking static files to our template. For this project, we'll render a template that displays a checkerboard
# Your program should have the outputs below

# Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)

#first import libraries
from flask import Flask, render_template

#create instance of Flask 
app = Flask (__name__)

# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route ("/")
def boardNum0():
    return render_template ("index.html", x = 8, y = 8)

# http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route("/<int:y>")
def boardNum1(y):
    return render_template("index.html", x = 8, y = y)

# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard. 
@app.route("/<int:y>/<int:x>")
def boardNum2(x, y):
    return render_template("index.html", x = x, y = y)

# BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route("/<int:y>/<int:x>/<color1>/<color2>")
def boardBonus(x, y, color1, color2):
    return render_template("index.html", x = x, y = y, color1 = color1, color2 = color2)

#add debugger
if (__name__ == "__main__"):
    app.run (debug = True)