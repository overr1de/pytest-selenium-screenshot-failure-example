import time

def test_selenium_error_is_being_captured_as_screenshot(selenium_driver):
    selenium_driver.get("https://google.com")
    time.sleep(5)

    assert False  # should invoke hook call, that creates a screenshot