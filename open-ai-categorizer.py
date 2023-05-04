#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
from dotenv import load_dotenv
load_dotenv()

# Insert your own api_base, version, and key
openai.api_type = "azure"
openai.api_base =  os.getenv("OPEN_AI_API_BASE")
openai.api_version =  os.getenv("OPEN_AI_API_VERSION")
openai.api_key = os.getenv("OPEN_AI_API_KEY")
#response = openai.Completion.create(
#  engine="curie",
#  prompt="#Start of meetingChairman Wormsley (at the proper time and place, after taking the chair and striking the gavel on the table): This meeting of the CTAS County Commission will come to order. Clerk please call the role. (Ensure that a majority of the members are present.)\n\nChairman Wormsley: Each of you has received the agenda. I will entertain a motion that the agenda be approved.\n\nCommissioner Brown: So moved.\n\nCommissioner Hobbs: Seconded\n\nChairman Wormsley: It has been moved and seconded that the agenda be approved as received by the members. All those in favor signify by saying \"Aye\"?...Opposed by saying \"No\"?...The agenda is approved. You have received a copy of the minutes of the last meeting. Are there any corrections or additions to the meeting?\n\nCommissioner McCroskey: Mister Chairman, my name has been omitted from the Special Committee on Indigent Care.\n\nChairman Wormsley: Thank you. If there are no objections, the minutes will be corrected to include the name of Commissioner McCroskey. Will the clerk please make this correction. Any further corrections? Seeing none, without objection the minutes will stand approved as read. (This is sort of a short cut way that is commonly used for approval of minutes and/or the agenda rather than requiring a motion and second.)\n\nChairman Wormsley: Commissioner Adkins, the first item on the agenda is yours.\n\nCommissioner Adkins: Mister Chairman, I would like to make a motion to approve the resolution taking money from the Data Processing Reserve Account in the County Clerk's office and moving it to the equipment line to purchase a laptop computer.\n\nCommissioner Carmical: I second the motion.\n\nChairman Wormsley: This resolution has a motion and second. Will the clerk please take the vote.\n\nChairman Wormsley: The resolution passes. We will now take up old business. At our last meeting, Commissioner McKee, your motion to sell property near the airport was deferred to this meeting. You are recognized.\n\nCommissioner McKee: I move to withdraw that motion.\n\nChairman Wormsley: Commissioner McKee has moved to withdraw his motion to sell property near the airport. Seeing no objection, this motion is withdrawn. The next item on the agenda is Commissioner Rodgers'.\n\nCommissioner Rodgers: I move adopton of the resolution previously provided to each of you to increase the state match local litigation tax in circuit, chancery, and criminal courts to the maximum amounts permissible. This resolution calls for the increases to go to the general fund.\n\nChairman Wormsley: Commissioner Duckett\n\nCommissioner Duckett: The sheriff is opposed to this increase.\n\nChairman Wormsley: Commissioner, you are out of order because this motion has not been seconded as needed before the floor is open for discussion or debate. Discussion will begin after we have a second. Is there a second?\n\nCommissioner Reinhart: For purposes of discussion, I second the motion.\n\nChairman Wormsley: Commissioner Rodgers is recognized.\n\nCommissioner Rodgers: (Speaks about the data on collections, handing out all sorts of numerical figures regarding the litigation tax, and the county's need for additional revenue.)\n\nChairman Wormsley: Commissioner Duckett\n\nCommissioner Duckett: I move an amendment to the motion to require 25 percent of the proceeds from the increase in the tax on criminal cases go to fund the sheriff's department.\n\nChairman Wormsley: Commissioner Malone\n\nCommissioner Malone: I second the amendment.\n\nChairman Wormsley: A motion has been made and seconded to amend the motion to increase the state match local litigation taxes to the maximum amounts to require 25 percent of the proceeds from the increase in the tax on criminal cases in courts of record going to fund the sheriff's department. Any discussion? Will all those in favor please raise your hand? All those opposed please raise your hand. The amendment carries 17-2. We are now on the motion as amended. Any further discussion?\n\nCommissioner Headrick: Does this require a two-thirds vote?\n\nChairman Wormsley: Will the county attorney answer that question?\n\nCounty Attorney Fults: Since these are only courts of record, a majority vote will pass it. The two-thirds requirement is for the general sessions taxes.\n\nChairman Wormsley: Other questions or discussion? Commissioner Adams.\n\nCommissioner Adams: Move for a roll call vote.\n\nCommissioner Crenshaw: Second\n\nChairman Wormsley: The motion has been made and seconded that the state match local litigation taxes be increased to the maximum amounts allowed by law with 25 percent of the proceeds from the increase in the tax on criminal cases in courts of record going to fund the sheriff's department. Will all those in favor please vote as the clerk calls your name, those in favor vote \"aye,\" those against vote \"no.\" Nine votes for, nine votes against, one not voting. The increase fails. We are now on new business. Commissioner Adkins, the first item on the agenda is yours.\n\nCommissioner Adkins: Each of you has previously received a copy of a resolution to increase the wheel tax by $10 to make up the state cut in education funding. I move adoption of this resolution.\n\nChairman Wormsley: Commissioner Thompson\n\nCommissioner Thompson: I second.\n\nChairman Wormsley: It has been properly moved and seconded that a resolution increasing the wheel tax by $10 to make up the state cut in education funding be passed. Any discussion? (At this point numerous county commissioners speak for and against increasing the wheel tax and making up the education cuts. This is the first time this resolution is under consideration.) Commissioner Hayes is recognized.\n\nCommissioner Hayes: I move previous question.\n\nCommisioner Crenshaw: Second.\n\nChairman Wormsley: Previous question has been moved and seconded. As you know, a motion for previous question, if passed by a two-thirds vote, will cut off further debate and require us to vote yes or no on the resolution before us. You should vote for this motion if you wish to cut off further debate of the wheel tax increase at this point. Will all those in favor of previous question please raise your hand? Will all those against please raise your hand? The vote is 17-2. Previous question passes. We are now on the motion to increase the wheel tax by $10 to make up the state cut in education funding. Will all those in favor please raise your hand? Will all those against please raise your hand? The vote is 17-2. This increase passes on first passage. Is there any other new business? Since no member is seeking recognition, are there announcements? Commissioner Hailey.\n\nCommissioner Hailey: There will be a meeting of the Budget Committee to look at solid waste funding recommendations on Tuesday, July 16 at noon here in this room.\n\nChairman Wormsley: Any other announcements? The next meeting of this body will be Monday, August 19 at 7 p.m., here in this room. Commissioner Carmical.\n\nCommissioner Carmical: There will be a chili supper at County Elementary School on August 16 at 6:30 p.m. Everyone is invited.\n\nChairman Wormsley: Commissioner Austin.\n\nCommissioner Austin: Move adjournment.\n\nCommissioner Garland: Second.\n\nChairman Wormsley: Without objection, the meeting will stand adjourned.\n#End of meeting\n\nList of events in the meeting \n",
#  temperature=0.59,
#  max_tokens=400,
#  top_p=0.5,
#  frequency_penalty=0,
#  presence_penalty=0,
# best_of=1,
#  stop=None)
content = "Chairman Wormsley (at the proper time and place, after taking the chair and striking the gavel on the table): This meeting of the CTAS County Commission will come to order. Clerk please call the role. (Ensure that a majority of the members are present.)\n\nChairman Wormsley: Each of you has received the agenda. I will entertain a motion that the agenda be approved.\n\nCommissioner Brown: So moved.\n\nCommissioner Hobbs: Seconded\n\nChairman Wormsley: It has been moved and seconded that the agenda be approved as received by the members. All those in favor signify by saying \"Aye\"?...Opposed by saying \"No\"?...The agenda is approved. You have received a copy of the minutes of the last meeting. Are there any corrections or additions to the meeting?\n\nCommissioner McCroskey: Mister Chairman, my name has been omitted from the Special Committee on Indigent Care.\n\nChairman Wormsley: Thank you. If there are no objections, the minutes will be corrected to include the name of Commissioner McCroskey. Will the clerk please make this correction. Any further corrections? Seeing none, without objection the minutes will stand approved as read. (This is sort of a short cut way that is commonly used for approval of minutes and/or the agenda rather than requiring a motion and second.)\n\nChairman Wormsley: Commissioner Adkins, the first item on the agenda is yours.\n\nCommissioner Adkins: Mister Chairman, I would like to make a motion to approve the resolution taking money from the Data Processing Reserve Account in the County Clerk's office and moving it to the equipment line to purchase a laptop computer.\n\nCommissioner Carmical: I second the motion.\n\nChairman Wormsley: This resolution has a motion and second. Will the clerk please take the vote.\n\nChairman Wormsley: The resolution passes. We will now take up old business. At our last meeting, Commissioner McKee, your motion to sell property near the airport was deferred to this meeting. You are recognized.\n\nCommissioner McKee: I move to withdraw that motion.\n\nChairman Wormsley: Commissioner McKee has moved to withdraw his motion to sell property near the airport. Seeing no objection, this motion is withdrawn. The next item on the agenda is Commissioner Rodgers'.\n\nCommissioner Rodgers: I move adopton of the resolution previously provided to each of you to increase the state match local litigation tax in circuit, chancery, and criminal courts to the maximum amounts permissible. This resolution calls for the increases to go to the general fund.\n\nChairman Wormsley: Commissioner Duckett\n\nCommissioner Duckett: The sheriff is opposed to this increase.\n\nChairman Wormsley: Commissioner, you are out of order because this motion has not been seconded as needed before the floor is open for discussion or debate. Discussion will begin after we have a second. Is there a second?\n\nCommissioner Reinhart: For purposes of discussion, I second the motion.\n\nChairman Wormsley: Commissioner Rodgers is recognized.\n\nCommissioner Rodgers: (Speaks about the data on collections, handing out all sorts of numerical figures regarding the litigation tax, and the county's need for additional revenue.)\n\nChairman Wormsley: Commissioner Duckett\n\nCommissioner Duckett: I move an amendment to the motion to require 25 percent of the proceeds from the increase in the tax on criminal cases go to fund the sheriff's department.\n\nChairman Wormsley: Commissioner Malone\n\nCommissioner Malone: I second the amendment.\n\nChairman Wormsley: A motion has been made and seconded to amend the motion to increase the state match local litigation taxes to the maximum amounts to require 25 percent of the proceeds from the increase in the tax on criminal cases in courts of record going to fund the sheriff's department. Any discussion? Will all those in favor please raise your hand? All those opposed please raise your hand. The amendment carries 17-2. We are now on the motion as amended. Any further discussion?\n\nCommissioner Headrick: Does this require a two-thirds vote?\n\nChairman Wormsley: Will the county attorney answer that question?\n\nCounty Attorney Fults: Since these are only courts of record, a majority vote will pass it. The two-thirds requirement is for the general sessions taxes.\n\nChairman Wormsley: Other questions or discussion? Commissioner Adams.\n\nCommissioner Adams: Move for a roll call vote.\n\nCommissioner Crenshaw: Second\n\nChairman Wormsley: The motion has been made and seconded that the state match local litigation taxes be increased to the maximum amounts allowed by law with 25 percent of the proceeds from the increase in the tax on criminal cases in courts of record going to fund the sheriff's department. Will all those in favor please vote as the clerk calls your name, those in favor vote \"aye,\" those against vote \"no.\" Nine votes for, nine votes against, one not voting. The increase fails. We are now on new business. Commissioner Adkins, the first item on the agenda is yours.\n\nCommissioner Adkins: Each of you has previously received a copy of a resolution to increase the wheel tax by $10 to make up the state cut in education funding. I move adoption of this resolution.\n\nChairman Wormsley: Commissioner Thompson\n\nCommissioner Thompson: I second.\n\nChairman Wormsley: It has been properly moved and seconded that a resolution increasing the wheel tax by $10 to make up the state cut in education funding be passed. Any discussion? (At this point numerous county commissioners speak for and against increasing the wheel tax and making up the education cuts. This is the first time this resolution is under consideration.) Commissioner Hayes is recognized.\n\nCommissioner Hayes: I move previous question.\n\nCommisioner Crenshaw: Second.\n\nChairman Wormsley: Previous question has been moved and seconded. As you know, a motion for previous question, if passed by a two-thirds vote, will cut off further debate and require us to vote yes or no on the resolution before us. You should vote for this motion if you wish to cut off further debate of the wheel tax increase at this point. Will all those in favor of previous question please raise your hand? Will all those against please raise your hand? The vote is 17-2. Previous question passes. We are now on the motion to increase the wheel tax by $10 to make up the state cut in education funding. Will all those in favor please raise your hand? Will all those against please raise your hand? The vote is 17-2. This increase passes on first passage. Is there any other new business? Since no member is seeking recognition, are there announcements? Commissioner Hailey.\n\nCommissioner Hailey: There will be a meeting of the Budget Committee to look at solid waste funding recommendations on Tuesday, July 16 at noon here in this room.\n\nChairman Wormsley: Any other announcements? The next meeting of this body will be Monday, August 19 at 7 p.m., here in this room. Commissioner Carmical.\n\nCommissioner Carmical: There will be a chili supper at County Elementary School on August 16 at 6:30 p.m. Everyone is invited.\n\nChairman Wormsley: Commissioner Austin.\n\nCommissioner Austin: Move adjournment.\n\nCommissioner Garland: Second.\n\nChairman Wormsley: Without objection, the meeting will stand adjourned."
#print(response)

# choices = response.choices

# first = choices[0]
# firstText = first.text

# print(firstText)
def get_response(content, prompt_postfix):
    import tiktoken

    response_chunck = []
    n = 1000 # max tokens for chuncking
    max_tokens = 400 # max tokens for response

    tokenizer = tiktoken.get_encoding('p50k_base')

    # Generate chunkcs    
    chunks = chunk_generator(content, n, tokenizer)

    # Decode chunk of text
    text_chunks = [tokenizer.decode(chunk) for chunk in chunks]

    # Request api
    for chunk in text_chunks:
        response_chunck.append(request_api(chunk, prompt_postfix, max_tokens))
        #print(chunk)
        #print('>>> synopsis: \n' + synopsis_chunck[-1])

    # response
    response = ' '.join(response_chunck)

    return response

def chunk_generator(text, n, tokenizer):
    tokens = tokenizer.encode(text)
    i = 0
    while i < len(tokens):
        # Find the nearest end of sentence within a range of 0.5 * n and 1.5 * n tokens
        j = min(i + int(1.5 * n), len(tokens))
        while j > i + int(0.5 * n):
            # Decode the tokens and check for full stop or newline
            chunk = tokenizer.decode(tokens[i:j])
            if chunk.endswith(".") or chunk.endswith("\n"):
                break
            j -= 1
        # If no end of sentence found, use n tokens as the chunk size
        if j == i + int(0.5 * n):
            j = min(i + n, len(tokens))
        yield tokens[i:j]
        i = j
        
def request_api(document, prompt_postfix, max_tokens):
    prompt = prompt_postfix.replace('<document>',document)
    #print(f'>>> prompt : {prompt}')

    response = openai.Completion.create(  
        engine="curie",
        prompt=prompt,
        temperature=0,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1,
        stop='###')

    return response['choices'][0]['text']

prompt_categories = [
    "\nUnique speakers in the meeting\nSpeakers ",
    "\nAgenda discussed in the meeting\nAgenda items ",
    "\nResolutions reached in the meeting\nResolutions ",
    "\nWhat is next after the meeting\nNext Steps "
]

# Prompt postfix
prompt_postfix = """ <document>
  \n###
"""
#print(prompt_postfix)


for prompt in prompt_categories:
    print(prompt)
    prompt_with_postfix = prompt_postfix + prompt 
    response = get_response(content, prompt_with_postfix)
    print(response)
