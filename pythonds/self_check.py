import string
from random import choice


def gen_phrase(strlen):
    phrase = ''
    letter = string.ascii_lowercase + ' '
    for l in range(strlen):
        phrase = phrase + choice(letter)
    return phrase


def compare(base, teststring):
    num = 0
    for i in range(len(base)):
        if base[i] == teststring[i]:
            num += 1
    return num/len(base)


def main():
    goal = 'methinks it is like a weasel'
    new_str = gen_phrase(28)
    best = 0
    newscore = compare(goal, new_str)
    while newscore < 1:
        if newscore > best:
            print(newscore, new_str)
            best = newscore
        new_str = gen_phrase(28)
        newscore = compare(goal, new_str)


main()
