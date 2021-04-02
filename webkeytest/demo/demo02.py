from selenium import webdriver
import threading
import time


def visit(driver):
    # driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    time.sleep(5)
    driver.quit()


def get_driver(device, browser):
    # chromedriver = PATH("../exe/chromedriver.exe")
    # os.environ["webdriver.chrome.driver"] = chromedriver
    chrome_capabilities = {
        "browserName": browser,  # 浏览器名称
        "version": "",  # 操作系统版本
        "platform": "ANY",  # 平台，这里可以是windows、linux、andriod等等
        # "javascriptEnabled": True,  # 是否启用js
        # "webdriver.chrome.driver": chromedriver
    }
    driver = webdriver.Remote(command_executor=device, desired_capabilities=chrome_capabilities)
    # driver.maximize_window()  # 将浏览器最大化
    # driver.get("https://www.baidu.com/")
    return driver


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
    driver = get_driver(url,browser)
    th.append(threading.Thread(target=visit, args=[driver]))

for t in th:
    t.start()
