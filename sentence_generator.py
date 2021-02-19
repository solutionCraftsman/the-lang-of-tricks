
from random import randint
# from random import choice


def generate_sentence():
    articles = ("the", "a", "one", "some", "any")
    nouns = ("boy", "girl", "dog", "town", "car")
    verbs = ("drove", "jumped", "ran", "walked", "skipped")
    prepositions = ("to", "from", "over", "under", "on")

    random_number = randint(0, 4)
    article = str(articles[random_number])
    # article = str(choice(articles))
    article = article.capitalize()

    sentence_list = list()
    sentence_list.append(article)
    # sentence_list: list = []

    random_number = randint(0, 4)
    noun = str(nouns[random_number])
    sentence_list.append(noun)

    random_number = randint(0, 4)
    verb = str(verbs[random_number])
    sentence_list.append(verb)

    random_number = randint(0, 4)
    preposition = str(prepositions[random_number])
    sentence_list.append(preposition)

    random_number = randint(0, 4)
    article = str(articles[random_number])
    sentence_list.append(article)

    random_number = randint(0, 4)
    noun = str(nouns[random_number])
    sentence_list.append(noun)

    sentence = " ".join(sentence_list)
    sentence = sentence + "."

    return sentence


if __name__ == '__main__':
    for _ in range(20):
        print(generate_sentence())
