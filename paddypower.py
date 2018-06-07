from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("chromedriver")
BASE_URL = "https://www.paddypower.com/"
driver.get(BASE_URL)

game = 'football'
category = "World Cup 2018".lower()
menu__sections = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "menu__section"))
)

for menu__section in menu__sections:
    menu__items = WebDriverWait(menu__section, 20).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "menu__item"))
    )
    for menu__item in menu__items:
        if menu__item.text.lower() == game:
            menu__item.click()

            ribbon__contents = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "ribbon__content"))
            )
            for ribbon__content in ribbon__contents:
                ribbon__items = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "ribbon__item"))
                )

                for ribbon__item in ribbon__items:
                    if ribbon__item.text.lower() == category:
                        print(ribbon__item.text)
                        ribbon__item.click()
                        accordion__headers=WebDriverWait(driver, 20).until(
                            EC.presence_of_all_elements_located(
                                (By.CLASS_NAME, "accordion__header"))
                        )
                        for h in accordion__headers:
                            print(h.text)
                            h.click()

                        outright_items = WebDriverWait(driver, 20).until(
                            EC.presence_of_all_elements_located(
                                (By.CLASS_NAME, "outright-item"))
                        )
                        for outright_item in outright_items:
                            print(outright_item.text)
                        driver.quit()
                        exit()
