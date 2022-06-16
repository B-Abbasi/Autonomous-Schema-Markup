# helperFunctions.py
import pandas as pd
import numpy as np
import re


# function to remove special characters
def remove_special_characters(text):
    # define the pattern to keep
    pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 
    pat = r'[^a-zA-z0-9\s]' 
    return re.sub(pat, '', text)

def removeTrailingSpaces(text):
    text = text.strip()
    return text
    
    
def fetchFeatureEmbeddings(df):
  featuresEmbeddings = pd.DataFrame()

  for i, r in df.iterrows():
    _t = pd.DataFrame( calculateSentenceEmbedding(r[0].lower().replace('-',' ').split(' ')))
    _t = fetchMeanOfEmbeddings(_t)
    featuresEmbeddings =pd.concat([featuresEmbeddings, _t], axis=1)
  

  featuresEmbeddings = featuresEmbeddings.transpose()
  featuresEmbeddings.index = df.index.values
  return featuresEmbeddings


def calculateSentenceEmbedding(sentence):
  sent_embedding = np.zeros((len(sentence),50))
  for i in range(0, len(sentence)):
    sentence[i] = removeTrailingSpaces( remove_special_characters(sentence[i]))
    if(len(sentence[i])>2):
      sent_embedding[i] = glove_model[sentence[i]]
  return sent_embedding


def fetchMeanOfEmbeddings(emb):
  emb =  emb.mean(axis=0)
  return emb