from selenium import webdriver # pip install selenium

# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://python.org")

driver.maximize_window()
time.sleep(5)
driver.quit()