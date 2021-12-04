import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pytestFrame.function.time_stamp import time_stamp
from pytestFrame import conftest


#修改Chrome浏览器启动配置文件，选择手机模式，启动时直接打开开发者模式
options = webdriver.ChromeOptions()
mobile_emulation = {"deviceName":"iPhone X"}
options.add_experimental_option("mobileEmulation",mobile_emulation)
options.add_argument("--auto-open-devtools-for-tabs")

class Test_Case_Invite_Friend_H5oldzh(unittest.TestCase):

    def setUp(self) -> None:
        #启动浏览器时自动进入开发者手机模式
        self.driver = webdriver.Chrome(chrome_options=options)
        sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()


    def test_001_invite_friend_H5oldzh(self):
        try:
            #打开邀请好友H5旧页面
            self.driver.get('https://u.yamibuy.com/643187?utm_medium=internal_share_sms')
            self.driver.implicitly_wait(10)

            # 获取按钮文本值
            button_text = self.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[3]/div/a/span').text

            # 获取url，判断url中是否有 “invite_code”
            url = self.driver.current_url

            # 通过url中是否有 “invite_code” 断言
            if "invite_code" in url:
                assert "invite_code" in url

            # 如果url断言不通过，通过是否有 “立即领取” 断言
            else:
                self.assertEqual(button_text, '立即领取')

        except AssertionError as e:
            self.driver.get_screenshot_as_file(r'..\screen_shot\H5oldzh邀请错误'+time_stamp()+'.png')
            raise e



unittest.TextTestRunner()