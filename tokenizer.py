from nltk.tokenize import sent_tokenize,word_tokenize
example_text="Hello Mr. smith,how are you? the weather is great and python is awesome. The sky is looking blue"
print(sent_tokenize(example_text))
print("--------------------")
print(word_tokenize(example_text))
