import openai
import os
DEFAULT_MODEL_NAME = 'ada'
MODELS = {
        'ada': {
            'name': 'ada',
            'cost': 0.0008
        },
        'curie': {
            'name': 'text-curie-001',
            'cost': 0.0012
        },
        'curie': {
            'name': 'text-davinci-002',
            'cost': 0.0600
        },
        'davinci': {
            'name': 'text-davinci-002',
            'cost': 0.0600
        }
    }

class GPT3Client():
    def __init__(self,cost,model_name=DEFAULT_MODEL_NAME):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.model = MODELS[model_name]
        self.cost = cost
        
    def Complete(self, prompt):
        for _ in range(3):
            response = openai.Completion.create(
              model=self.model['name'],
              prompt=prompt,
              max_tokens=20,
              temperature=0,
              stop=[">"]
            ).choices[0].text.strip()
            self.cost.Add(len(list(response + prompt)) * self.model['cost'] * 0.25 * .001)
            if response == "":
                continue
            return response
        return "I don't understand"

