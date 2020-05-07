import random
import tkinter as tk

root = tk.Tk()

output = tk.Label(root, text='Hello')
output.pack()

user_input = tk.Entry(root)
user_input.pack()

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
huh = "I did not understand what you said"

def cb(event):
    user_text = user_input.get()
    if user_text in greetings:
        bot_text = random.choice(greetings)
    elif user_text in question:
        bot_text = random.choice(responses)
    else:
        bot_text = huh
    output.config(text=bot_text)

user_input.bind("<Return>", cb)


tk.mainloop()
