from selenium.webdriver.common.keys import Keys
from time import sleep
from conftest import driver, is_visible_by_xpath, is_visible_by_ID
import pickle
from selenium.webdriver.common.by import By

count = 0

def cook_cookies():
    login = 'tn.srgv@yandex.com'
    logining = driver.find_element(By.ID, 'email')
    logining.send_keys(login)
    logining.send_keys(Keys.ENTER)
    pickle.dump(driver.get_cookies(), open('cookies-workzilla', 'wb'))


def load_cookies():
    for coockie in pickle.load(open('cookies-workzilla', 'rb')):
        driver.add_cookie(coockie)

def parsing():
    keywords = ["парс", "собрат", "парсинг", "тикток", "тик-ток", "tik-tok", "тик ток", "tik tok", "собрать", "базу"]
    global count
    print(count)

    if count == 0:
        url = 'https://client.work-zilla.com/freelancer'
        driver.get(url)

        is_visible_by_ID('email')
        load_cookies()

    driver.refresh()
    is_visible_by_xpath('//div[@class="normal-top"]')
    tasks = []
    count += 1
    try:
        elements = driver.find_elements(By.XPATH, '//div[@class="normal-top"]')
        for element in elements:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            title_text = element.find_element(By.XPATH, './div/h3/div/div')
            if any(keyword in title_text.text.lower() for keyword in keywords):
                web = element.find_element(By.XPATH, './/a').get_attribute('href')
                tasks.append(web)

        if len(tasks) == 0:
            tasks.append("заданий по парсингу нет")

        return tasks

    except Exception as ex:
        pass

    finally:
       pass
        # driver.close()
        # driver.quit()
