import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

SIGN_UP = True
FETCH_LOGIN_DATA = False
USE_ADMIN_CREDENTIALS = 0
TIME_TRAVEL = True

def signup():
    signup_btn = driver.find_element(By.ID, value="toggle-login-register")
    signup_btn.click()

    driver.implicitly_wait(10)

    with open(file="signup_data.json",mode="r") as file:
        data = json.load(file)
        signup_name = data["chrome_signup"]["name"]
        signup_email = data["chrome_signup"]["email"]
        signup_password = data["chrome_signup"]["password"]

    name_input = driver.find_element(By.ID, value="name-input")
    email_input = driver.find_element(By.ID, value="email-input")
    password_input = driver.find_element(By.ID, value="password-input")

    name_input.send_keys(signup_name)
    email_input.send_keys(signup_email)
    password_input.send_keys(signup_password)
def login():
    login_email = ""
    password_input = ""
    if FETCH_LOGIN_DATA:
        try:
            with open(file="login_data.json",mode="r") as file:
                data = json.load(file)
                login_email = data["chrome_login"]["email"]
                login_password = data["chrome_login"]["password"]
        except OSError:
            print("No login data found in computer..")
    if login_email == "" or password_input == "":
        print("No login data was given. Reading information from the website instead.")

        all_login_data = driver.find_elements(By.CLASS_NAME, value="Login_credentialGroup__xutMX")

        login_data = all_login_data[USE_ADMIN_CREDENTIALS].find_elements(By.CLASS_NAME, value="Login_credentialDetail__Mu9oI")

        login_email = ""
        login_password = ""
        for entry in login_data:
            if "email" in entry.text.lower():
                login_email = entry.text.replace("Email: ", "")
            elif "password" in entry.text.lower():
                login_password = entry.text.replace("Password: ", "")
            else:
                print("Not email or password, ignoring...")

        if login_email == "" or login_password == "":
            print("Couldn't read email or password from website.")
        else:
            with open(file="login_data.json",mode="w") as file:
                data = {
                    "chrome_login": {
                        "email": login_email,
                        "password":login_password
                    }
                }
                json.dump(data, file, indent=4)
    
    email_input = driver.find_element(By.ID, value="email-input")
    password_input = driver.find_element(By.ID, value="password-input")
    email_input.send_keys(login_email)
    password_input.send_keys(login_password)
def booking_summary(booked_classes_in_session, waitlisted_classes_in_session):
    bookable_classes = 0
    waitlistable_classes = 0
    total_booked_classes = 0
    total_waitlisted_classes = 0

    week_schedue = driver.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")
    for day_schedule in week_schedue:
        classes = day_schedule.find_elements(By.CLASS_NAME, "ClassCard_cardHeader__D9pf3")

        for class_ in classes:
            book_class_btn = class_.find_element(By.CSS_SELECTOR, ".ClassCard_cardActions__tVZBm .ClassCard_bookButton__DMM1I")
            booking_status = book_class_btn.text
            
            if booking_status == "Book Class":
                bookable_classes += 1
            elif booking_status == "Join Waitlist":
                waitlistable_classes += 1
            elif booking_status == "Booked":
                total_booked_classes += 1
            elif booking_status == "Waitlisted":
                total_waitlisted_classes += 1
            else:
                print(f"Error finding booking status. Got: {booking_status}")
            
    print(
        "----------------------\n" \
        "   BOOKING SUMMARY\n" \
        "----------------------\n\n" \
        f" - Classes booked in this session: {booked_classes_in_session}\n" \
        f" - Waitlisted classes in this session: {waitlisted_classes_in_session}\n\n"
        f" - Total booked classes: {total_booked_classes}\n" \
        f" - Total waitlisted classes: {total_waitlisted_classes}\n\n"
        f" - Classes available to be booked: {bookable_classes}\n" \
        f" - Classes available to be waitlisted: {waitlistable_classes}\n\n"
    )

    return total_booked_classes, total_waitlisted_classes
def login_as_admin():
    print("Logging in as admin...")

    all_login_data = driver.find_elements(By.CLASS_NAME, value="Login_credentialGroup__xutMX")

    login_data = all_login_data[1].find_elements(By.CLASS_NAME, value="Login_credentialDetail__Mu9oI")

    login_email = ""
    login_password = ""
    for entry in login_data:
        if "email" in entry.text.lower():
            login_email = entry.text.replace("Email: ", "")
        elif "password" in entry.text.lower():
            login_password = entry.text.replace("Password: ", "")
        else:
            print("Not email or password, ignoring...")

    if login_email == "" or login_password == "":
        print("Couldn't read email or password from website.")
        raise LookupError
    
    email_input = driver.find_element(By.ID, value="email-input")
    password_input = driver.find_element(By.ID, value="password-input")
    email_input.send_keys(login_email)
    password_input.send_keys(login_password, Keys.ENTER)
def advance_three_days():
    advance_three_days_btn = driver.find_element(By.ID, "advance-3-days")
    advance_three_days_btn.click()
def logout():
    logout_btn = driver.find_element(By.ID, "logout-button")
    logout_btn.click()
def try_signup_or_login(func, retries=7):
    func()
    for attempt in range(retries):
        print(f"Starting login attempt #{attempt}")
        password_input = driver.find_element(By.ID, value="password-input")
        password_input.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        try:
            driver.find_element(By.ID, "error-message")
            print(f"Failed login attempt #{attempt}.")
            driver.implicitly_wait(10)
        except:
            print("Successfully logged in. Finding the next 6PM Tuesday class.")
            break
    if attempt >= 7:
        print("Couldn't login or signup")
        raise ConnectionRefusedError
def enable_simulation():
    enable_simulation_checkbox = driver.find_element(By.ID, value="network-enabled-toggle")
    enable_simulation_checkbox.click()

    driver.implicitly_wait(10)

    failure_rate_slider = driver.find_element(By.ID, "failure-rate-slider")
    failure_rate_slider.click()
    for _ in range(10):
        failure_rate_slider.send_keys(Keys.RIGHT)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

login_btn = driver.find_element(By.ID, value="login-button")
login_btn.click()

driver.implicitly_wait(10)

if TIME_TRAVEL:
    login_as_admin()
    driver.implicitly_wait(10)
    advance_three_days()
    driver.implicitly_wait(10)
    enable_simulation()
    driver.implicitly_wait(10)
    logout()
    driver.implicitly_wait(10)

login_btn = driver.find_element(By.ID, value="login-button")
login_btn.click()
driver.implicitly_wait(10)

if SIGN_UP:
    try_signup_or_login(func=signup)    
else:
    try_signup_or_login(func=login)

driver.implicitly_wait(10)


days_to_be_scheduled = ["Tue", "Thu"]
booked_classes_in_session = 0
waitlisted_classes_in_session = 0

week_schedue = driver.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")
for day_schedule in week_schedue:
    day_name = day_schedule.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs").text
    if "Tue" in day_name or "Thu" in day_name:
        tuesday_schedule = day_schedule

        classes = tuesday_schedule.find_elements(By.CLASS_NAME, "ClassCard_cardHeader__D9pf3")
        for class_ in classes:
            class_time = class_.find_element(By.CLASS_NAME, "ClassCard_classDetail__Z8Z8f").text
            class_time = class_time.replace("Time: ", "")
            if class_time == "6:00 PM":
                six_pm_class = class_

                class_name = f"{six_pm_class.find_element(By.CLASS_NAME, "ClassCard_className__q0kVz").text}"
                class_time_and_day = f"{tuesday_schedule.find_element(By.CLASS_NAME, "Schedule_dayTitle__YBybs").text}, {class_time}"
                book_class_btn = six_pm_class.find_element(By.CSS_SELECTOR, ".ClassCard_cardActions__tVZBm .ClassCard_bookButton__DMM1I")
                booking_status = book_class_btn.text
                if booking_status == "Book Class":
                    book_class_btn.click()
                    time.sleep(0.5)
                    booked_classes_in_session += 1
                    print(f"Successfully booked: {class_name} on {class_time_and_day}.")
                elif booking_status == "Join Waitlist":
                    book_class_btn.click()
                    time.sleep(0.5)
                    waitlisted_classes_in_session += 1
                    print(f"Successfully waitlisted: {class_name} on {class_time_and_day}.")
                elif booking_status == "Booked":
                    print(f"{class_name} on {class_time_and_day} is already booked.")
                elif booking_status == "Waitlisted":
                    print(f"{class_name} on {class_time_and_day} is already waitlisted.")
                else:
                    print("Error finding booking status.")
                    raise LookupError


total_booked_classes, total_waitlisted_classes = booking_summary(booked_classes_in_session, waitlisted_classes_in_session)

print("Checking if summary is correct....\n")
my_bookings_btn = driver.find_element(By.ID, "my-bookings-link")
my_bookings_btn.click()

driver.implicitly_wait(10)

confirmed_bookings = driver.find_element(By.ID, "confirmed-bookings-section").find_elements(By.CSS_SELECTOR, ".MyBookings_bookingCard__VRdrR")
total_confirmed_bookings = len(confirmed_bookings)

# confirmed_waitlists = driver.find_element(By.ID, "waitlist-section").find_elements(By.CSS_SELECTOR, ".MyBookings_waitlist__rD_tlR")
# total_confirmed_waitlists = len(confirmed_bookings)

print(
    " --- BOOKINGS ---\n" \
    f" - Expected: {total_booked_classes}\n" \
    f" - Found: {total_confirmed_bookings}\n\n" \
    # " --- WAITLISTS ---\n" \
    # f" - Expected: {total_waitlisted_classes}\n" \
    # f" - Found: {confirmed_waitlists}\n\n"
)

missing_books = total_confirmed_bookings - total_booked_classes

if missing_books == 0:
    print("✅ SUCCESS: All bookings are in order.")
elif missing_books > 0:
    print(f"❌ MISMATCH: Missing {missing_books} bookings.")
else:
    print(f"❌ MISMATCH: Extra {-missing_books} bookings.")



    
