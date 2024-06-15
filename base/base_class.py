import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method - get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Methon checking header"""
    def checking_header(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method screenshoots"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshort = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(".\\screen\\" + name_screenshort)

    """Methon assert url"""
    def  assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")