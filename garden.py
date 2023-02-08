import spacy

nlp = spacy.load("en_core_web_sm")
# Find at least 5 garden path sentences from the web or think up your own.
# Store the sentences you have identified or created in a list called gardenpathSentences

gardenpathSentences = [
    "The raft floated down the river sank.",
    "The horse raced past the barn fell.",
    "The man who whistled tunes pianos.",
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "The prime number few.",
    "The man who hunts ducks out on weekends.",
    "Until the police arrest the drug dealers control the street.",
]

# ●Tokenise each sentence in the list and perform entity recognition.

for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    print([(w.text, w.pos_) for w in nlp_sentence])
    # print([(i, i.label_, i.label) for i in nlp_sentence])
    # print([token.orth_ for token in nlp_sentence if not token.is_punct | token.is_space])


# ●Examine how spaCy has categorised each sentence. Then, use spacy.explain to look up and print the meaning of entities that you don’t understand. For example:print(spacy.explain("FAC"))
# ●At the bottom of your file, write a comment about two entities that you looked up. For each entity answer the following questions:
# ○What was the entity and its explanation that you looked up?
# ○Did the entity make sense in terms of the word associated with it?

# ●Host your solution on GitHub
#  Dockerfile
# README.md with instructions
# requirements.txt to automate the installation of the project’s requirements.
# exclude any venv or virtualenv files from your repo.
# ●Link to your public remote Git repo in a file named nlp.txt in your Dropbox folder.
