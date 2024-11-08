from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest


class digift_ui(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path='C:/Windows/System32/chromedriver.exe')
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://qa.digift.ru/")

    def scroll_to_element(self, element):
        self.wd.execute_script("arguments[0].scrollIntoView();", element)

    def choose_cards(self):
        wd = self.wd
        wd.find_element_by_xpath("//li[1]/button").click()
        wd.find_element_by_xpath("//li[2]/button").click()
        wd.find_element_by_xpath("//li[3]/button").click()
        wd.find_element_by_xpath("//li[4]/button").click()
        wd.find_element_by_xpath("//li[5]/button").click()
        wd.find_element_by_xpath("//li[6]/button").click()

    def find_nominal_card_element(self):
        return self.wd.find_element_by_xpath("//*[text()='Номинал карты']")

    def test_digift_ui(self):
        self.open_home_page()
        nominal_card_element = self.find_nominal_card_element()
        self.scroll_to_element(nominal_card_element)
        self.choose_cards()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
