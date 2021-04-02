import threading
import time

from common.remote_driver import RemoteDriver


def visit(driver):
    # driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    time.sleep(5)
    driver.quit()

host = {
    'http://172.16.13.118:4450/wd/hub': 'chrome',
    'http://172.16.13.118:4451/wd/hub': 'chrome'
}

th = []

for url, browser in host.items():
    # print(url + '----' + browser)

    # 设定Node节点的URL地址，后续将通过访问这个地址连接到Node计算机
    # driver = webdriver.Remote(url, desired_capabilities={
    #     # 远程计算机的平台
    #     "platform": "WINDOWS",
    #     # 指定远程计算机执行使用的浏览器为chrome；或者internet explorer/firefox
    #     "browserName": browser
    # })
    driver = RemoteDriver().get_driver(url, browser)
    th.append(threading.Thread(target=visit, args=[driver]))

for t in th:
    t.start()