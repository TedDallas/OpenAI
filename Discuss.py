import os
import openai

os.system('cls')
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_prompt()->str:
  return str.strip(input())

Prompt = get_prompt() 

while str.upper(Prompt) != "EXIT":

  Model = "text-davinci-003"

  response = openai.Completion.create(
    model = Model,
    prompt = Prompt,
    temperature = 0.5,
    max_tokens = 4000,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
  )

  if (len(response.choices) > 0):
    print(response.choices[0].text)
  else:
    print(response)

  print()
  Prompt = get_prompt()
  print()
