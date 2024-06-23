from selenium.webdriver import Chrome


class LoginPage():

    def __init__(self, driver_instance: Chrome):
        self.driver = driver_instance
        self.login_url = "https://accounts.google.com/signin"

    def get_login_page(self):
        self.driver.get(self.login_url)

