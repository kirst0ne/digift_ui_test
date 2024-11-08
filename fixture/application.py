from selenium import webdriver


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome(executable_path='C:/chromedriver.exe')
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

    def destroy(self):
        self.wd.quit()
