import nltk
from nltk.corpus import treebank

sentence = """The method which is used by Roland Hartanto is wrong."""
tokens = nltk.word_tokenize(sentence)
print("Tokens: ")
print(tokens)

tagged = nltk.pos_tag(tokens)
print("Tagged Sentence: ")
print(tagged)

entities = nltk.chunk.ne_chunk(tagged)
print("Named Entities: ")
print(entities)