import pytest

base_url = "https://automationintesting.online/api/auth/login"
room_url = "https://automationintesting.online/api/room/"

def test_check_room_price(page):

    payload = {
        "username" : "admin",
        "password" : "password"
    }

    response = page.request.post(base_url, data=payload)
    assert response.status==200

def test_get_room_price(page):

    response = page.request.get(room_url)
    assert response.status == 200

    
    room_data = response.json()
    assert "rooms" in room_data

    first_room = room_data['rooms'][0]
    assert 'roomPrice' in first_room
    
    print(f"Room_price: {first_room['roomPrice']}")
