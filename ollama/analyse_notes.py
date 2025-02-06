import os
import gzip
import json

import ollama
from ollama import chat
from ollama import ChatResponse

# Function to read JSON data from a gzipped file
def read_json_gz(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as gz_file:
        json_data = json.load(gz_file)
    return json_data

notes_rows = read_json_gz("asclepius_notes.json.gz")
notes = [x["note"] for x in notes_rows]

#print(ollama.list())

for note in notes[:5]:
    prompt = f'Here is a clinical note, please analyze it for the presence of medical implants. Answer as a JSON object with the format {{"has_implant": true/false, "implant": ""/"pacemake"}}: {note}'
    response: ChatResponse = chat(model='phi4:latest', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)

