from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Launch browser in headless mode
        page = browser.new_page()  # Open a new page
        page.goto("https://www.google.com")  # Navigate to Google
        print("Page Title:", page.title())  # Print the page title
        browser.close()  # Close the browser

if __name__ == "__main__":
    test_example()
