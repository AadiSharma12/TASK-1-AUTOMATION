# Data-Driven Login Test with Selenium (Local HTML)

This project demonstrates **data-driven testing** using **Selenium WebDriver** and a **local HTML login page**.

## ✅ Valid Credentials

Only this combination is treated as **correct**:

- **Username:** `aadisharma`  
- **Password:** `aadi99`

All other username/password combinations should fail.

---

## 📁 Files

- `login.html` – Simple login page (front-end) with JavaScript validation  
- `login_test_data.csv` – Test data (multiple username/password combinations)  
- `data_driven_test.py` – Python script using Selenium to run data-driven tests  
- `login_test_results.csv` – Generated after running tests (contains PASS/FAIL for each row)  
- `login_test_log.txt` – Log file with detailed messages for each test

---

## 🧰 Requirements

- Python 3.8+
- Google Chrome installed
- Python package: `selenium`

Install Selenium:

```bash
pip install selenium
------------------How to Run This Project----------------------------
Step 1 — Install Requirements

Make sure Python is installed, then install Selenium:

pip install selenium

Step 2 — Download/Clone the Repository
git clone https://github.com/AadiSharma12/TASK-1-AUTOMATION


—or download the ZIP and extract it.

Step 3 — Open Command Prompt in the Project Folder

Example:

cd TASK-1-AUTOMATION

Step 4 — Run the Script
python data_driven_test.py

Step 5 — View Output

After execution, check:

login_test_results.csv → Test results

login_test_log.txt → Log messages

✔ Expected Behavior

Only login with:
Username: aadisharma
Password: aadi99
should pass.

All other username/password combinations should fail.
