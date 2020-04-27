"""

"""
import matplotlib.pyplot as plt
import numpy as np
from _7Days.Day_5.CountWords import getTopTen


def showFigure():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    top_ten = getTopTen()
    labels = list(top_ten.keys())
    print(labels)
    x = np.arange(0, 1000, 100)
    print(x)
    y = list(top_ten.values())
    plt.xticks(fontsize=10)
    plt.bar(x, y, align='center', tick_label=labels, alpha=0.8, width=80)
    plt.title("《青春有你2》评论词频统计")
    # plt.grid(axis='both', color='r', linestyle='--')
    plt.show()


if __name__ == '__main__':
    showFigure()