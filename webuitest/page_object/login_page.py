from webuitest.base.base_page import BasePage
from selenium.webdriver.common.by import By


# 登录页面http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html
class LoginPage(BasePage):
    url = BasePage.url+'?s=/index/user/logininfo.html'
    user = (By.NAME, 'accounts')
    pwd = (By.NAME, 'pwd')
    button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    # 登录
    def login(self, username, password):
        self.open()
        self.input(self.user, username)
        self.input(self.pwd, password)
        self.click(self.button)


# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lp = LoginPage(driver)
#     lp.login('wwwwww', 'wwwwww')
