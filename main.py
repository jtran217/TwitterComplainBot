# IMPORT LIST
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# CONSTANT VARIABLES
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "DRIVER PATH"
TWITTER_EMAIL = "TWITTER EMAIL"
TWITTER_PASSWORD = "TWITTER PASSWORD"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.up = None
        self.down = None
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        sleep(45)
        down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.down = down.get_attribute("innerHTML")
        self.up = up.get_attribute("innerHTML")
        print(f"Download Speed: {self.down}")
        print(f"Upload Speed: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        sleep(3)
        log_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        log_in.click()
        sleep(1)
        email = self.driver.find_element_by_name("session[username_or_email]")
        email.send_keys(TWITTER_EMAIL)
        pass_form = self.driver.find_element_by_name("session[password]")
        pass_form.send_keys(TWITTER_PASSWORD)
        pass_form.send_keys(Keys.ENTER)
        sleep(1)
        tweet_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span')
        tweet_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for"
                            f"{PROMISED_DOWN}down/{PROMISED_UP}up?")
        sleep(2)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_button.click()


ISTB = InternetSpeedTwitterBot()

ISTB.get_internet_speed()

#TWEET ONLY WHEN UPLOAD AND DOWNLOAD SPEED LESS THAN CONTRACT PROMISE
if ISTB.up < PROMISED_UP and ISTB.down < PROMISED_DOWN:
    ISTB.tweet_at_provider()