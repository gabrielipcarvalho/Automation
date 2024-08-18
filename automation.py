from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = Options()

# Specify the path to chromedriver using Service
service = Service("/Users/gabriel/PycharmProjects/automation/chromedriver")

# Create a Chrome WebDriver instance with the specified service and options
chrome_browser = webdriver.Chrome(service=service, options=options)

chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
assert "Selenium Easy Demo" in chrome_browser.title
show_button_text = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
print(show_button_text.get_attribute("innerHTML"))
assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, "user-message")

user_button2 = WebDriverWait(chrome_browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#get-input .btn"))
)
print(user_button2)

user_message.clear()
user_message.send_keys("I am very happy!")

show_button_text.click()

output_message = chrome_browser.find_element(By.ID, "display")
assert "I am very happy!" in output_message.text

input("press enter to finish...")
chrome_browser.quit()
