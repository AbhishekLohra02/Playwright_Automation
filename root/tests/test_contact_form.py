import pytest
from playwright.sync_api import expect
from pages.hotel_page import hotelpage

@pytest.mark.smoke
def test_contact_form(page):
    hotel = hotelpage(page)
    hotel.navigation()
    hotel.submit_contact_form(
        "Abhishek Lohra",
        "abhishektest@mail.com",
        "1233123123123",
        "Booking Help",
        "I'm just testing that contact form is working or not and as it is a smoke test, I'm not checking the error messages here and just checking the happy flow"
    )

    expect(hotel.contact_name).to_be_visible()
    expect(hotel.success_message).to_have_text("Thanks for getting in touch Abhishek Lohra!")