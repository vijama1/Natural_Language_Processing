import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import string
tokens=[]
final_list=[]
punctuation=[]
invalid_words=['a','an','the','is','explain','define','meaning','give','example','examples','am','are','this','that','do','please','would','you','of','me','could','show','present','my','what','who','me','my','','tell','hey','all','in','under','then','will','would','for','there','command','find','my','run','execute','tell','year']

def find_meaning(user_input):
    for i in user_input.split():
        if i not in stopwords.words('english'):
            tokens.append(i)
    for j in tokens:
        if j not in invalid_words:
            final_list.append(j)
    for k in final_list:
        if k not in string.punctuation:
            punctuation.append(k)
    user_command=' '.join(punctuation)
    if 'explain' in user_input.split():
        books=wordnet.synsets(user_command)
        number_of_examples=len(books[0].examples())
        definition=books[0].definition()
        print("----------------------------------------------------")
        print("Definition: "+str(definition))
        print("----------------------------------------------------")
        j=1
        for i in books[0].examples():
            print("----------------------------------------------------")
            print("Example "+str(j)+":"+str(i))
            print("----------------------------------------------------")
            j=j+1
            print("Press y for more examples any other button otherwise")
            more_examples=input("Do you want another exmple:")
            if more_examples=="y":
                pass
            else:
                break
        
    if 'define' in user_input.split() or 'definition' in user_input.split():
        # print("only definition")
        definition=books[0].definition()
        print("----------------------------------------------------")
        print("Definition: "+str(definition))
        print("----------------------------------------------------")
        #print("Definition: "+str(definition))
    if 'example' in user_input.split() or 'examples' in user_input.split():
        #print("only examples")
        books=wordnet.synsets(user_command)
        j=1
        for i in books[0].examples():
            print("----------------------------------------------------")
            print("Example "+str(j)+":"+str(i))
            print("----------------------------------------------------")
            j=j+1
            print("Press y for more examples any other button otherwise")
            more_examples=input("Do you want another exmple:")
            if more_examples=="y":
                pass
            else:
                break
