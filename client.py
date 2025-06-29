from openai import OpenAI
client = OpenAI (               #OpenAI here is creating an instance importing a class
    api_key="***",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
       {"role":"system", "content":"you are a virtual assistant named Jarvis skilled in general tasks like Alexa and google cloud "}, 
       {"role":"user","content":"What is json file "}
    ]
)
print(completion.choices[0].message.content)