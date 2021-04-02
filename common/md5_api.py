"""
@Project ：auto_test
@File ：api_md5.py
@Date ：2021/3/25 10:56
"""
import hashlib


def get_md5(string):
    """
    :param string:输入的字符串
    :return:
    """
    string_md5 = hashlib.md5(str(string).encode('utf-8')).hexdigest()
    return string_md5


if __name__ == '__main__':
    text = get_md5('我叫张三')
    print(text)
