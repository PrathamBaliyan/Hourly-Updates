from playwright.sync_api import sync_playwright

def book_flight():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Change to False to see browser
        context = browser.new_context()
        page = context.new_page()

        try:
            # Step 1: Open Indigo website
            #page.goto("https://www.goindigo.in/", wait_until="load")

            # Step 2: Select "One Way" trip
            #page.click('button[value="oneway"]')
            # Step 1: Open Indigo website
            page.goto("https://www.goindigo.in/", wait_until="load")

            # Step 2: Wait for "One Way" button and click
            page.wait_for_selector('button[value="oneway"]', timeout=10000)  # Increased timeout
            page.click('button[value="oneway"]')

            # Step 3: Debugging Log
            print("✅ Clicked on 'One Way' button successfully.")

            # Proceed with the rest of the script...

            browser.close()

        except Exception as e:
            print(f"❌ Error: {e}")
            browser.close()


            # Step 3: Enter From & To destinations
            page.fill('input[placeholder="From"]', "Delhi")
            page.click("text=Indira Gandhi International Airport")  # Select from dropdown
            page.fill('input[placeholder="To"]', "Mumbai")
            page.click("text=Chhatrapati Shivaji Maharaj International Airport")  # Select from dropdown

            # Step 4: Select Departure Date (Next Available Date)
            page.click('input[name="departureDate"]')
            page.click("text=Next")  # Adjust based on availability
            page.click("text=Select")

            # Step 5: Click "Search Flights"
            page.click('button[type="submit"]')

            # Step 6: Wait for Flight List and Select the First Flight
            page.wait_for_selector(".fare-summary-card", timeout=10000)
            page.click(".fare-summary-card:first-child button")

            # Step 7: Proceed to Passenger Details
            page.wait_for_selector('button:has-text("Continue")')
            page.click('button:has-text("Continue")')

            # Step 8: Fill Passenger Details (Modify as needed)
            page.fill('input[name="firstName"]', "John")
            page.fill('input[name="lastName"]', "Doe")
            page.select_option('select[name="gender"]', "Male")
            page.fill('input[name="contactNumber"]', "9876543210")
            page.fill('input[name="email"]', "john.doe@example.com")

            # Step 9: Click "Proceed to Payment"
            page.click('button:has-text("Proceed to Payment")')

            # Step 10: Wait for Payment Page and Take Screenshot
            page.wait_for_selector("text=Payment Options", timeout=10000)
            screenshot_path = "indigo_payment_page.png"
            page.screenshot(path=screenshot_path)

            print(f"✅ Screenshot saved: {screenshot_path}")

            # Step 11: Save Screenshot Path to a Local File
            with open("screenshot_path.txt", "w") as file:
                file.write(screenshot_path)
            
            print(f"✅ Screenshot path saved to 'screenshot_path.txt'")

            # Step 11: Close Browser
            browser.close()

        except Exception as e:
            print(f"❌ Error: {e}")
            browser.close()

# Run the function
book_flight()
