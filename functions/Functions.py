from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import regexp_tokenize
import random
import numpy as np

def tokenize(raw_text):
    """
    Convert raw text string to a list of tokens (words).
    :param raw_text: string
    :return: list of strings
    """
    word_pattern = r"[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+"
    stop_word_list = stopwords.words('english')
    token_text = regexp_tokenize(raw_text.replace('-', ' ').replace('_', ' ').replace('\n', ' '), word_pattern)
    token_text = [token.lower() for token in token_text if token.lower() not in stop_word_list and str(token).isalpha()]
    return token_text


def stem_lem_words(word_list, engine="word_net"):
    """
    :param word_list: a list of words
    :param engine: variable to choose between available stemmer
    :return: stemmed/lemmatized list of words
    """
    if engine == "porter":
        porter = PorterStemmer()
        return [porter.stem(word) for word in word_list]
    elif engine == "lancaster":
        lancaster = LancasterStemmer()
        return [lancaster.stem(word) for word in word_list]
    elif engine == "word_net":
        lem = WordNetLemmatizer()
        return [lem.lemmatize(word) for word in word_list]


def create_para(word_list, para_size=150):
    list_of_paragraphs = [' '.join(word_list[x:x+para_size]) for x in range(0, len(word_list), para_size)]
    return list_of_paragraphs

def create_select_para(word_list, para_size=150, num_para=200):
    starting_list = np.random.randint(0, high=len(word_list)-150, size=num_para, dtype='l')
    paragraphs = []
    for start in starting_list:
        paragraphs.append(' '.join(word_list[start:start+150]))
    return paragraphs


def select_random_para(list_para, num_para=200):
    if len(list_para) < num_para:
        return random.sample(list_para, len(list_para))
    else:
        return random.sample(list_para, num_para)
