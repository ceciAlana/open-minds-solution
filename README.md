# open-minds-solution
Team Open Minds' main repository for the 2023 Engineering Hubs AI Jam hackathon.

Install the following 
```
pip install flask
pip install openai
pip install tiktoken
pip install python-dotenv
```

Example .env file
```
AZURE_OPENAI_ENDPOINT=https://open-minds-ai.openai.azure.com/
AZURE_OPENAI_API_KEY=<<YOUR API KEY>>
AZURE_OPENAI_DEPLOYMENT_NAME=<<YOUR DEPLOYED MODEL NAME>>
OPEN_AI_API_VERSION=2022-12-01

```

To use flask / run server
```
pip install flask
flask run
```

Run teams bot 

```
navigate to /bot directory
npm i
npm start
```

Testing in teams
```
- to start the Teams, open the /bot dir in another vs code window
- go to run and debug / Ctrl+Shift+D and choose (Launch Remote (Chrome)) and click green arrow (it will launch), you might need to install teams toolkit extension - but i think itll let you know in the console 
- login to teams with credentials
- there is already a meeting where i added the the bot, you can just join that meeting to test it
```
