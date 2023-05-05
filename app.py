from ai_utils import get_response

prompt_categories = [
    # {"title": "", "prompt": "\nList speakers in the meeting. \nList Agenda discussed in the meeting. \nList the resolutions reached in the meeting. \nList next Steps\n"},

    {"title": "\nSpeakers:", "prompt": "\nList people who spoke in the meeting\nSpeakers:\n-"},
    {"title": "\nAgenda items:", "prompt": "\nList the Agenda of the meeting\nAgenda items:\n-"},
    {"title": "\nResolutions:", "prompt": "\nList conclusions reached in the meeting\nConclusions:\n-"},
    {"title": "\nNext Steps:", "prompt": "\nWhat is next after the meeting\nNext Steps:\n-"}
]

# Prompt postfix
prompt_postfix = """ <document>
  \n###
"""
#print(prompt_postfix)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    content = format(request.form['text'])
    full_response = ""
    for prompt in prompt_categories:
        full_response = full_response + "\n" + prompt["title"] 
        prompt_with_postfix = prompt_postfix + prompt["prompt"]
        response = get_response(content, prompt_with_postfix)
        full_response = full_response + "\n-" + response

    return full_response, 200, {'Content-Type': 'text/css; charset=utf-8'}