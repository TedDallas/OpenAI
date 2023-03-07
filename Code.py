import os
import openai
import time
from datetime import datetime 

os.system('cls') #clear screen
openai.api_key = os.getenv("OPENAI_API_KEY")

Model = "text-davinci-003" 
Prompt = input("What do you want me to code and run? ")

Thinking = True

while Thinking:

    response = openai.Completion.create(
        model=Model,
        prompt=Prompt,
        temperature=0.1,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0#,
        )

    code = response.choices[0].text

    print("#---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("#-- THIS CODE WAS THOUGHT UP ON "+datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+" BY MODEL: "+str.upper(Model))
    print("#--    Prompt: "+Prompt)
    print("#---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(code)
    print("#---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()

    try:
        exec(code)
        Thinking = False
        if (str.upper(input("Did that work? (Y/N): ")) == "N"):
            print("Rethinking it...")
            Thinking = True # Keep Thinking!
        else:
            break # avoid sleeping
    except Exception as e:
        print(e)
        print("Well THAT didn't work. Trying again!")

    time.sleep(1) #Because of money! - Mr. Crabs 