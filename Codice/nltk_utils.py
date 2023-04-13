import numpy as np
import nltk
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("italian")


def tokenize(sentence):
    """
    divide la frase in un array di parole
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    stemming = trovare la radice di una parola
    esempi:
    parole = ["computer", "computare", "computabile", "computazionale"]
    parole = [stem(x) for x in parole]
    -> ["comput", "comput", "comput","comput"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    ritorna un array di bag of words:
    assegna 1 per ogni parola conosciuta che esiste nella frase, se la parola non esiste assegna 0
    esempio:
    frase = ["oggi", "é", "bel", "tempo"]
    words = ["ciao", "oggi", "é", "proprio", "bel", "tempo"]
    bog   = [  0 ,     1 ,    1 ,     0 ,      1 ,     1 ]
    """
    # stem ogni parola
    sentence_words = [stem(word) for word in tokenized_sentence]
    # inizializzo la bag a 0 per ogni parola
    bag = np.zeros(len(words), dtype=np.float32)

    # se la parola esiste nella frase, inserisce un 1
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag
