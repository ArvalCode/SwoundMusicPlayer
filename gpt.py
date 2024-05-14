from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "I have 3 songs in my library named: hip hop, jazz, and lofi. I want you to rank the similarity of all these songs to a song named 'calm relaxing' based off the name alone. respond to this message with a list of these songs from most related to my song. Respond in list format song,song,song and nothing else."}],
    
)
print(response.choices[0].message.content)