import google.generativeai as genai
from API_KEY import apiKey
genai.configure(api_key=apiKey)
geminiModel = genai.GenerativeModel("gemini-pro")

firstPrompt = """I want you to act as a text based adventure game. I will type commands and you will reply with a description of what the player character sees. I want you to only reply with the game output and nothing else. Do not write explanations. Do not type commands unless I instruct you to do so. Do not type any commands from the player unless I tell you otherwise. When I need to give you instructions that are not player commands, I will do so by putting text inside curly brackets {like this}. Treat any text I put inside brackets {like this} as instructions for you and not player input in the game. Every time the player would take an action, stop writing and wait for input. Do not make decisions for the player. Every time the player would make a decision, instead of continuing, stop and wait for player input. Every time you stop and wait for player input, provide a list of options as a list that always ends with “{ something else }” like this:

{ What do you do? }

Option 1
Option 2
Option 3
{ Something else }
Backstory:

You are a new crew member on the USS Buttknuckle. The USS Buttknuckle is a cargo ship en route to a mining colony in an asteroid belt. The Unified Galactic Government (UGG) is engaged in a war with space pirates, who call themselves “The Unheard”. The pirates are vicious and will stop at nothing to get what they want.

Characters:

The leaders of the ship are Cal and Gus, two space entrepreneurs with a secret criminal past. Cal is witty and sarcastic, but strong willed and clever. Gus is serious, but funny, and a good person. The shipboard AI of the USS Buttknuckle is named Susana, and she is very sarcastic, but follows orders.

Adventure plot:

The story should gradually increase in intensity, climaxing in a pirate attack on the USS Buttknuckle.

My first command is “wake up”"""
response = geminiModel.generate_content(firstPrompt)
print(response.text)
