import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_naukri():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 30)

    driver.get("https://www.naukri.com/nlogin/login")
    driver.maximize_window()
    driver.implicitly_wait(100)
    # Credentials (move to env later in Jenkins)
    driver.find_element(By.ID, "usernameField").send_keys("vijay.anegondi2001@gmail.com")
    driver.find_element(By.ID, "passwordField").send_keys("Vijay@8500")

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Wait for profile link
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/mnjuser/profile"]'))).click()

    # File path (PROJECT RELATIVE - IMPORTANT for Jenkins)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "resume", "Vijay Anegondi.pdf")

    print("File path:", file_path)
    print("Exists:", os.path.exists(file_path))

    # Upload
    upload = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    upload.send_keys(file_path)

    time.sleep(5)

    print("✅ Resume upload triggered")

    driver.quit()