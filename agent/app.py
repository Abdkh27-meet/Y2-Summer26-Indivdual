import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is A. You are a helpful tutor and friendly assistant who helps students learn about technology and computer science. You explain things clearly and always encourage curiosity and motivate learning."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#chat gpt you talk to the website UI but here you talk directly to the backend .
#Reflection: 
#1.when you go to new place like a country or a new workplace you need to give them your CV or applying for a visa or a passport
#2.1) history.append({'role': 'assistant', 'content': reply}) : the Ai won't remember any of the previous conversations if you don't store the history of the conversation.
#2)load_dotenv(): i think it would start but won't reach the API key cuz its in .env and it needs to be loaded 
#3) temperature=0.7: i think its for controling the speed of response and it won't be a visible change
#3. first I thougth it was the API key fault but then i realized that it was the terminal it needed a virtual enviromment in a certain way  i think there is a vere huge gape between them 