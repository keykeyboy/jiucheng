import unittest

from ddt import file_data, ddt
from webuitest.page_object.login_page import LoginPage
from webuitest.page_object.addcart_page import AddCartPage
from selenium import webdriver
from common.chrome_option import Options


@ddt
class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=Options().chrome_options())
        cls.lp = LoginPage(cls.driver)
        cls.acp = AddCartPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登录
    @file_data('../data/user_info.yaml')
    def test_01_login(self, **kwargs):
        self.lp.login(kwargs['username'], kwargs['password'])

    # 添加购物车
    def test_02_addcart(self):
        self.acp.addcart()


if __name__ == '__main__':
    unittest.main()
