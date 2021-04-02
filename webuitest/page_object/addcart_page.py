from webuitest.base.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class AddCartPage(BasePage):
    url = BasePage.url+'?s=/index/goods/index/id/2.html'
    suit = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[2]')
    color = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[2]/ul/li[2]')
    space = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[3]/ul/li[2]')
    count = (By.ID, 'text_box')
    button_buy = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/button')

    def addcart(self):
        self.open()
        time.sleep(1)
        self.click(self.suit)
        time.sleep(1)
        self.click(self.color)
        time.sleep(1)
        self.click(self.space)
        # self.input(self.count, num)
        time.sleep(1)
        self.click(self.button_buy)
        # self.screen_shot()


# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     acp = AddCartPage(driver)
#     acp.addcart()
