import requests

api_key = "SA8xF8f0RHqa9BMj"
bot_id = "168961"

def get_response(message, external_id):
    url = f"https://www.personalityforge.com/api/chat/?apiKey={api_key}&chatBotID={bot_id}&message={message}&externalID={external_id}"
    r = requests.get(url)
    response = r.json()
    if response['success'] == 1:
        return response['message']['message']
    else:
        return "Error: " + response['errorMessage']

external_id = "user"

while True:
    message = input("You: ")
    if message.lower() == 'bye':
        print("Bot: Bye!")
        break
    print("Bot:", get_response(message, external_id))
