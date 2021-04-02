'''
@Project ：auto_test 
@File ：api_login.py
@Date ：2021/3/29 13:57 
'''

from apikeytest.keywords.key_words import ApiKeys
import unittest
from ddt import ddt, file_data
from apikeytest.config.read_ini import ReadIni


@ddt
class LoginApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ak = ApiKeys()
        cls.base_url = ReadIni('../config/config.ini', 'TEST_SERVER', 'URL')
        # cls.token = None

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @file_data('../data/login.yaml')
    def test_login(self, url, data, expect_field, expect_value):
        res = self.ak.do_post(url=self.base_url + url, json=data)
        content = res.text
        print(content)
        text = self.ak.get_text(content, expect_field)
        token = self.ak.get_text(content, 'token')
        if token:
            LoginApi.token=token
        print(self.token)
        self.assertEqual(text, expect_value, msg='没找到 {0} 期望值 {1} '.format(expect_field, expect_value))

    def test_print(self):
        print(self.token)


if __name__ == '__main__':
    unittest.main()
