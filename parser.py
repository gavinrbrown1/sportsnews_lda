# ok, now we've got the text files woth words, now what?

from nltk.tokenize import TreebankWordTokenizer
from nltk.stem.porter import PorterStemmer

from stop_words import get_stop_words

def parse():

    # import my index of files
    index = open('file_index.txt', 'r')
    file_index = index.read().split()

    # list of lists of tokens
    documents = []

    for filename in file_index:
        file = open(filename)
        text = file.read().lower()
        file.close()

        # not perfect, unfortunately. Regexes might make it smarter
        tokens = TreebankWordTokenizer().tokenize(text)

        # remove words of length 1, for periods and commas
        tokens = [w for w in tokens if len(w) > 1]

        # stop words from the package, as well as my additions
        stopwords = get_stop_words('en')
        additions = ['n\'t']
        stopwords = stopwords + additions
        tokens = [t for t in tokens if t not in stopwords]

        # now stemming
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(w) for w in tokens]

        # now some additional cleaning
        tokens = [t for t in tokens if t not in ['\'s', '\'\'']]

        # and add to the total list
        documents.append(tokens)

    return(documents)

documents = parse()

# for d in documents:
#     for w in d:
#         print(w, end=' ')
#     print()
#     print()

# dirty but it will do
