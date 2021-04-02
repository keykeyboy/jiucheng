'''
@Project ：auto_test 
@File ：key_words.py
@Date ：2021/3/26 9:23 
'''
import json

import requests
import jsonpath
from common.log import Logging


class ApiKeys:
    def __init__(self):
        self.log = Logging()

    def get(self, url, params=None, **kwargs):
        """
        :param url:访问地址
        :param params: 参数,设置默认值，没有传递值是为None
        :return:
        """
        response = requests.get(url=url, params=params, **kwargs)
        # self.log.log('请求地址：{},请求参数：{}'.format(url, params))
        return response

    def post(self, url,  json=None, **kwargs):
        '''
        :param url: 请求地址
        :param data:
        :param json:
        :param kwargs:
        :return:
        '''
        response = requests.post(url=url, json=json, **kwargs)
        # print('1111111111')
        # self.log.info('11111')
        self.log.log('请求url:{},参数:{},返回结果:{}'.format(url,json,response.text))
        return response

    def get_text(self, res, expect_field):
        '''
        :param key: key为接口的断言字段，需要根据key从res获取对应值
        :param res: res接口请求响应内容
        :return: 如果返回有值就返回真，没值就返回false
        '''

        try:
            json_res = json.loads(res)
            # 如果返回值，value就是一个列表['success1','success2'...]，如果不返回值就为false
            value = jsonpath.jsonpath(json_res, '$..{0}'.format(expect_field))
            if value:
                if len(value) == 1:
                    # 感觉长度为1的话直接返回value就可以
                    return value[0]
            return value
        except Exception as e:
            # 报异常直接返回False
            return False

    def asserted(self, actual_value, expect_value):
        '''
        :param actual_value: 实际值
        :param expect_value: 期望值
        :return: 如果实际值和期望值一致返回True,否则返回False
        '''
        try:
            assert actual_value == expect_value
            return True
        except:
            return False


if __name__ == '__main__':
    ak = ApiKeys()
    for i in range(3):
        url = 'http://39.98.138.157:5000/api/login'
        # rs = ak.do_get(url=url)
        data = {
            'username': 'admin1',
            'password': '123456'
        }
        rs = ak.post(url=url, json=data)
    # text = rs.text
    # # print(rs.status_code)
    # # print(text)
    # result = ak.get_text(text, 'msg')
    # status = ak.asserted('success1', 'success')
    # print(result, status)
