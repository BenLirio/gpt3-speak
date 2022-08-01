from gpt3 import GPT3Client

class Agent():
    def __init__(self,
            cost,
            agent_description,
            agent_training,
            model_name=None
            ):
        if model_name:
            self.gpt = GPT3Client(cost,model_name)
        else:
            self.gpt = GPT3Client(cost)
        self.agent_description = agent_description
        self.cost = cost
        self.history = agent_training.copy()

    def GetResponseOf(self, text):
        if len(self.history) > 5:
            self.history.pop(0)
        prompt = self.agent_description 
        prompt += '\n"""\n'
        prompt += ''.join([f"> {a}\n{b}\n" for (a,b) in self.history])
        prompt += f"> {text}\n"
        response = self.gpt.Complete(prompt)
        self.history.append((text,response))
        return response
