def test_digift_ui(app):
    app.open_home_page()
    nominal_card_element = app.cards.find_nominal_card_element()
    app.cards.scroll_to_element(nominal_card_element)
    app.cards.choose_cards()
