import nltk
from nltk.chat.util import Chat, reflections

pairs=[
    #
    [
        r"my name is (.)",
        ["Hello %1, How are you"]
    ],
    # Or expression
    [
        r"Hi|Hello|Hey there|Hola",
        ["Hello ","hii"]
    ],
    [
        r"what is your name ?",
        ["I am a bot . you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"I (.*) good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude Seriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Kartik created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['pune',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of cricket",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Rohit","virat"]
    ],
    [
        r"quit",
        ["Thank you for using our intelligence services"]
    ],
    

]

def chat():
    print("Hey i am chatbot! how can i help you :")
    chat = Chat(pairs)
    chat.converse()

if __name__== "__main__":
    chat()