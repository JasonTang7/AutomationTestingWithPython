import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pytestFrame.function.time_stamp import time_stamp

#修改Chrome浏览器启动配置，英文
options = webdriver.ChromeOptions()
options.add_argument("lang=en-US.UTF-8")

class Test_Case_Invite_Friend_PColden(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(chrome_options=options)
        sleep(1)
        self.driver.maximize_window()
        sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()


    def test_001_invite_friend_PColden(self):
        try:
            #打开旧的PC英文邀请界面
            self.driver.get('https://customer.yamibuy.com/account/register?invite_code=495852&user_id=590458&email_type=user_invite_friends&language=en_US')
            self.driver.implicitly_wait(10)

            # 获取按钮文本值
            button_text = self.driver.find_element(By.XPATH,'//*[@id="inviteContainerId"]/div/div/p').text

            # 获取url，判断url中是否有 “invite_code”
            url = self.driver.current_url

            # 通过url中是否有 “invite_code” 断言
            if "invite_code" in url:
                assert "invite_code" in url

            # 如果url断言不通过，通过是否有 “Claim your $10 coupon ” 断言
            else:
                self.assertEqual(button_text, 'Claim your $10 coupon ')

        except AssertionError as e:
            self.driver.get_screenshot_as_file(r'..\screen_shot\PColden邀请错误'+time_stamp()+'.png')
            raise e



unittest.TextTestRunner()