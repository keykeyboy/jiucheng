'''
@Project ：auto_test 
@File ：test_demo02.py
@Date ：2021/4/2 10:53 
'''
from selenium import webdriver
import pytest
import time

class TestDemo02:
    def test_01(self):
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('橙子')
        time.sleep(5)
        driver.close()

    def test_02(self):
        driver = webdriver.Chrome()
        driver.get('https://www.bilibili.com/')
        driver.find_element_by_xpath('//*[@id="nav_searchform"]/input').send_keys('test02')
        time.sleep(5)
        driver.close()

    def test_03(self):
        driver = webdriver.Chrome()
        driver.get('https://www.zhihu.com/')
        time.sleep(5)
        driver.close()

if __name__ == '__main__':
    pytest.main(['-s','-v','test_demo02.py','-n','3'])