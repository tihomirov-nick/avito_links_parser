import tkinter as tk
from tkinter import messagebox
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def start_parsing():
    url = url_entry.get()
    iterations = int(iterations_entry.get())
    login = login_entry.get()
    password = password_entry.get()

    options = ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    driver = Chrome(options=options, driver_executable_path="chromedriver.exe")
    driver.get(url=url)

    if login and password:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='index-nav-link-muv1u index-login-NV2z_']"))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='login']"))).send_keys(login)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'css-1kdcmzd') and contains(text(), 'Войти')]"))).click()

    time.sleep(10)

    links = []
    for i in range(iterations):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.styles-module-root-QmppR.styles-module-root_noVisited-aFA10.styles-module-root_preset_black-JkIdG')))
        page_links = [element.get_attribute('href') for element in elements]
        links.extend(page_links)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.styles-module-item-kF45w.styles-module-item_arrow-sxBqe.styles-module-item_size_s-Tvz95.styles-module-item_link-_bV2N'))).click()

    driver.quit()

    with open('links.txt', 'w', encoding="utf-8") as f:
        for link in links:
            f.write(f"{link}\n")

    messagebox.showinfo("Готово!", "Парсинг успешно завершен!")

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

root = tk.Tk()
root.title("Парсер AVITO")
root.geometry("500x300")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True, fill="both")

url_label = tk.Label(frame, text="Ссылка на главную поисковую страницу:")
url_label.pack()

url_entry = tk.Entry(frame)
url_entry.pack(fill="x")

iterations_label = tk.Label(frame, text="Кол-во страниц для поиска:")
iterations_label.pack()

iterations_entry = tk.Entry(frame)
iterations_entry.pack(fill="x")

login_label = tk.Label(frame, text="Логин:")
login_label.pack()

login_entry = tk.Entry(frame)
login_entry.pack(fill="x")

password_label = tk.Label(frame, text="Пароль:")
password_label.pack()

password_entry = tk.Entry(frame)
password_entry.pack(fill="x")

start_button = tk.Button(frame, text="Начать парсинг", command=start_parsing)
start_button.pack(pady=10)

context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Вставить", command=lambda: root.focus_get().event_generate("<<Paste>>"))

url_entry.bind("<Button-3>", show_context_menu)
iterations_entry.bind("<Button-3>", show_context_menu)
login_entry.bind("<Button-3>", show_context_menu)
password_entry.bind("<Button-3>", show_context_menu)

root.mainloop()
