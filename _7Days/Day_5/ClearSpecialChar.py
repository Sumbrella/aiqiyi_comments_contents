"""

"""
import re


def clear_special_char(content):
    s = re.sub(r"</?(.+?)>|&nbsp;|\t|\r", "", content)
    s = re.sub(r"\n", " ", s)
    s = re.sub(r"\+", "\\*", s)
    s = re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]', '', s)
    s = re.sub('[\001\002\003\004\005\006\007\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x20]]', '', s)
    s = re.sub('[a-zA-Z]', '', s)
    s = re.sub('^\d+(\.\d+)>$', '', s)

    return s


if __name__ == '__main__':
    with open('cleared_comments.txt', 'a+') as fs:
        new_line = ""
        with open('comments.txt', 'r') as fp:
            for line in fp:
                new_line = clear_special_char(line)
        fs.write(new_line)