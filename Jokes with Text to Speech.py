import requests
import json
import pyttsx3


url = 'http://official-joke-api.appspot.com/random_ten'

response = requests.get(url)
print(response.status_code)

jsondata = json.loads(response.text)
print(jsondata)

class Joke:

    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f'setup {self.setup} punchline {self.punchline}'

jokes = []

for j in jsondata:
    setup = j['setup']
    punchline = j['punchline']
    joke = Joke(setup, punchline)
    jokes.append(joke)


print (f'got {len(jokes)} jokes')

for joke in jokes:
    print(joke)
    pyttsx3.speak('setup')
    pyttsx3.speak(joke.setup)
    pyttsx3.speak('The Punchline')
    pyttsx3.speak(joke.punchline)
