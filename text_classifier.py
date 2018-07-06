import nltk
import random
from nltk.corpus import movie_reviews
import pickle
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
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets=[(find_features(rev),category) for (rev,category) in documents]

training_set=featuresets[:1900]
testing_set=featuresets[1900:]

classifier=nltk.NaiveBayesClassifier.train(training_set)

#to load already trained data
# classifier_f=open("naivebayes.pickle","rb")
# classifier=pickle.load(classifier_f)
# classifier_f.close()

print(nltk.classify.accuracy(classifier,testing_set))
classifier.show_most_informative_features(15)

#to prevent from training again and again
# save_classifier=open("naivebayes.pickle","wb")
# pickle.dump(classifier,save_classifier)
# save_classifier.close()
