class NominalCardsHelper:
    def __init__(self, app):
        self.app = app

    def scroll_to_element(self, element):
        self.app.wd.execute_script("arguments[0].scrollIntoView();", element)

    def choose_cards(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//li[1]/button").click()
        wd.find_element_by_xpath("//li[2]/button").click()
        wd.find_element_by_xpath("//li[3]/button").click()
        wd.find_element_by_xpath("//li[4]/button").click()
        wd.find_element_by_xpath("//li[5]/button").click()
        wd.find_element_by_xpath("//li[6]/button").click()

    def find_nominal_card_element(self):
        return self.app.wd.find_element_by_xpath("//*[text()='Номинал карты']")
