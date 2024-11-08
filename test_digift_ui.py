import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_digift_ui(app):
    app.open_home_page()
    nominal_card_element = app.find_nominal_card_element()
    app.scroll_to_element(nominal_card_element)
    app.choose_cards()
