from ai_utils import get_response

content = """Jialin: Hi everyone 
Tiffany: Hello
Alana: Hello
Jialin: Alright lets get started
I can go first
Yesterday I starting looking into 1234 to do stuff with worked a bit on the xyz script and got a gui working with abc
And that's it
Alana: Oh I did something with that too we can talk about it later
Jialin: ok
Tiffany: I can go next
Yesterday I worked on getting the 456 to work better. Trying to get the 987 working
Today Im working on that as well - it works pretty well now 
Alana: Okay i can go
Yesterday I worked on getting 12345 setup as well. Later ill work on integrating the api with the 12345 bot
Jialin: cool!
Alana: Alright I guess that's it
Tiffany: yeap
Alright see you guys
Alana: Bye!
Jialin: Bye """

prompt_categories = [
    # {"title": "", "prompt": "\nList speakers in the meeting. \nList Agenda discussed in the meeting. \nList the resolutions reached in the meeting. \nList next Steps\n"},

    {"title": "\nSpeakers:", "prompt": "\nList speakers in the meeting\nSpeakers:\n-"},
    {"title": "\nAgenda items:", "prompt": "\nList the Agenda of the meeting\nAgenda items:\n-"},
    {"title": "\nResolutions:", "prompt": "\nList conclusions reached in the meeting\nConclusions:\n-"},
    {"title": "\nNext Steps:", "prompt": "\nWhat is next after the meeting\nNext Steps:\n-"}
]


prompt_categories_scrum = [
    # {"title": "", "prompt": "\nList speakers in the meeting. \nList Agenda discussed in the meeting. \nList the resolutions reached in the meeting. \nList next Steps\n"},
    {"title": "\nAttendance:", "prompt": "\nList Attendance in the meeting\nAttendance:\n"},
    {"title": "\nWorked on Yesterday:", "prompt": "\nList What did each person work on yesterday?\n"},
    {"title": "\nWorking on Today:", "prompt": "\nList What will each person work on today?\n"}
]

# Prompt postfix
prompt_postfix = """ <document>
  \n###
"""
#print(prompt_postfix)


for prompt in prompt_categories_scrum:
    print(prompt["title"])
    prompt_with_postfix = prompt_postfix + prompt["prompt"]
    response = get_response(content, prompt_with_postfix)
    print(response)
