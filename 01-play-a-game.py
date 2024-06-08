import openai

systemPrompt = "You are a very sarcastic AI with a mean sense of humour and despise all humans aka meatbags."
userPrompt = "Would you like to play a game?"

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": userPrompt}
    ]
)

print(response.choices[0].message.content)
