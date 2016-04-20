from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game2')
def show_game_form():
    """Get madlib input"""

    play_game = request.args.get('play-game')

    if play_game == "yes":
        return render_template("game2.html")

    else:
        return render_template('goodbye.html')




@app.route('/madlib2', methods=['POST'])
def show_madlib():
    """renders a delightfully hilarious story"""

    adjective = request.form.get("adjective")
    adverb = request.form.get("adverb")
    body_part = request.form.get("body-part")
    noun = request.form.get("noun")
    plural_noun = request.form.get("plural-noun")

    dwarf_input = request.form.getlist("dwarfs")

    print dwarf_input
    # all_dwarfs = ["Snow White"] + dwarf_input

    # if dwarf_input == []:
    #     dwarfs = "Snow White"
    #     dwarf = "Snow White"
    # else: 
    #     dwarfs = ", ".join(all_dwarfs[:-1]) + " and " + all_dwarfs[-1]
    #     dwarf = choice(all_dwarfs)

    return render_template("madlibs2.html",
                           adjective=adjective,
                           adverb=adverb,
                           body=body_part,
                           noun=noun,
                           nouns=plural_noun,
                           dwarfs=dwarf_input,
                           dwarf=dwarf_input)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
