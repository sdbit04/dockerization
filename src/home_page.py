from selenium.webdriver import Chrome


class HomePage():

    def __init__(self, driver_instance: Chrome):
        self.driver = driver_instance
        self.url = "https://www.google.com/"

    def get_home_page(self):
        self.driver.get(self.url)

