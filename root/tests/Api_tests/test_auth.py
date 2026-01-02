import pytest

base_url = "https://automationintesting.online/api/auth/login"

def test_auth_login_success(page):

    payload = {
        "username" : "admin",
        "password" : "password"
    }

    response = page.request.post(base_url, data=payload)

    assert response.status == 200
    print(response.json())
    print(response.headers)

def test_auth_login_failure(page):

    payload = {
        "username" : "Abhishek",
        "password" : " Abhishek@123"
    }

    response = page.request.post(base_url, data=payload)

    assert response.status in [401, 403]
