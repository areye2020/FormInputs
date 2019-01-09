from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    shows = {"Everybody Hates Chris":0, "Crazy Ex Girlfriend":0,"One Tree Hill":0,"The 100":0,"Smallville":0,"The Flash":0,"Riverdale":0,"The Vampire Diaries":0,"Whose Line is it Anyway?":0,"Americas Next Top Model":0}

    if Genre == "Comedy":
        shows["Everybody Hates Chris", "Crazy Ex Girlfriend"] += 2
    elif Genre == "Drama":
        shows["The 100","One Tree Hill"] += 2
    elif Genre == "Superhero":
        shows["The Flash","Smallville"] += 2
    elif Genre == "Suspence":
        shows["Riverdale","The Vampire Diaries"] += 2
    elif Genre == "Reality":
        shows["Whose Line is it Anyway?","Americas Next Top Model"] += 2

    if Type == "Amortentia":
        shows["Hufflepuff"] += 2
    elif Type == "Polyjuice":
        shows["Slytherin"] += 2


    Genre = request.form.get('input_dropdown', '')
    name = request.form.get('input_name', '')
    if name == "":
        return render_template("main_page.html", output="Plese Enter Name")
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="You're a wizard %s." % name)
