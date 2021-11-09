from http import cookiejar
import mechanize
from abc import ABC, abstractmethod, abstractproperty

import settings

VITAL_URL = 'https://www.mindbodyonline.com/explore/locations/vital-climbing-gym-williamsburg'
CLASS_URL = 'https://cart.mindbodyonline.com/sites/85337/cart/add_booking?item%5Binfo%5D=Tue.+Nov+16%2C+2021+11%3A45+am&item%5Bmbo_id%5D=105842&item%5Bmbo_location_id%5D=1&item%5Bname%5D=AERIAL+-+Beginner+Silks&item%5Btype%5D=Class'
CHECKOUT_URL = 'https://cart.mindbodyonline.com/sites/85337/cart/proceed_to_checkout'


class Scheduler(ABC):

    @abstractmethod
    def login(self):

        pass

    @abstractmethod
    def schedule_class(self, url: str):
        pass


class MechanizeScheduler(Scheduler):

    browser: mechanize.Browser
    username: str = settings.MINDBODY_USERNAME
    password: str = settings.MINDBODY_PASSWORD

    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        self.browser.addheaders = [(
            'User-agent',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        )]
        self.browser.set_cookiejar(cookiejar.CookieJar())

        
    def login(self):
        self.browser.open(self.login_url)
        form = self.browser.select_form(nr=0)
        form['username'] = self.username
        form['password'] = self.password