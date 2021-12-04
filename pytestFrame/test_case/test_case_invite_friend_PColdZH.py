import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pytestFrame.function.time_stamp import time_stamp

class Test_Case_Invite_Friend_PColdzh(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        sleep(1)
        self.driver.maximize_window()
        sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()


    def test_001_invite_friend_PColdzh(self):
        try:
            #打开旧的PC中文邀请页面
            self.driver.get('https://customer.yamibuy.com/account/register?invite_code=495852&user_id=590458&email_type=user_invite_friends&language=zh_CN')
            self.driver.implicitly_wait(10)

            # 获取左下角弹框的文本值
            button_text = self.driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/p').text

            # 获取url，判断url中是否有 “invite_code”
            url = self.driver.current_url

            # 通过url中是否有 “invite_code” 断言
            if "invite_code" in url:
                assert "invite_code" in url

            # 如果url断言不通过，通过是否有 “领取立减$10优惠券” 断言
            else:
                self.assertEqual(button_text, '领取立减$10优惠券')
        except AssertionError as e:
            self.driver.get_screenshot_as_file(r'..\screen_shot\PColdzh邀请错误'+time_stamp()+'.png')
            raise e



unittest.TextTestRunner()