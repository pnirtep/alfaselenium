import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36")

driver = webdriver.Chrome(options=options)
action = ActionChains(driver)

main_page = driver.get('https://www.alfastrah.ru/')
time.sleep(5)
car_menu = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]')
action.move_to_element(car_menu).perform()
time.sleep(3)
osago_calc = driver.find_elements_by_class_name('calc-popup__link')
element = osago_calc[1].click()







