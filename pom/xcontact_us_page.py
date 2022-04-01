# TODO: IMPORTANT! Watch sections on pytest and fixture, and Data Driven testing before building POM for entire app!
# TODO: Fixtures are ideal for any repetitive steps in the beginning or the end of tests
# TODO: Use POM helper methods only for repetitive steps in the middle of your tests

from pom.xcontact_us_page_elements import ContactUs

class ContactUsPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):   #fixture is better suited for this task
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self, name, adress, email, phone_number, test_subject, message):
        self.page.fill(ContactUs.name_input, name)
        self.page.fill(ContactUs.adress_input, adress)
        self.page.fill(ContactUs.email_input, email)
        self.page.fill(ContactUs.phone_number_input, phone_number)
        self.page.fill(ContactUs.test_subject_input, test_subject)
        self.page.fill(ContactUs.textarea_input, message)
        #self.page.press('[aria-label="Enter your search term"]', "Enter")