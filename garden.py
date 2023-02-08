import spacy

nlp = spacy.load("en_core_web_sm")

# Find at least 5 garden path sentences from the web or think up your own.
# Store the sentences you have identified or created in a list called gardenpathSentences

gardenpathSentences = [
    "The pope (Latin: papa, from Greek: πάππας, romanized: pappas, 'father'), also known as supreme pontiff (pontifex maximus or summus pontifex), Roman pontiff (Romanus pontifex) or sovereign pontiff, is the bishop of Rome (or historically the patriarch of Rome), head of the worldwide Catholic Church, and has also served as the head of state or sovereign of the Papal States and later the Vatican City State since the eighth century.",  # Test sentence, from wikipedia
    "Communism (from Latin communis, 'common, universal') is a left-wing sociopolitical, philosophical, and economic ideology and current within the socialist movement, whose goal is the establishment of a communist society, a socioeconomic order centered around common ownership of the means of production, distribution, and exchange that allocates products to everyone in the society.",  # Test sentence, from wikipedia
    "The raft floated down the river sank.",
    "The horse raced past the barn fell.",
    "The man who whistled tunes pianos.",
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "The prime number few.",
    "The man who hunts ducks out on weekends.",
    "Until the police arrest the drug dealers control the street.",
]

# Tokenise each sentence in the list and perform entity recognition.

# Encountering errors with entity recognition
for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    print(
        [token.orth_ for token in nlp_sentence if not token.is_punct | token.is_space]
    )

    print([(entity, entity.label_, entity.label) for entity in nlp_sentence.ents])
    # does not recognize any entities within the garden path sentences


# Examine how spaCy has categorised each sentence. Then, use spacy.explain to look up and print the meaning of entities that you don’t understand. For example:print(spacy.explain("FAC"))
print(spacy.explain("NORP"))
print(spacy.explain("ORG"))
print(spacy.explain("GPE"))

# At the bottom of your file, write a comment about two entities that you looked up. For each entity answer the following questions

# What was the entity and its explanation that you looked up?
# "NORP", explained as "Nationalities or religious or political groups"

# Did the entity make sense in terms of the word associated with it?
# Yes, as things such as "communism", "Latin",  and "Greek" are all correctly categorized into this entity, and are a political group and nationalities respectively

# What was the entity and its explanation that you looked up?
# "GPE", explained as "Countries, cities, states"

# Did the entity make sense in terms of the word associated with it?
# Yes, GPE was associated with "Vatican City State", "Rome", "the Papal States"
