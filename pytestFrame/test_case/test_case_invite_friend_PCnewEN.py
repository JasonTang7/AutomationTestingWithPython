import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pytestFrame.function.time_stamp import time_stamp

#修改Chrome浏览器启动配置，英文
options = webdriver.ChromeOptions()
options.add_argument("lang=en-US.UTF-8")

class Test_Case_Invite_Friend_PCnewen(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        sleep(1)
        self.driver.maximize_window()
        sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()


    def test_001_invite_friend_PCnewen(self):
        try:
            # 输入url
            self.driver.get('https://www.yamibuy.com/en?invite_code=495852&user_id=590458&email_type=user_invite_friends&language=en_US')
            self.driver.implicitly_wait(10)

            # 获取按钮文本值
            button_text = self.driver.find_element(By.XPATH,'//*[@id="inviteContainerId"]/div/div/div/div[2]/div/button[1]').text

            # 获取url，判断url中是否有 “invite_code”
            url = self.driver.current_url

            # 通过url中是否有 “invite_code” 断言
            if "invite_code" in url:
                assert "invite_code" in url

            # 如果url断言不通过，通过是否有 “Claim Your Coupon” 断言
            else:
                self.assertEqual(button_text, 'Claim Your Coupon')

        except AssertionError as e:
            self.driver.get_screenshot_as_file(r'..\screen_shot\PCnewen邀请错误'+time_stamp()+'.png')
            raise  e



unittest.TextTestRunner()