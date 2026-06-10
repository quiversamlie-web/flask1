from xml.dom.minidom import Document

from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Home/1st page
@app.route("/")
def pertama():
    # <a> anchor tag with its attribute
    return "<h1>Hello, World!</h1><br><p>Nice to see you</p><p>please check</p><a href='/random_fact'>View a random fact!</a><br><a href='/modern_fact'>View a modern fact!</a><br><a href='/random_password'>View a Random Password!</a>|<br><a href='/Coinflip'>View a Coinflip!</a>"
    
# 2nd page
@app.route("/random_fact")

def kedua():
    txt_name = random.choice(os.listdir("fact_list"))
    # formatted string
    with open(f'fact_list/{txt_name}', 'r') as f:
        document = f.read()
    return f'{document}'

@app.route("/random_password")

def ketiga():
    elements = "+-/*!&$#?=@<>"
    password = ""
    a = random.randint(5,15)

    for i in range(a):
        password += random.choice(elements)

    return password

@app.route("/Coinflip")

def keempat():
    num = random.randint(1,2)
    if num == 1:
        return "Heads"
    else:
        return "Tails"
# 2nd page
@app.route('/modern_fact')
def index():
    return render_template('dasar.html')#folder templates
app.run(debug=True)
