from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story, story_2 

app = Flask(__name__)
app.config['SECRET_KEY'] = "randomsecretkey"

debug = DebugToolbarExtension(app)

@app.route('/')
def show_madlibs_form():
    prompts =  story.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story-2-form')
def show_madlibs_2_form():
    new_prompts = story_2.prompts
    return render_template('home.html', new_prompts=new_prompts)

@app.route('/story')
def get_story():
    text = story.generate(request.args)
    return render_template('story.html', text=text)

@app.route('/story-2')
def get_story_2():
    new_text = story_2.generate(request.args)
    return render_template('story-2.html', text=new_text)



