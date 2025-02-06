import json
from ollama import chat
from ollama import ChatResponse

with open("ollama/asclepius_notes.json") as fp:
    notes = json.load(fp)

for note in notes:
    prompt = f'Here is a clinical note, please analyze it for the presence of medical implants. Answer as a JSON object with the format {{"has_implant": true/false, "implant": ""/"pacemake"}}: {note}'
    response: ChatResponse = chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
