'''
@Project ：auto_test 
@File ：mock_server.py
@Date ：2021/3/25 11:04 
'''
from unittest import mock


def MockServer(rerurn_value):
    '''
    :param rerurn_value: 期待返回的值
    :return:调用的返回值名需要和Mock服务方法名保持一致
    '''
    return mock.Mock(return_value=rerurn_value)
