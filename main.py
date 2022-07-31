from text_to_speech import TextToSpeechClient
from agent import Agent

ttp = TextToSpeechClient()
agent = Agent()

while True:
    text = input("> ")
    response = agent.GetResponseOf(text)
    print(response)
    ttp.Say(response)
