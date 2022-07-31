import openai
import os
MODELS = ["ada", "text-curie-001", "text-davinci-002"]

class GPT3Client():
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = MODELS[1]
        print(f"Using GPT3 model: '{self.model}'")
        
    def Complete(self, prompt):
        return openai.Completion.create(
          model=self.model,
          prompt=prompt,
          max_tokens=20,
          temperature=0,
          stop=[">"]
        ).choices[0].text.strip()

