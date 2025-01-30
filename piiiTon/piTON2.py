def show_messages(messages):
    for message in messages:
        print(message)
    while text_messages:
        x = text_messages.pop()
        sent.append(x)
    print('from', text_messages, 'in', sent)
text_messages = [
    "Hello there!",
    "How are you doing?",
    "Python is awesome!",
    "Remember to drink water.",
    "Have a great day!"
]
sent = []
show_messages(text_messages)