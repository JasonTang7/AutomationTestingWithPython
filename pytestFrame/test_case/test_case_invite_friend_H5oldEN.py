import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pytestFrame.function.time_stamp import time_stamp


#修改Chrome浏览器启动配置文件，英文，选择手机模式，启动时直接打开开发者模式
options = webdriver.ChromeOptions()
mobile_emulation = {"deviceName":"iPhone X"}
options.add_experimental_option("mobileEmulation",mobile_emulation)
options.add_argument("--auto-open-devtools-for-tabs")
options.add_argument("lang=en-US.UTF-8")

class Test_Case_Invite_Friend_H5olden(unittest.TestCase):

    def setUp(self) -> None:
        #启动浏览器时自动进入开发者手机模式
        self.driver = webdriver.Chrome(chrome_options=options)
        sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()


    def test_001_invite_friend_H5olden(self):
        try:
            # 打开邀请好友H5旧页面
            self.driver.get('https://u.yamibuy.com/643248?utm_medium=internal_share_copylink')
            self.driver.implicitly_wait(10)

            #获取按钮文本值
            button_text = self.driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div[3]/div/a/span').text

            #获取url，判断url中是否有 “invite_code”
            url = self.driver.current_url

            #通过url中是否有 “invite_code” 断言
            if "invite_code" in url:
                assert "invite_code" in url

            #如果url断言不通过，通过是否有 “Take it now” 断言
            else:
                self.assertEqual(button_text,'Take it now')


        except AssertionError as e:
            self.driver.get_screenshot_as_file(r'..\screen_shot\H5olden邀请错误' + time_stamp() + '.png')
            raise e



unittest.TextTestRunner()