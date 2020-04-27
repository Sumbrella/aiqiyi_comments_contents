"""

"""

import jieba
from tkinter import _flatten

def cut_words():
    # jieba.load_userdict("add_words.txt")
    words = []
    with open("cleared_comments.txt", "r") as fp:
        for line in fp.readlines():
            words.append(jieba.lcut(line))
    words = list(_flatten(words))
    return words


if __name__ == "__main__":
    # jieba.add_word()
    words = cut_words()
    print(words)