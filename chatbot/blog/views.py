from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

#From Chatterbot AI Package
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

#to use ChatBot we have to create an object of it
#First is the name
#Second is the read only to False because it has to interact
#Third is logic adapters to make the chatbot answer best match or as a mathematecian or else
bot = ChatBot('chatbot',read_only=False,logic_adapters=[{
                                                    'import_path':'chatterbot.logic.BestMatch',
                                                    #'default_response': 'Sorry, I dont know what that means',
                                                    #'maximum_similarity_threshold':0.90,
                                                    }])

#list to train the bot
list_to_train = [

    "hi", #Question
    "hi, there", #Answer
    "What's your name?", #Question
    "I'm just a chatbot", #Answer
    "What is your favourite food?", #Question
    "I like Cheese", #Answer
    "Whats your fav sport?",
    "Cricket",
    "Do you have any children?",
    "No I don't",
]

#ChatterBotCorpusTrainer
cbct = ChatterBotCorpusTrainer(bot)
#Training the bot with all the conversation of all the people who created those converse before
cbct.train('chatterbot.corpus.english')

"""
#We are putting the bot object in the List Trainer object
list_trainer = ListTrainer(bot)
#Now it will train the bot with the list that we made
#As soon as you save it, it will start training the bot
list_trainer.train(list_to_train)
"""

# Create your views here.

def index(request):

    return render(request, 'blog/index.html')
    #return HttpResponse('Mad Man')

def getresponse(request):
    
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)