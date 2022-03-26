import numpy as np
import pandas as pd 
import json
import nltk
from nltk import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords #used to extract repetitve words with less unimportant meaning
import re #used to regularize - meaning removing punctuations
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.feature_extraction.text import TfidfVectorizer
import random
import pickle
from tqdm.notebook import trange # https://tqdm.github.io/

with open('intents_NEW.json','r') as infile:
    intents=json.load(infile)
with open('vocabulary_NEW.json','r') as infile:
    vocabulary=json.load(infile)
with open('tags_NEW.json','r') as infile:
    tags=json.load(infile)
    
lemma_object= WordNetLemmatizer()

def bag_of_words(tokenized_pattern,vocabulary): #Accepts vocabulary which is the prepared Json file
    tokenized_pattern=[lemma_object.lemmatize(word) for word in tokenized_pattern ]
    bag= np.zeros(len(vocabulary),dtype=int)
    #One Hot Encoding
    for i, word in enumerate(vocabulary):
        if word in tokenized_pattern:
            bag[i]=1
    return bag

f = open('MultiNaive_NEW.pickle', 'rb')
disease_detect_model = pickle.load(f)
f.close()

bot_name = "Dr.Stone"

def reply(message):
    words = nltk.word_tokenize(message.lower())#Tokenize input sentence
    bag = bag_of_words(words,vocabulary) # One Hot encoding
    bag = np.reshape(bag,(-1,1)) # Reshaping
    bag = np.transpose(bag) # Transpose
    prediction=disease_detect_model.predict(bag) #Predicting the output
    label=tags[prediction[0]]
    for intent in intents['intents']:
        if label == intent['tag']:
            return intent["responses"][0]
            
    return "No understando"
    

