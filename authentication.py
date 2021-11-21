from selenium.webdriver.common.by import By


def connect_to_linkedin(driver, username_input, password_input):
    driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys(username_input)
    password.send_keys(password_input)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()