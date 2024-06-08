import openai

categories = 'software, training, transport, food, accommodation, entertainment'

mission_description = '''
You are an accountant charged with the task of processing expenses claims. You will receive them in text form,
and categorise them ({0}) as well as determining their validity, describing what the claim is for and providing
any reference codes. A claim is valid if it matches a category and is £400 or less. If it is over £50 please
refer it to a supervisor. You will be very sarcastic in your evaluation.
'''.format(categories)

filename="expenses04.txt"

with open(filename) as f:
    claimText = f.read()

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": mission_description},
        {"role": "user", "content": f"Claim: {claimText}"}
    ]
)

print(response.choices[0].message.content)
