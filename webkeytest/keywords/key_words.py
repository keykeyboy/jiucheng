'''
web端关键字驱动类
1.工具类代码健壮性，对异常做处理
'''
from time import sleep

from selenium import webdriver
from common.chrome_option import Options


# 获取浏览器驱动,通过反射，根据传入浏览器类型获取浏览器驱动
# getattr(webdriver, type_)相当于webdriver.Chrome()
# 当浏览器参数传入异常是也需要设置options值
from common.log import Logging


def browser(type_,is_loc):
    try:
        opt = Options().chrome_options()
        driver = getattr(webdriver, type_)()
        # driver = getattr(webdriver, type_)(options=opt)
    except Exception as e:
        print(e)
        # 异常默认浏览器是Chrome
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome(options=opt)
    return driver


class KeyWords:
    # driver = webdriver.Chrome()
    # 构造函数
    # 创建实例对象需要构造函数
    def __init__(self, type_,log_file):
        self.driver = browser(type_)
        # 隐式等待
        self.driver.implicitly_wait(10)
        self.logging_ = Logging().log_template(log_file)

    # 获取浏览器驱动,通过反射，根据传入浏览器类型获取浏览器驱动
    # getattr(webdriver, type_)相当于webdriver.Chrome()
    # 当浏览器参数传入异常是也需要设置options值

    # 打开网址
    def open(self, **kwargs):
        self.driver.get(kwargs['text'])
        self.logging_.info('输入的网址是{}'.format(kwargs['text']))

    # 关闭浏览器
    def quit(self, **kwargs):
        self.logging_.info('窗口-{}关闭'.format(self.driver.title))
        self.driver.quit()

    # 定位元素
    def locator(self, **kwargs):
        try:
            self.logging_.info('定位元素的name为{}，value为{}'.format(kwargs['name'], kwargs['value']))
            return self.driver.find_element(kwargs['name'], kwargs['value'])
        except Exception as e:
            print(e)
            self.logging_.info('定位元素的name为{}，value为{},未找到该元素'.format(kwargs['name'], kwargs['value']))

    # 点击操作
    def click(self, **kwargs):
        self.logging_.info('点击操作定位元素的name为{}，value为{}'.format(kwargs['name'], kwargs['value']))
        self.locator(**kwargs).click()

    # 输入操作
    def input(self, **kwargs):
        self.logging_.info('输入定位元素的name为{}，value为{},输入内容为{}'.format(kwargs['name'], kwargs['value'], kwargs['text']))
        self.locator(**kwargs).send_keys(kwargs['text'])

    # 断言校验
    def assert_text(self, **kwargs):
        # self.logging_.info(
        #     '断言定位元素的name为{}，value为{}，断言值为{}'.format(kwargs['name'], kwargs['value'], kwargs['fact_text']))
        try:
            assert self.locator(**kwargs).text == kwargs['fact_text'], '断言失败'
            return True
        except:
            return False

    # 强制等待
    def wait(self, **kwargs):
        self.logging_.info('强制等待{}s'.format(kwargs['text']))
        sleep(kwargs['text'])

    # 截屏
    def save_screen(self,file_name):
        self.driver.save_screenshot(file_name)
    # 显示等待
