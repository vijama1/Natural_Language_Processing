import nltk
import random
from nltk.corpus import movie_reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC
from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers=classifiers
    def classify(self,features):
        votes=[]
        for c in self._classifiers:
            v=c.classify(features)
            votes.append(v)
        return mode(votes)
    def confidence(self,features):
        votes=[]
        for c in self._classifiers:
            v=c.classify(features)
            votes.append(v)
        choice_votes=votes.count(mode(votes))
        conf=choice_votes/len(votes)
        return conf


documents=[]
documents=[(list(movie_reviews.words(fileid)),category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]
# for category in movie_reviews.categories():
#     for fileid in movie_reviews.fileids(category):
#         documents.append(list(movie_reviews.words(fileid)),category)
random.shuffle(documents)
#print(documents[1])
all_words=[]
for w in movie_reviews.words():
    w=w.lower()
    all_words.append(w)
all_words=nltk.FreqDist(all_words)
# print(all_words.most_common(15))
# print(all_words["stupid"])
word_features=list(all_words.keys())[:3000]
#print(word_features)

def find_features(document):
    words=set(document)
    features={}
    for w in word_features:
        features[w]=(w in words)
    return features
#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets=[(find_features(rev),category) for (rev,category) in documents]

training_set=featuresets[:1900]
testing_set=featuresets[1900:]

classifier=nltk.NaiveBayesClassifier.train(training_set)

#to load already trained data
# classifier_f=open("naivebayes.pickle","rb")
# classifier=pickle.load(classifier_f)
# classifier_f.close()

print("Naive Bayes Classifier Accuracy: ",nltk.classify.accuracy(classifier,testing_set))
classifier.show_most_informative_features(15)

#to prevent from training again and again
# save_classifier=open("naivebayes.pickle","wb")
# pickle.dump(classifier,save_classifier)
# save_classifier.cl
MNB_classifer=SklearnClassifier(MultinomialNB())
MNB_classifer.train(training_set)
print("MNB Classifier Accuracy: ",nltk.classify.accuracy(MNB_classifer,testing_set))

# GaussianNB_classifer=SklearnClassifier(GaussianNB())
# GaussianNB_classifer.train(training_set)
# print(nltk.classify.accuracy(GaussianNB_classifer,testing_set))

BernaulliNB_classifier=SklearnClassifier(BernoulliNB())
BernaulliNB_classifier.train(training_set)
print("Bernoulli Classifier Accuracy: ",nltk.classify.accuracy(BernaulliNB_classifier,testing_set))



LogisticRegression_classifer=SklearnClassifier(LogisticRegression())
LogisticRegression_classifer.train(training_set)
print("Logistic Regression Classifier Accuracy: ",nltk.classify.accuracy(LogisticRegression_classifer,testing_set))

SGD_classifer=SklearnClassifier(SGDClassifier())
SGD_classifer.train(training_set)
print("SGD Classifier Accuracy: ",nltk.classify.accuracy(SGD_classifer,testing_set))

SVC_classifer=SklearnClassifier(SVC())
SVC_classifer.train(training_set)
print("SVC Classifier Accuracy: ",nltk.classify.accuracy(SVC_classifer,testing_set))

LinearSVC_classifier=SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("Linear SVC Classifier Accuracy: ",nltk.classify.accuracy(LinearSVC_classifier,testing_set))

NuSVC_classifer=SklearnClassifier(NuSVC())
NuSVC_classifer.train(training_set)
print("NuSVC Classifier Accuracy: ",nltk.classify.accuracy(NuSVC_classifer,testing_set))


voted_classifier=VoteClassifier(classifier,MNB_classifer,BernaulliNB_classifier,LogisticRegression_classifer,SGD_classifer,LinearSVC_classifier,NuSVC_classifer)

print("Voted Classifier Accuracy: ",nltk.classify.accuracy(voted_classifier,testing_set))
print("Classification:",voted_classifier.classify(testing_set[0][0]),"confidence %",voted_classifier.confidence(testing_set[0][0]))
print("Classification:",voted_classifier.classify(testing_set[1][0]),"confidence %",voted_classifier.confidence(testing_set[1][0]))
print("Classification:",voted_classifier.classify(testing_set[2][0]),"confidence %",voted_classifier.confidence(testing_set[2][0]))
print("Classification:",voted_classifier.classify(testing_set[3][0]),"confidence %",voted_classifier.confidence(testing_set[3][0]))
print("Classification:",voted_classifier.classify(testing_set[4][0]),"confidence %",voted_classifier.confidence(testing_set[4][0]))
print("Classification:",voted_classifier.classify(testing_set[5][0]),"confidence %",voted_classifier.confidence(testing_set[5][0]))
