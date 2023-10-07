from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

driver = Chrome(options=options)

url = "https://www.avito.ru"
driver.get(url=url)

login = "login"
password = "password"

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='index-nav-link-muv1u index-login-NV2z_']"))).click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='login']"))).send_keys(login)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(password)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'css-1kdcmzd') and contains(text(), 'Войти')]"))).click()

url = "https://www.avito.ru/sankt-peterburg/odezhda_obuv_aksessuary/dzhinsovka_stone_island_3035547878"
driver.get(url=url)

# Получение текста из поля "item-id"
num = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@data-marker='item-view/item-id']"))
    ).text

# Получение текста из поля "total-views"
total_views = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@data-marker='item-view/total-views']"))
    ).text

# Получение текста из поля "item-date"
item_date = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@data-marker='item-view/item-date']"))
    ).text

# Получение текста из поля "rating"
rating = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@data-marker='rating-caption/rating']"))
    ).text

# Получение текста из элемента с классом "SnippetBadge-title-oSImJ"
sells = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//span[@class='SnippetBadge-root-Vp6bq']"))
    )
sells_arr = [sell.text for sell in sells]

# Получение текста из элемента с классом "desktop-9uhrzn"
advertisements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class, 'desktop-9uhrzn')]"))
    )
advertisements_arr = [advertisement.text for advertisement in advertisements]

# Вывод полученного текста
print("Ad num:", num)
print("Total views:", total_views)
print("Item date:", item_date)
print("Rating:", rating)
print("Sells count:", sells_arr)
print("Advertisements count:", advertisements_arr)
