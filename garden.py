# importing libraries/modules requires download
import spacy

nlp = spacy.load('en_core_web_sm')

sentence_1 = "While I was surfing Reddit went down."
sentence_2 = "While Tom was washing the dishes fell on the floor."
sentence_3 = "Dave sleeps with Helen and Laura gets a new job."
sentence_4 = "The cotton clothing is made of grows in Mississippi."
sentence_5 = "Mary gave the child the dog bit a Band-Aid."

# store the strings in a list, so we can iterate through them at the same time.
garden_path_sentences = [sentence_1, sentence_2, sentence_3, sentence_4,
                         sentence_5]

for sentence in garden_path_sentences:
    print(sentence)

    # Tokenization
    doc = nlp(sentence)
    print([token.orth_ for token in doc])

    # Entity recognition
    garden_doc = nlp(sentence)
    print([(i, i.label_, i.label) for i in garden_doc.ents])

# asking spaCy what the different entity tags mean and printing the results
print(spacy.explain("GPE"))
print(spacy.explain("NORP"))
print(spacy.explain("ORG"))

# For my first sentence spaCy recognised the entity "Reddit" as falling into
# the Nationalities or religious or political groups, I was surprised as I
# don't think of "Reddit" as any of those things, it's a website.

# For the third sentence the name "Helen" is recognised as either a company,
# agency or institution but in this content it's just the name of a person.


