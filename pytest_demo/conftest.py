'''
@Project ：auto_test 
@File ：conftest.py.py
@Date ：2021/4/2 9:58 
'''
'''
这是pytest中的预置函数定义的配置文件：注意，文件名称一定是conftest。不能是其他的
scope参数定义的4种等级（默认等级是function）：
    session：在本次session级别中只执行一次
    module：在模块级别中只执行一次
    class：在类级别中只执行一次
    function：在函数级别中执行，每有一个函数就执行一次
'''
import pytest
import requests
from apikeytest.keywords.key_words import ApiKeys


@pytest.fixture(scope='session')
def test():
    ak = ApiKeys()
    data = {
        'username': 'admin',
        'password': '123456',
    }
    url = 'http://39.98.138.157:5000/api/login'
    res = requests.post(url=url, json=data)
    return ak.get_text(res.text, 'token')


@pytest.fixture(scope='module')
def test_module():
    print('testmodule')
