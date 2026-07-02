from playwright.sync_api import sync_playwright

def test_login_and_signup_buttons():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nilesh-chetu.github.io/")

        # Verify login button exists and has correct styling
        login_button = page.locator(".login-button")
        assert login_button.is_visible()
        assert login_button.evaluate("element => getComputedStyle(element).backgroundColor") == "rgb(19, 122, 139)"

        # Verify signup button exists and has correct styling
        signup_button = page.locator(".signup-button")
        assert signup_button.is_visible()
        assert signup_button.evaluate("element => getComputedStyle(element).backgroundColor") == "rgb(19, 122, 139)"
        assert signup_button.evaluate("element => getComputedStyle(element).cursor") == "not-allowed"

        # Verify signup button is non-functional
        signup_button.click(force=True)
        assert not page.url.endswith("#")  # Should not navigate anywhere

        # Verify login functionality
        page.fill("#username", "admin")
        page.fill("#password", "admin")
        page.click(".login-button")
        assert page.evaluate("alertText => window.alertText", "Congratulations!!!")

        browser.close()

if __name__ == "__main__":
    test_login_and_signup_buttons()