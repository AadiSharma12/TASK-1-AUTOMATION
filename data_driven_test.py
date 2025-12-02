import csv
import logging
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# ==============================
# LOGGING SETUP
# ==============================
LOG_FILE = "login_test_log.txt"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("===== LOGIN TEST RUN STARTED =====")

# ==============================
# SELENIUM SETUP
# ==============================
try:
    driver = webdriver.Chrome()  # uses default Chrome / Selenium Manager
except WebDriverException as e:
    print("❌ Could not start Chrome WebDriver. Make sure Google Chrome is installed.")
    print(e)
    raise

driver.maximize_window()

# ==============================
# LOCAL HTML PAGE (RELATIVE PATH)
# ==============================
html_path = os.path.abspath("login.html")
URL = f"file:///{html_path.replace(os.sep, '/')}"  # works on any OS

# ==============================
# CORE TEST FUNCTION
# ==============================
def run_login_test(username: str, password: str, expected_result: str):
    """
    Runs one login test on login.html using data from CSV.
    expected_result: 'success' or 'failure'
    Returns: (status: 'PASS'/'FAIL', details: str)
    """
    try:
        driver.get(URL)

        # Locate elements
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginBtn")

        # Enter values
        username_input.clear()
        password_input.clear()
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        # Read message shown on page
        message_element = driver.find_element(By.ID, "message")
        message_text = message_element.text.strip()

        # Our page shows one of:
        # "Login successful. Welcome, ...!"
        # "Invalid username or password."

        if expected_result == "success":
            if "Login successful" in message_text:
                return "PASS", (
                    f"Login SUCCESS as expected for user '{username}'. "
                    f"Page message: '{message_text}'"
                )
            else:
                return "FAIL", (
                    f"Expected SUCCESS for user '{username}', "
                    f"but page message was: '{message_text}'"
                )

        elif expected_result == "failure":
            if "Invalid username or password" in message_text:
                return "PASS", (
                    f"Login FAILED as expected for user '{username}'. "
                    f"Page message: '{message_text}'"
                )
            else:
                return "FAIL", (
                    f"Expected FAILURE for user '{username}', "
                    f"but page message was: '{message_text}'"
                )

        else:
            return "FAIL", f"Invalid expected_result in CSV: '{expected_result}'"

    except NoSuchElementException as e:
        return "FAIL", f"Element not found on page. Error: {e}"
    except Exception as e:
        return "FAIL", f"Unexpected error during test. Error: {e}"

# ==============================
# MAIN: READ CSV & RUN ALL TESTS
# ==============================
INPUT_CSV = "login_test_data.csv"
OUTPUT_CSV = "login_test_results.csv"

results = []

with open(INPUT_CSV, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username = row["username"]
        password = row["password"]
        expected = row["expected_result"].strip().lower()
        purpose = row.get("purpose", "").strip()

        status, details = run_login_test(username, password, expected)

        log_line = (
            f"[{status}] User='{username}', Password='{password}', "
            f"Expected={expected.upper()}, Purpose='{purpose}'. Details: {details}"
        )

        if status == "PASS":
            logging.info(log_line)
        else:
            logging.error(log_line)

        results.append({
            "username": username,
            "password": password,
            "expected_result": expected,
            "purpose": purpose,
            "status": status,
            "details": details
        })

# Close browser after all tests
driver.quit()
logging.info("===== LOGIN TEST RUN FINISHED =====")

# ==============================
# SAVE RESULTS TO CSV
# ==============================
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["username", "password", "expected_result", "purpose", "status", "details"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("✅ All tests finished.")
print(f"📄 Results saved to: {OUTPUT_CSV}")
print(f"🧾 Log saved to: {LOG_FILE}")
