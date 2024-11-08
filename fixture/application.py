from selenium import webdriver
from fixture.cards import NominalCardsHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome(executable_path='C:/chromedriver.exe')
        self.wd.implicitly_wait(30)
        self.cards = NominalCardsHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://qa.digift.ru/")

    def destroy(self):
        self.wd.quit()
