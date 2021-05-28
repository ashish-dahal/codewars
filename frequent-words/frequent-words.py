import collections


def top_3_words(text):
    return [i[0] for i in collections.Counter(text.translate(text.maketrans('!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', '                               ', )).lower().split()).most_common(3) if i[0] not in "'"*100]
