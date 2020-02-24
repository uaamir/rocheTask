
#Task 2 
# Aamir Khan


import pandas as pd 
from sklearn.model_selection import train_test_split 

import nltk
from nltk.corpus import stopwords

data = pd.read_json('Graduate - HEADLINES dataset (2019-06).json', lines=True)

print("Reading the JSON file", data.columns, data.shape)

# Splitting the dataset into train and test set
train, test = train_test_split(data,test_size = 0.1)
#train set
train_1 = train[ train['is_sarcastic'] == 1]
train_1 = train_1['headline']
train_0 = train[ train['is_sarcastic'] == 0]
train_0 = train_0['headline']
#test set
test_1 = test[ test['is_sarcastic'] == 1]
test_1 = test_1['headline']
test_0 = test[ test['is_sarcastic'] == 0]
test_0 = test_0['headline']

print("Data split into train and Test")

headlines= []
stopwords_set = set(stopwords.words("english"))

for index, row in train.iterrows():
    words_filtered = [e.lower() for e in row.headline.split() if len(e) >= 3]
    words_without_stopwords = [word for word in words_filtered if not word in stopwords_set]
    print(words_without_stopwords)
    headlines.append((words_without_stopwords, row.is_sarcastic))

# Extracting word features
def get_words_in_headlines(headlines):
    all = []
    for (words, sentiment) in headlines:
        all.extend(words)
    return all

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    features = wordlist.keys()
    return features
w_features = get_word_features(get_words_in_headlines(headlines))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in w_features:
        features['contains(%s)' % word] = (word in document_words)
    return features



# Training the Naive Bayes classifier
training_set = nltk.classify.apply_features(extract_features,headlines)
classifier = nltk.NaiveBayesClassifier.train(training_set)


count_0 = 0
count_1 = 0
for obj in test_0: 
    res =  classifier.classify(extract_features(obj.split()))
    if(res == 0): 
        count_0 = count_0 + 1
for obj in test_1: 
    res =  classifier.classify(extract_features(obj.split()))
    if(res == 1): 
        count_1 = count_1 + 1
        
percent_sarcastic = len(test_1)/count_1
percent_non_sarcastic = len(test_0)/count_0

print('[Not_sarcastic]: %s - %s/%s '  % (percent_non_sarcastic, len(test_0),count_0))        
print('[Sacrcastic]: %s - %s/%s '  % (percent_sarcastic,len(test_1),count_1))    


