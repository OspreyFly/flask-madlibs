from flask import Flask, request, render_template, session, redirect, url_for
from stories import Story

app = Flask(__name__)
app.secret_key = 'secret_key'

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")

@app.route('/home')
def home():
    return render_template('home.html', story=story)

@app.route("/story")
def story_page():
    input_values = session.get('input_values', [])
    print("INPUT_VALUES: ", input_values)
    text = story.generate(input_values)
    print("TEXT: ", text)
    return render_template('stories.html', text=text)

@app.route("/submit", methods=['POST'])
def submit():
    input_values = request.form
    print("SUBMIT: ", input_values)
    session['input_values'] = input_values
    return redirect("/story")