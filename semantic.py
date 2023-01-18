import spacy

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


'''
It is interesting that cat and monkey are similar despite not sharing any letters. 
It must be the case that they are similar in some other way.

'''

nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
The results are different when using the smaller model.
The smaller model is faster but less accurate, and suggests the words are much more similar)

'''