from elements import WebElement
from selenium.webdriver.common.by import By


class Locators:
    """ return tuple """
    # Контакт с коронавирусом
    LOCATOR_VIRUS_CONTACT_CHECKBOX = (By.XPATH, "//input[@name='virus-contact']/following-sibling::span")
    # Согласие
    LOCATOR_AGREE_CHECKBOX = (By.XPATH, "//input[@name='agree-polis']/following-sibling::span")
    # Продолжить
    LOCATOR_CALCULATE_BUTTON = (By.XPATH, "//button[@name='calculate']")
    # Продолжить (выключена)
    # LOCATOR_STEP1_OFF_BUTTON = (By.XPATH, "//div[@class='step1' and @style='display: none;']")
    # Имя страхователя
    LOCATOR_NAME_FIELD = (By.XPATH, "//label[@for='name']/following-sibling::input[1]")
    # Дата рождения страхователя
    LOCATOR_DATE_BIRTH_FIELD = (By.CSS_SELECTOR, "#dateBirth")
    # Серия/номер паспорта
    LOCATOR_PASSPORT_SERIES_NUMBERS_FIELD = (By.CSS_SELECTOR, "#id")
    # Дата выдачи паспорта
    LOCATOR_PASSPORT_ISSUE_DATE_FIELD = (By.CSS_SELECTOR, "#idDate")
    # Адрес
    LOCATOR_ADDRESS_FIELD = (By.CSS_SELECTOR, "#address")
    # Телефон
    LOCATOR_PHONE_FIELD = (By.CSS_SELECTOR, "#phone")
    # Почта
    LOCATOR_EMAIL_FIELD = (By.CSS_SELECTOR, "#email")
    # Перейти к оплате
    LOCATOR_PAYMENT_BUTTON = (By.XPATH, "//button[text()='Перейти к оплате']")


class Errors:
    ERROR_NAME = (By.XPATH, "//div[@class='error' and text()='Не указана фамилия.']")
    ERROR_DATE_BIRTH = (By.XPATH, "//div[@class='error' and text()='Не указана дата рождения.']")
    ERROR_PASSPORT_SERIES_NUMBERS = (By.XPATH, "//div[@class='error' and text()='Не указаны серия/номер паспорта.']")
    ERROR_PASSPORT_ISSUE_DATE = (By.XPATH, "//div[@class='error' and text()='Не указаны дата выдачи паспорта.']")
    ERROR_PHONE = (By.XPATH, "//div[@class='error' and text()='Не указан номер телефона.']")
    ERROR_EMAIL = (By.XPATH, "//div[@class='error' and text()='Не указан E-Mail.']")


class SearchMethods(WebElement):
    def click_on_the_search_checkbox_corona(self):
        return self.find_element(Locators.LOCATOR_VIRUS_CONTACT_CHECKBOX, 2).click()

    def click_on_the_search_checkbox_agree(self):
        return self.find_element(Locators.LOCATOR_AGREE_CHECKBOX, 2).click()

    def click_on_the_search_checkbox_calculate(self):
        return self.find_element(Locators.LOCATOR_CALCULATE_BUTTON, 2).click()

    def enter_fullname(self, word):
        # self.execute_script(f'''document.querySelector("#name").click()''')
        search_field = self.find_element(Locators.LOCATOR_NAME_FIELD)
        search_field.send_keys(word)
        return search_field

    def enter_date_birth(self, word):
        search_field = self.find_element(Locators.LOCATOR_DATE_BIRTH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_series_numbers_passport(self, word):
        search_field = self.find_element(Locators.LOCATOR_PASSPORT_SERIES_NUMBERS_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_date_passport(self, word):
        search_field = self.find_element(Locators.LOCATOR_PASSPORT_ISSUE_DATE_FIELD)
        search_field.click()
        search_field.send_keys(word)
        search_field.click()
        return search_field

    def enter_address(self, word):
        search_field = self.find_element(Locators.LOCATOR_ADDRESS_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_phone(self, word):
        search_field = self.find_element(Locators.LOCATOR_PHONE_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def enter_email(self, word):
        search_field = self.find_element(Locators.LOCATOR_EMAIL_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button_payment(self):
        return self.find_element(Locators.LOCATOR_PAYMENT_BUTTON, 2).click()

    # errors
    def check_error_name(self):
        return self.find_elements(Errors.ERROR_NAME, 2)

    def check_error_date_birth(self):
        return self.find_elements(Errors.ERROR_DATE_BIRTH, 2)

    def check_error_passport_series_numbers(self):
        return self.find_elements(Errors.ERROR_PASSPORT_SERIES_NUMBERS, 2)

    def check_error_passport_issue_date(self):
        return self.find_elements(Errors.ERROR_PASSPORT_ISSUE_DATE, 2)

    def check_error_phone(self):
        return self.find_elements(Errors.ERROR_PHONE, 2)

    def check_error_email(self):
        return self.find_elements(Errors.ERROR_EMAIL, 2)

