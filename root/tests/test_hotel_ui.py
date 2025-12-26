import pytest
from playwright.sync_api import expect
from pages.hotel_page import hotelpage

@pytest.mark.smoke
def test_hotelpage_loads(page):
    hotel = hotelpage(page)
    hotel.navigation()
    expect(hotel.submit_button).to_be_visible()

