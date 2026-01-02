import pytest
from playwright.sync_api import expect
from pages.hotel_page import hotelpage

@pytest.mark.smoke
def test_booking_function(page):
    hotel = hotelpage(page)
    hotel.navigation()
    hotel.book_now_function(
        "Abhishek",
        "Lohra",
        "abhisheklohra@mail.com",
        "928818888181"
    )
    expect (hotel.page)