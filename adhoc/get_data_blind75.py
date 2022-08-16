
# https://www.analyticsvidhya.com/blog/2020/08/web-scraping-selenium-with-python/

# pip install selenium
# pip install webdriver-manager
# pip install Pillow

import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import pandas as pd

# open browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# go to neetcode
url = "https://neetcode.io/"
driver.get(url)

# MANUAL: expand all folds
results = driver.find_elements(By.CLASS_NAME, "table-text")

recs = []
for r in results:
    recs.append((r.text,r.get_attribute("href")))

df = pd.DataFrame(recs)
df.columns = ["Text", "Link"]
df.to_csv("blind75.csv", index = False)


