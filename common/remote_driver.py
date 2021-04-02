from selenium import webdriver


# 分布式执行测试用例
# 主机负责分配任务至执行机，执行命令java -jar selenium-server-standalone-3.141.59.jar -role hub -port 4444
# 执行机上执行命令java -jar selenium-server-standalone-3.141.59.jar -role node -hub
# --http://172.16.13.118:9001/grid/register/ -port 9001
# device为执行机访问地址，如http://172.16.13.118:4450/wd/hub
# browser为执行机浏览器类型，如chrome

class RemoteDriver:
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
