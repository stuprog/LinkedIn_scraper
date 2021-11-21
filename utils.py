from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def initialize():
    # Creating a webdriver instance
    s = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=s, options=options)
    driver.maximize_window()
    return driver


def scroll_down(driver, initial_scroll, final_scroll):
    start = time.time()
    while True:
        driver.execute_script(f"window.scrollTo({initial_scroll},{final_scroll})")
        # this command scrolls the window starting from
        # the pixel value stored in the initialScroll
        # variable to the pixel value stored at the
        # finalScroll variable
        initial_scroll = final_scroll
        final_scroll += 1000
        # we will stop the script for 3 seconds so that
        # the data can load
        time.sleep(1)
        # You can change it as per your needs and internet speed
        end = time.time()
        # We will scroll for 20 seconds.
        # You can change it as per your needs and internet speed
        if round(end - start) > 5:
            break


def extract_number(string):
    numbers = [int(word) for word in string.split() if word.isdigit()]
    return numbers
