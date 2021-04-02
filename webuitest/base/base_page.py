from selenium.webdriver.support.ui import WebDriverWait

from common.log import Logging
import time
from selenium import webdriver


# 页面基类

class BasePage:

    url = 'http://39.98.138.157/shopxo/index.php'
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        self.log = Logging().log_template('../log/info.log')
        # self.url = 'http://39.98.138.157/shopxo/index.php'

    # 定位元素,return返回元素
    def locator(self, loc):
        self.log.info('定位元素：{}'.format(loc))
        return self.driver.find_element(*loc)

    # 打开网页
    def open(self):
        self.log.info('正在打开网址：{}'.format(self.url))
        self.driver.get(self.url)

    # 输入
    def input(self, loc, content):
        self.locator(loc).send_keys(content)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 关闭浏览器
    def quit(self):
        self.log.info('正在关闭浏览器'.format(self.driver.title))
        self.driver.close()

    # 截屏
    # def screen_shot(self):
    #     self.driver.save_screenshot('../picture/1.png')

    # 断言
    def assert_text(self, loc):
        WebDriverWait(self.driver,0.5,5).until(lambda el:self.locator(loc),message='没找到该元素')

