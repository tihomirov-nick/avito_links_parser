from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

driver = Chrome(options=options)

url = 'https://www.avito.ru/sankt-peterburg?q=куртка'
full_ad_url = 'https://www.avito.ru/sankt-peterburg/odezhda_obuv_aksessuary/dzhinsovka_stone_island_3035547878'
ad_url = '/sankt-peterburg/odezhda_obuv_aksessuary/dzhinsovka_stone_island_3035547878'

driver.get(url=url)

found = False

while found != True:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@itemprop="url"]')))
    links = [element.get_attribute('href') for element in elements]

    if full_ad_url in links:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//a[@itemprop="url" and @href="{ad_url}"]')))
        element.click()
        time.sleep(10)
        break

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div[3]/div[3]/nav/ul/li[4]')))
    element.click()

driver.quit()