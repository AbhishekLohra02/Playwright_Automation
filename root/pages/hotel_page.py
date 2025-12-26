class hotelpage:
    def __init__(self, page):
        self.page = page
        # form locators:
        self.name_field = page.locator("//input[@id='name']")
        self.email_field = page.locator("//input[@id='email']")
        self.phone_field = page.locator("//input[@id='phone']")
        self.subject_field = page.locator("//input[@id='subject']")
        self.message_field = page.locator("//textarea[@id='description']")
        self.success_message = page.get_by_role("heading", name="Thanks for getting in touch Abhishek Lohra!")
        self.book_now_button = page.locator("//body//div[@id='root-container']//div//div//div[@class='container']//div[1]//div[1]//div[3]//a[1]")
        self.calender_field = page.locator("//div[@class='rbc-calendar']")

        self.contact_name = page.get_by_test_id("ContactName")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.reserve_now = page.locator("//button[@id='doReservation']")
        self.name_reserve_now = page.locator("//input[@placeholder='Firstname']")
        self.lastname_reserve_now = page.locator("input[placeholder='Lastname']")
        self.email_reserve_now = page.locator("input[placeholder='Email']")
        self.phone_reserve_now = page.locator("input[placeholder='Phone']")
        self.final_reservenow_button = page.get_by_role("button", name="Reserve Now")

    def navigation(self):
        self.page.goto("https://automationintesting.online/")
        self.page.pause() # pause for just 5 seconds to see the page after it gets loaded
        

    def submit_contact_form(self, name, email, phone, subject, message):
        self.name_field.fill(name)
        self.email_field.fill(email)
        self.phone_field.fill(phone)
        self.subject_field.fill(subject)
        self.message_field.fill(message)
        self.submit_button.click()

    def get_success_message(self):
        self.success_message.wait_for(state="visible")
        return self.success_message.text_content()
    
    def book_now_function(self,firstname, lastname, email, phone):
        self.book_now_button.click()
        
        # 1. Identify all day cells
        days = self.page.locator(".rbc-day-bg")
        
        # 2. Simple Loop: Find a day that doesn't have a 'booked' marker
        # We start at index 5 to be safe from previous month's dates
        start_day_index = 5 
        for i in range(5, days.count()):
            # If this specific day contains no booking events
            if self.page.locator(".rbc-event").count() == 0:
                start_day_index = i
                break

        # 3. Define our range (e.g., a 2-day stay)
        checkin = days.nth(start_day_index)
        checkout = days.nth(start_day_index + 2)

        # 4. Drag to select
        checkin.drag_to(checkout, force=True)
        # 3. Fill the Guest Details
        # These fields only become visible/available AFTER the drag is successful
        self.name_reserve_now.fill(firstname)
        self.lastname_reserve_now.fill(lastname)
        self.email_reserve_now.fill(email)
        self.phone_reserve_now.fill(phone)
        
        # 4. Click the final 'Book' / 'Reserve' button
        self.final_reservenow_button.click()

    
