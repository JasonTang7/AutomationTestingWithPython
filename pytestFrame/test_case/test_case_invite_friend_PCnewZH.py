import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pytestFrame.function.time_stamp import time_stamp

class Test_Case_Invite_Friend_PCnewZH(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        sleep(1)
        self.driver.maximize_window()
        sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()


    def test_001_invite_friend_PCnewzh(self):
        try:
            #输入url
            self.driver.get('https://www.yamibuy.com/?invite_code=495852&user_id=590458&email_type=user_invite_friends&language=zh_CN')
            self.driver.implicitly_wait(10)

            # 获取按钮文本值
            button_text = self.driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div[4]').text

            # 获取url，判断url中是否有 “invite_code”
            url = self.driver.current_url

            # 通过url中是否有 “invite_code” 断言
            if "invite_code" in url:
                assert "invite_code" in url

            # 如果url断言不通过，通过是否有 “领取奖励” 断言
            else:
                self.assertEqual(button_text, '领取奖励')

        except AssertionError as e:
            self.driver.get_screenshot_as_file(r'..\screen_shot\PCnewzh邀请错误'+time_stamp()+'.png')
            raise e



unittest.TextTestRunner()
