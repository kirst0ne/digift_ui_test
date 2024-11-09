from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class NominalCardsHelper:
    def __init__(self, app):
        self.app = app

    def scroll_to_element(self, element):
        self.app.wd.execute_script("arguments[0].scrollIntoView();", element)

    def activate_card(self, index):
        self.app.wd.find_element_by_xpath(f"//li[{index}]/button").click()

    def choose_cards(self, wd):
        for i in range(1, 7):
            self.activate_card(i)
            self.check_active_button(i)
            self.check_inactive_buttons(i)
            self.check_nominal_value(i)

    def check_active_button(self, index):
        active_button = self.app.wd.find_element_by_xpath(
            f"//li[{index}]/button[contains(@class, 'par-options__button--active')]"
        )
        assert active_button.is_enabled(), f"Button {index} should be active after clicking"

    def check_inactive_buttons(self, active_index):
        for j in range(1, 7):
            if j != active_index:
                inactive_button = self.app.wd.find_element_by_xpath(f"//li[{j}]/button")
                assert not inactive_button.get_attribute("class") == "par-options__button--active",\
                    f"Button {j} should not be active"

    def find_nominal_card_element(self):
        self.app.open_home_page()
        return self.app.wd.find_element_by_xpath("//*[text()='Номинал карты']")

    def get_activation_button(self):
        buttons = WebDriverWait(self.app.wd, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".par-options__button"))
        )
        for button in buttons:
            if "par-options__button--active" in button.get_attribute("class"):
                return button
        raise Exception("Активная кнопка не найдена")

    def is_activation_button_enabled(self):
        button = self.get_activation_button()
        return "par-options__button--active" in button.get_attribute("class")

    def activate_initial_card(self):
        self.activate_card(3)

    def get_button_value(self, index):
        return self.app.wd.find_element_by_xpath(f"//li[{index}]/button").text

    def get_nominal_value(self):
        return self.app.wd.find_element_by_id("range-value-input").get_attribute('value')

    def check_nominal_value(self, index):
        button_value = self.get_button_value(index)
        nominal_value = self.get_nominal_value()
        assert nominal_value == button_value, f"Expected nominal value '{button_value}' but got '{nominal_value}'"
