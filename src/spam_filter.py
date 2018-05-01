from __future__ import print_function, division
import nltk
import os
import random
from collections import Counter
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, DecisionTreeClassifier, classify

stoplist = stopwords.words('english')

def init_lists(folder):
    a_list = []
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file, 'r', errors="ignore")
        a_list.append(f.read())
    f.close()
    return a_list

def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(sentence)]

def get_features(text, setting):
    if setting=='bow':
        return {word: count for word, count in Counter(preprocess(text)).items() if not word in stoplist}
    else:
        return {word: True for word in preprocess(text) if not word in stoplist}

def init_train_set(features, samples_proportion):
    train_size = int(len(features) * samples_proportion)
    train_set, test_set = features[:train_size], features[train_size:]
    print ('Ukuran training set = ' + str(len(train_set)) + ' email')
    print ('Ukuran test set = ' + str(len(test_set)) + ' email')
    return train_set, test_set

def nbtrain(train_set):
    classifier = NaiveBayesClassifier.train(train_set)
    return classifier

def dttrain(train_set):
    # entropy_cutoff=0.05, depth_cutoff=100,
    # support_cutoff=10, binary=False, feature_values=None,
    # verbose=False
    classifier = DecisionTreeClassifier.train(train_set, depth_cutoff=10000)
    return classifier

def evaluate(train_set, test_set, classifier):
    print ('Accuracy (training set) = ' + str(classify.accuracy(classifier, train_set)))
    print ('Accuracy (test set) = ' + str(classify.accuracy(classifier, test_set)))
    
    classifier.show_most_informative_features(20)

if __name__ == "__main__":
    # initialise the data
    spam = init_lists('../data/email/spam/')
    ham = init_lists('../data/email/ham/')
    all_emails = [(email, 'spam') for email in spam]
    all_emails += [(email, 'ham') for email in ham]
    random.shuffle(all_emails)
    print ('Corpus size = ' + str(len(all_emails)) + ' emails')

    # extract the features
    all_features = [(get_features(email, ''), label) for (email, label) in all_emails]
    print ('Terkumpul ' + str(len(all_features)) + ' feature set')

    # initialize train set
    train_set, test_set = init_train_set(all_features, 0.8)
    
    # train the classifier with Naive Bayes & Decision Tree
    nb_classifier = nbtrain(train_set)
    print("NB DONE")
    # dt_classifier = dttrain(train_set)
    # print("DT DONE")

    evaluate(train_set, test_set, nb_classifier)
    
    while(1):
        message = input('enter email example:')
        if(message != "quit"):
            print("Naive Bayes Prediction: " + str(nb_classifier.classify(get_features(message, ''))))
            # print("Decision Tree Prediction: " + str(dt_classifier.classify(word_feats([message]))))
    
