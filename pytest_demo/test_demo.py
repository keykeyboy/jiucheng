'''
@Project ：auto_test 
@File ：test_demo.py
@Date ：2021/4/1 17:12 
'''
import pytest
import allure
from selenium import webdriver



class Test:
    @allure.feature('某网站的第一个测试用例')
    @allure.story('我的登录')
    @allure.title('登录情况的结果')
    @pytest.mark.testlogin
    def test_demo01(self):
        with allure.step('我的登录步骤'):
            with open('./img/1.jpg', 'rb') as f:
                img = f.read()
                allure.attach(img, '景甜的自拍照')
            assert 1 == 2

    @allure.feature('某某网站的第二个测试用例')
    @allure.story('我的购物')
    @allure.title('购物情况结果')
    @pytest.mark.testbuy
    def test_demo02(self):
        print('testdemo02')

    @allure.feature('某网站的第一个测试用例')
    @allure.story('我的登录')
    @allure.title('获取token值')
    def test_demo03(self,test):

        print('token值为：{}'.format(test))
        return test


# platform win32 -- Python 3.7.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
# rootdir: D:\PythonProject\auto_test\pytest_demo
# collected 2 items
if __name__ == '__main__':
    pytest.main()
    # pytest.main(['-s','-v','test_demo.py::Test::test_demo03','--html=./report/report01.html','--self-contained-html'])
    # pytest.main(['-s','-v','test_demo.py::Test::test_demo01','--html=./report/report01.html','--self-contained-html'])
    # pytest.main(['-s', 'test_demo.py', '--alluredir', './result'])

# 执行完后再执行：allure generate ./result/ -o ./report_allure --clean
