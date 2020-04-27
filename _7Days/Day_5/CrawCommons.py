"""

"""

import requests
import json


def getLastIdAndSave(ori_url, lastID=0):
    url = ori_url + str(lastID)
    response = requests.get(url)
    string = str(response.text)
    js_res = json.loads(string)
    # print(js_res)
    # print(js_res['data']['comments'])
    total = 0
    for comment in js_res['data']['comments']:
        if 'content' in comment.keys():
            content = comment['content']
            with open('comments.txt', 'a+') as fp:
                fp.write(content+'\n')
            lastID = comment['id']
            total += 1
    return lastID, total


if __name__ == '__main__':
    times = 100
    lastID = 0
    num = 0
    url = "https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.11.5&authcookie=null&business_type=17&content_id=15068699100&hot_size=10&last_id="
    # url = "https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.11.5&authcookie=null&business_type=17&content_id=15068699100&hot_size=10&last_id=240262633321"
    for i in range(times):
        lastID, t = getLastIdAndSave(url, lastID)
        #time.sleep(1)
        num += t
        print("已爬取%d条评论" % num)
