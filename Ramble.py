import os
import openai
import time

os.system('cls')
openai.api_key = os.getenv("OPENAI_API_KEY")

Model = "text-davinci-003"
Thought = input("What do you want me to think about? ")

while True:
  
    response = openai.Completion.create(
        model = Model,
        prompt = Thought,
        temperature = 0, #random.random(), #We on drugs, bro!
        max_tokens = 50,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    
    Thought = response.choices[0].text
    print()
    print("> "+Thought)
    time.sleep(5)
