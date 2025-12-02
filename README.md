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
