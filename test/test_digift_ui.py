import allure


def test_digift_ui(app):
    with allure.step('Finding of card nominals'):
        nominal_card_element = app.cards.find_nominal_card_element()
        app.cards.scroll_to_element(nominal_card_element)
    with allure.step('Check that the button is active'):
        app.cards.activate_initial_card()
        assert app.cards.is_activation_button_enabled()
    with allure.step('The buttons are activated and the selected denomination is displayed'):
        app.cards.choose_cards(app.wd)
        assert app.cards.is_activation_button_enabled()
