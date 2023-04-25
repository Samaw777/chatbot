from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import tensorflow as tf
from tensorflow.keras.models import load_model

# Create your views here.

def homepage(request):
    return render(request, 'mainchat/homepage.html')

def home(request):
    if request.method == 'POST':
        return redirect('mainchat-home')  

    return render(request, 'mainchat/home.html')

def output(request):  
    return render(request, 'mainchat/output.html')
def login(request):
    return render(request, 'mainchat/login.html')
def signup(request):
    return render(request, 'mainchat/signup.html')
def afterlogin(request):
    return render(request, 'mainchat/afterlogin.html')
def chatpaneltest(request):
    return render(request, 'mainchat/chatpaneltest.html')


#Chatbot ruterning function
#LOAD and usemodel
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np


from keras.models import load_model

model = load_model('mainchat/chatbot_model.h5')
import json
import random

intents = json.loads(open('mainchat/intents.json').read())
words = pickle.load(open('mainchat/words.pkl', 'rb'))
classes = pickle.load(open('mainchat/classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return (np.array(bag))


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if (i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result
#Break

#Calling the chatbot
def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

#Get Chatbot Respond
def get_Response(request):

    userMessage = request.GET.get('userMessage')
    chat_response = str(chatbot_response(userMessage))
    return HttpResponse(chat_response)