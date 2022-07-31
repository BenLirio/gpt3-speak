from gpt3 import GPT3Client

AGENT_DESCRIPTION = "This is an agent returns the opposite"
AGENT_TRAINING = [
        ("tall","short"),
        ("fat","thin"),
        ("fast","slow"),
]

class Agent():
    def __init__(self):
        self.gpt = GPT3Client()
        self.history = AGENT_TRAINING.copy()

    def GetResponseOf(self, text):
        if len(self.history) > 5:
            self.history.pop(0)
        prompt = AGENT_DESCRIPTION 
        prompt += '\n"""\n'
        prompt += ''.join([f"> {a}\n{b}\n" for (a,b) in self.history])
        prompt += f"> {text}\n"
        response = self.gpt.Complete(prompt)
        self.history.append((text,response))
        return response
