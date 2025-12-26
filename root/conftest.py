import pytest

@pytest.fixture(scope="function")
def set_up(page):
    # This runs before every test
    page.set_viewport_size({"width": 1280, "height": 720})
    yield page
    # You can add "Clean up" code here (like deleting a booking)
    