import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class Eosago(unittest.TestCase):
    def setUp(self):
        options = Options()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options)
        self.action = ActionChains(self.driver)

        self.driver.get('https://www.alfastrah.ru/')

    def test_e_osago(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        car_menu = self.driver.find_elements_by_class_name('calc__image')[0]
        self.action.move_to_element(car_menu).perform()
        time.sleep(1)
        osago_calc = self.driver.find_elements_by_class_name('calc-popup__link_online')
        osago_calc[1].click()
        time.sleep(3)
        try:
            modal_close_button2 = self.driver.find_elements_by_class_name('modal__close')[-1].click()
        except Exception as ex:
            print(ex)
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_id("fl-237207"))
            modal_close_button1 = self.driver.find_element_by_xpath('/html/body/div/div[3]/button[1]').click()
            self.driver.switch_to.default_content()
        except Exception as ex:
            print(ex)

        self.driver.execute_script("window.scrollTo(0, 500)")

        try:
            modal_close_button2 = self.driver.find_elements_by_class_name('modal__close')[-1].click()
        except Exception as ex:
            print(ex)
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_id("fl-237207"))
            modal_close_button1 = self.driver.find_element_by_xpath('/html/body/div/div[3]/button[1]').click()

        except Exception as ex:
            print(ex)

        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)

        category_ts = self.driver.find_elements_by_class_name("select2-selection__arrow")[0].click()
        category_ts_value = self.driver.find_elements_by_class_name("select2-results__option")[2].click()

        marka = self.driver.find_element_by_css_selector('.js-eosago-brand-name-input')
        time.sleep(3)
        marka.send_keys('Volkswagen')
        time.sleep(3)
        marka.send_keys(Keys.TAB)

        model = self.driver.find_element_by_css_selector('.js-eosago-model-name-input')
        time.sleep(3)
        model.send_keys('Golf Plus')
        time.sleep(3)

        year = self.driver.find_elements_by_class_name("select2-selection__arrow")[2].click()
        year_value = self.driver.find_elements_by_class_name("select2-results__option")[5].click()
        time.sleep(3)

        arenda_check = self.driver.find_elements_by_class_name("checkbox__indicatior")[0]
        self.driver.execute_script("window.scrollTo(0, 700)")
        arenda_check.click()

        auto_number = self.driver.find_element_by_id('AUTO_NUMBER')
        auto_number.send_keys('А111МР')
        auto_region = self.driver.find_element_by_id('AUTO_REGION')
        auto_region.send_keys('199')

        win_code = self.driver.find_elements_by_name('CarIdValue')[0]
        win_code.send_keys('KNDJC733545301768')

        button = self.driver.find_element_by_css_selector('.js-eosago-step1-form-auto-submit')
        button.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    while True:
        try:
            unittest.main()
            time.sleep(60)
        except Exception as e:
            print(e)
            unittest.main()
            time.sleep(60)