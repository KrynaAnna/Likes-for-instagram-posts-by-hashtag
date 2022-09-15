from authentication import login, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random

a, b, c = 'sweets', 'love', 'ontario'
# LOG IN


def hashtag(login, password):
    browser = webdriver.Chrome('D:\chromedriver.exe')
    browser.implicitly_wait(8)
    browser.get('https://www.instagram.com')
    time.sleep(random.randrange(6,9))

    _a_button = browser.find_element_by_css_selector('button[class="aOOlW  bIiDR  "]')
    _a_button.click()

    _login = browser.find_element(By.NAME, "username")
    _login.clear()
    _login.send_keys(login)

    time.sleep(random.randrange(3,5))

    _password = browser.find_element(By.NAME, "password")
    _password.clear()
    _password.send_keys(password)

    time.sleep(random.randrange(10))

    _b_button = browser.find_element_by_css_selector('button[type ="submit"]')
    _b_button.click()
    time.sleep(random.randrange(4,8))
    _c_button = browser.find_element_by_css_selector('button[class="sqdOP yWX7d    y3zKF     "]')
    _c_button.click()
    time.sleep(random.randrange(4,8))
    _d_button = browser.find_element_by_css_selector('button[class="aOOlW   HoLwm "]')
    _d_button.click()
    time.sleep(random.randrange(4,8))
    
# HASHTAGS
    
    hashtags=[a, b, c]
    for h in hashtags:

        browser.get(f'https://www.instagram.com/explore/tags/{h}/')
        time.sleep(random.randrange(3,5))

        for i in range(1, 2): #10
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3,5))
        hrefs = browser.find_elements_by_tag_name('a')
        links = []
        for item in hrefs:
            href = item.get_attribute('href')
            if "/p/" in href:
              links.append(href)

        for link in links[0:3]:
            browser.get(link)
            time.sleep(random.randrange(5,10))

            like_button = browser.find_element_by_class_name("fr66n").click()
            time.sleep(random.randrange(5,10))

            try:
                _d_button = browser.find_element_by_css_selector('button[class="aOOlW   HoLwm "]').click()
                time.sleep(5,10)
            except:
                pass

        print('Hashtag ' + h + ' done!')


hashtag(login, password)
