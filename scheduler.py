from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from abc import ABC, abstractmethod, abstractproperty

import settings
from exceptions import AuthenticationException

VITAL_URL = 'https://www.vitalclimbinggym.com/brooklyn-book-class'
CLASS_URL = 'https://cart.mindbodyonline.com/sites/85337/cart/add_booking?item%5Binfo%5D=Tue.+Nov+16%2C+2021+11%3A45+am&item%5Bmbo_id%5D=105842&item%5Bmbo_location_id%5D=1&item%5Bname%5D=AERIAL+-+Beginner+Silks&item%5Btype%5D=Class'
CHECKOUT_URL = 'https://cart.mindbodyonline.com/sites/85337/cart/proceed_to_checkout'


class Scheduler(ABC):

    @abstractmethod
    def login(self):

        pass

    @abstractmethod
    def schedule_class(self, url: str):
        pass


class VitalScheduler(Scheduler):

    browser: Firefox
    username: str = settings.MINDBODY_USERNAME
    password: str = settings.MINDBODY_PASSWORD
    login_url: str = 'https://cart.mindbodyonline.com/sites/85337/client'
    login_success_url: str = 'https://cart.mindbodyonline.com/sites/85337/client/edit'
    class_name: str = 'AERIAL - Beginner Silks'
    checkout_url: str

    def __init__(self, class_name):
        self.browser = Firefox()

    def get_class_url(self, name: str) -> str:
        pass

    def get_checkout_url(self) -> str:
        pass

    def login(self) -> None:
        self.browser.get(self.login_url)
        username_input = self.browser.find_element(By.ID, 'mb_client_session_username')
        username_input.send_keys(self.username)
        password_input = self.browser.find_element(By.ID, 'mb_client_session_password')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        if self.browser.current_url != self.login_success_url:
            raise AuthenticationException

    def select_date(self, date):
        date_input = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/main/section/div/div[2]/div/div/div/healcode-widget/div/div/div[3]/div/label/input')
        self.browser.execute_script(f'document.getElementsByClassName("bw-datepicker__input")[0].value = "{date}"')
        date_input.click()
        datepicker_accept_button = self.browser.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/a[2]')
        datepicker_accept_button.click()

    def filter_classes(self, name):
        pass

    def schedule_class(self, url: str):
        pass