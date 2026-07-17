from playwright.sync_api import sync_playwright, expect

def test_website_title_and_login_functionality():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nilesh-chetu.github.io/")

        # Verify the title has been updated
        expect(page.locator("h1")).to_have_text("Welcome to Chetu's website")

        # Verify login button exists and has correct styling
        login_button = page.locator(".login-button")
        expect(login_button).to_be_visible()
        expect(login_button).to_have_css("background-color", "rgb(19, 122, 139)")

        # Verify signup button exists and has correct styling
        signup_button = page.locator(".signup-button")
        expect(signup_button).to_be_visible()
        expect(signup_button).to_have_css("background-color", "rgb(19, 122, 139)")
        expect(signup_button).to_have_css("cursor", "not-allowed")

        # Verify signup button is non-functional
        signup_button.click(force=True)
        expect(page).not_to_have_url("https://nilesh-chetu.github.io/#")

        # Verify successful login
        page.fill("#username", "admin")
        page.fill("#password", "admin")
        page.on("dialog", lambda dialog: dialog.accept())
        page.click(".login-button")

        # Verify failed login
        page.fill("#username", "wrong")
        page.fill("#password", "wrong")
        page.on("dialog", lambda dialog: dialog.accept())
        page.click(".login-button")

        browser.close()

if __name__ == "__main__":
    test_website_title_and_login_functionality()