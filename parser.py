# ok, now we've got the text files woth words, now what?

from nltk.tokenize import TreebankWordTokenizer
from nltk.stem.porter import PorterStemmer

from stop_words import get_stop_words

def parse():

    # import index of all the files
    index = open('data/file_index.txt', 'r')
    file_index = index.read().split()

    # list of lists of tokens
    documents = []

    for filename in file_index:
        # dump file to string
        file = open('data/' + filename)
        text = file.read().lower()
        file.close()

        # tokenizer not perfect, unfortunately.
        #   Regexes are harder but probably better
        tokens = TreebankWordTokenizer().tokenize(text)

        # remove words of length 1 (mainly periods and commas)
        tokens = [w for w in tokens if len(w) > 1]

        # stop words from the package, as well as my additions
        stopwords = get_stop_words('en')
        additions = ['n\'t', '\'s', '\'\'', '``', 'will']
        stopwords = stopwords + additions
        tokens = [t for t in tokens if t not in stopwords]

        # now stem everything
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(w) for w in tokens]

        # and add to the total list
        documents.append(tokens)

    return(documents)

# documents = parse()

# for d in documents:
#     for w in d:
#         print(w, end=' ')
#     print()
#     print()

# dirty, but it will do
