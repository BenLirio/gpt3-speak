from text_to_speech import TextToSpeechClient
import os
import signal
from agent import Agent
from cost import Cost

AGENT_DESCRIPTION = "This is an agent returns the opposite"
AGENT_TRAINING = [
        ("tall","short"),
        ("fat","thin"),
        ("fast","slow"),
]
PITCH = 0
SPEAKING_RATE = 1


cost = Cost()
ttp = TextToSpeechClient(cost,pitch=PITCH,speaking_rate=SPEAKING_RATE)
agent = Agent(cost, agent_description=AGENT_DESCRIPTION, agent_training=AGENT_TRAINING)

def on_exit(signum, frame):
    print("\nGoodbye")
    print(cost.ToString())
    exit()
signal.signal(signal.SIGINT, on_exit)

while True:
    text = input("> ")
    response = agent.GetResponseOf(text)
    print(response)
    ttp.Say(response)
