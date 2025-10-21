iphone_messages = ['I am home now love', 'Get on dog!', 'Buy me some milk at the store please']

def show_messages(messages):
    for message in messages:
        print(f'message: {message}')

show_messages(iphone_messages)

sent_messages = []

def send_messages(unsent_messages, sent_messages):
    """Places the unsent message to sent message list."""
    while unsent_messages:
        sent_message = unsent_messages.pop()
        sent_messages.append(sent_message)
        print(f'Sending message: {sent_message}')

send_messages(iphone_messages[:], sent_messages)
print(iphone_messages)

