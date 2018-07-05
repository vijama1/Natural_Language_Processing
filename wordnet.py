from nltk.corpus import wordnet

syns=wordnet.synsets("program")
#gives definition of program
print(syns[0].definition())

#gives example of program
print(syns[0].examples())

synonyms=[]
antonyms=[]

#prints antonym and synonym of good
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)
print(synonyms)

w1=wordnet.synset("ship.n.01")
w2=wordnet.synset("ship.n.01")
#print similarity between two words
print(w1.wup_similarity(w2))
