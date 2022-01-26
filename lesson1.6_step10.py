from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    buttonGet = browser.find_element(By.ID, "book")
    buttonGet.click()


    def calc(param):
        return math.log(abs(12 * math.sin(param)))


    x = browser.find_element(By.ID, "input_value").text
    result = str(calc(int(x)))
    inputElement = browser.find_element(By.ID, "answer")
    inputElement.send_keys(result)

    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    time.sleep(5)
    browser.quit()

