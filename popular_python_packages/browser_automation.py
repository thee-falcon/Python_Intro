# with selenium we can automate out browser, so we can write a bunch of scripts to test various functions on a website.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def cleanup_chrome():
    try:
        # For Mac
        os.system("killall 'Google Chrome'")
        time.sleep(2)  # Wait for processes to clean up
    except Exception as e:
        print(f"Error during cleanup: {e}")

try:
    cleanup_chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # This keeps the browser open

    chrome = webdriver.Chrome(options=options)
    chrome.get("https://github.com/")
    sign_in_link = chrome.find_element(By.LINK_TEXT, "Sign in")
    print("Sign in link found: ", sign_in_link.text)
    sign_in_link.click()
    username_box = chrome.find_element(By.ID, "login_field")
    username_box.send_keys("username")
    password_box = chrome.find_element(By.ID, "password")
    password_box.send_keys("password")
    password_box.submit()
    
    # profile_link = chrome.find_element(By.CLASS_NAME, ".Truncate__StyledTruncate-sc-23o1d2-0")
    # attri = profile_link.get_attribute("innerHTML")
    # assert "thee-falcon" in attri
except Exception as e:
    print(f"An error occurred. {e}")
finally:
    chrome.quit()