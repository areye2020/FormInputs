from flask import Flask, request, render_template
app = Flask(__name__)



def select_show(Genre, Type):

    shows = {"Everybody Hates Chris":0, "Crazy Ex Girlfriend":0,"One Tree Hill":0,"The 100":0,"Smallville":0,"The Flash":0,"Riverdale":0,"The Vampire Diaries":0,"Whose Line is it Anyway?":0,"Americas Next Top Model":0}

    if Genre == "Comedy":
        for show in ["Everybody Hates Chris","Crazy Ex Girlfriend"]:
            shows[show] += 2
    elif Genre == "Drama":
        for show in ["The 100","One Tree Hill"]:
            shows[show] += 2
    elif Genre == "Superhero":
        for show in ["The Flash","Smallville"]:
            shows[show] += 2
    elif Genre == "Suspence":
        for show in ["Riverdale","The Vampire Diaries"]:
            shows[show] += 2
    elif Genre == "Reality":
        for show in ["Whose Line is it Anyway?","Americas Next Top Model"]:
            shows[show] += 2

    if Type == "Current":
        for show in ["Crazy Ex Girlfriend", "The 100", "The Flash", "Riverdale", "Whose Line is it Anyway?"]:
            shows[show] += 2
    elif Type == "Past":
        for show in ["Everybody Hates Chris", "One Tree Hill", "Smallville", "The Vampire Diaries","Americas Next Top Model"]:
            shows[show] += 2
    selected_show = None
    for show, points in shows.items():
        if selected_show is None or shows[selected_show] < points:
            selected_show = show

    return selected_show

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")


@app.route('/process_inputs', methods=['POST'])

def process_inputs():
    Genre = request.form.get('input_dropdown', '')
    Type = request.form.get('input_select', '')
    name = request.form.get('input_name', '')
    if name == "":
        return render_template("main_page.html", output="Plese Enter Name")

    selected_show = select_show(Genre, Type)

    return render_template("main_page.html",
                           output= "Hmmmmmmmm , {0} based on your inputs the CW show that you should watch is ...........{1}!".format(name,selected_show))
