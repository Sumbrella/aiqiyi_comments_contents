"""

"""
import matplotlib
import pandas
from _7Days.Day_5.CutWords import cut_words


def stopWords(path):
    stop_words = []
    with open(path, "r") as fp:
        for line in fp.readlines():
            stop_words.append(line.strip())
    return stop_words


def countWords(words, stop_words=None):
    if stop_words is None:
        stop_words = []
    count_result = {}
    for word in words:
        if word not in stop_words:
            if word not in count_result.keys():
                count_result.update({word: 1})
            else:
                count_result[word] += 1

    return count_result


def getTopTen():
    words = cut_words()
    words_dict = countWords(words)
    words_sort_list = sorted(words_dict, key=lambda x: words_dict[x], reverse=True)
    # print(words_sort_list)
    top_ten_list = {}
    i = 0
    for word in words_sort_list:
        if len(word) >= 2 and i < 10:
            top_ten_list.update({word: words_dict[word]})
            i += 1

    return top_ten_list


if __name__ == '__main__':
    res = getTopTen()
    print(res)

