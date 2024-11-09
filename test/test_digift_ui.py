def test_digift_ui(app):
    nominal_card_element = app.cards.find_nominal_card_element()
    app.cards.scroll_to_element(nominal_card_element)
    app.cards.activate_initial_card()
    assert app.cards.is_activation_button_enabled()
    app.cards.choose_cards(app.wd)
    assert app.cards.is_activation_button_enabled()
