import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



def alfa_test():

    options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    action = ActionChains(driver)

    main_page = driver.get('https://www.alfastrah.ru/')
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    car_menu = driver.find_elements_by_class_name('calc__image')[0]
    action.move_to_element(car_menu).perform()
    time.sleep(1)
    osago_calc = driver.find_elements_by_class_name('calc-popup__link_online')
    e = osago_calc[1].click()
    time.sleep(3)

    try:
        modal_close_button2 = driver.find_elements_by_class_name('modal__close')[-1].click()
    except Exception as ex:
        print(ex)
    try:
        driver.switch_to.frame(driver.find_element_by_id("fl-237207"))
        modal_close_button1 = driver.find_element_by_xpath('/html/body/div/div[3]/button[1]').click()
        driver.switch_to.default_content()
    except Exception as ex:
        print(ex)

    driver.execute_script("window.scrollTo(0, 500)")

    try:
        modal_close_button2 = driver.find_elements_by_class_name('modal__close')[-1].click()
    except Exception as ex:
        print(ex)
    try:
        driver.switch_to.frame(driver.find_element_by_id("fl-237207"))
        modal_close_button1 = driver.find_element_by_xpath('/html/body/div/div[3]/button[1]').click()

    except Exception as ex:
        print(ex)

    driver.switch_to.default_content()
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)

    category_ts = driver.find_elements_by_class_name("select2-selection__arrow")[0].click()
    category_ts_value = driver.find_elements_by_class_name("select2-results__option")[2].click()

    # marka = driver.find_elements_by_name('brand_name')[0].send_keys('Volkswagen')
    marka = driver.find_element_by_css_selector('.js-eosago-brand-name-input')
    time.sleep(3)
    marka.send_keys('Volkswagen')
    time.sleep(3)
    marka.send_keys(Keys.TAB)

    model = driver.find_element_by_css_selector('.js-eosago-model-name-input')
    time.sleep(3)
    model.send_keys('Golf Plus')
    time.sleep(3)

    year = driver.find_elements_by_class_name("select2-selection__arrow")[2].click()
    year_value = driver.find_elements_by_class_name("select2-results__option")[5].click()
    time.sleep(3)


    arenda_check = driver.find_elements_by_class_name("checkbox__indicatior")[0]
    driver.execute_script("window.scrollTo(0, 700)")
    arenda_check.click()

    auto_number = driver.find_element_by_id('AUTO_NUMBER')
    auto_number.send_keys('А111МР')
    auto_region = driver.find_element_by_id('AUTO_REGION')
    auto_region.send_keys('199')

    win_code = driver.find_elements_by_name('CarIdValue')[0]
    win_code.send_keys('KNDJC733545301768')

    button = driver.find_element_by_css_selector('.js-eosago-step1-form-auto-submit')
    button.click()
    driver.quit()

    return



if __name__ == "__main__":
    while True:
        try:
            start_time = time.time()
            alfa_test()
            print("--- %s seconds ---" % (time.time() - start_time))
            time.sleep(60)
        except Exception as e:
            print(e)
            time.sleep(60)



