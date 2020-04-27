# 爬取爱奇艺评论、进行词频统计。

## 运行顺序
- CrawCommons.py **爬取评论(爱奇艺《青春有你2》评论)，将评论储存到当前目录的"comments.txt"文件夹中**
- CountWords.py **统计词频** 包含函数stopWords, countWords, getTopTen.详情见文件
- ClearSpecialChar.py **删除特殊字符等** 将删好的文件储存在当前目录的"cleared_comments.txt"中。
- GenerateCloud.py **根据词频生成词云**
- ShowFigure()**展示前十名的柱状图**
