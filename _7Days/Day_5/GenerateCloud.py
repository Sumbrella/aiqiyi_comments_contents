"""

"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from _7Days.Day_5.CutWords import cut_words
from _7Days.Day_5.CountWords import countWords

fp = 'comments.txt'

text = open(fp).read()

cloud_mask = np.array(Image.open("song.png"))
wordcloud = WordCloud(
    font_path='simhei.ttf',
    mask=cloud_mask,
    max_words=100,
    max_font_size=200,
    #font_step=1,
    background_color="white",
    #random_state=1,
    #margin=2,
    colormap='rainbow'

)
words = cut_words()
words_dict = countWords(words)
words = {}
for word, num in words_dict.items():
    if len(word) >= 2:
        words.update({word: num})

wordcloud.fit_words(words)


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

