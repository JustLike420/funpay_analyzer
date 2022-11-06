import re
import time
from bs4 import BeautifulSoup
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from .models import Seller, Offer

class FunPay:
    def __init__(self):
        self.url = 'https://funpay.com/'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=self.options,
        )

    def run(self):
        self.driver.get(f"{self.url}")

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def show_more(self):
        self.driver.find_element(By.CLASS_NAME, 'lazyload-more').click()


class CsGoSkins(FunPay):
    def __init__(self):
        super().__init__()
        self.url = 'https://funpay.com/lots/209/'

    def get_data(self):
        data = self.driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        offers = soup.find_all('a', class_='tc-item')
        s = 1
        for offer in offers:
            user_block = offer.find('div', class_='tc-user')
            username = user_block.find('div', class_='media-user-name').text.strip()
            user_href = user_block.find('div', class_='avatar-photo')['data-href']
            try:
                rating = offer.find('span', class_='rating-mini-count').text
            except:
                rating = -1
            seller = Seller.objects.get_or_create(username=username,
                                                  user_url=user_href,
                                                  rating=rating)
            title = offer.find('div', class_='tc-desc-text').text
            title = re.sub('[^\x00-\x7Fа-яА-Я]', '', title)  # delete emoji
            title = title.split(',')[0]  # delete trash
            type = offer['data-f-type']
            try:
                other = offer['data-f-other']
            except:
                other = ''
            rare = offer['data-f-rare']
            quality = offer['data-f-quality']
            href = offer['href']
            count = int(offer.find('div', class_='tc-amount').text.replace(' ', ''))
            price = offer.find('div', class_='tc-price')['data-s']
            Offer.objects.create(title=title, type=type, other=other, rare=rare, quality=quality, href=href,
                                 count=count,
                                 price=price, seller=seller[0])
            print(s)
            s += 1



