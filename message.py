import random
from nltk.corpus import wordnet as wn
def synonym(word, pos=None):
    arr=[]
    _pos=wn.ADJ
    if pos == 'NOUN':_pos=wn.NOUN
    if pos == 'VERB':_pos=wn.VERB

    synset_arrays = wn.synsets(word, pos=_pos)
    for synset_array in synset_arrays:
        for i in synset_array.lemma_names():
            arr.append(i)
    msg=random.choice(arr).replace("_", " ")
    return msg