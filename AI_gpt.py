import openai

openai.api_key = "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"

output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": "how to build a chat gpt bot in telegram using python ?"
    }]
)

print(output)