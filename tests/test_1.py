import allure
from absolute import SearchMethods
from allure_commons.types import AttachmentType
import time
from selenium.webdriver.support.ui import WebDriverWait
import requests
from selenium.webdriver.common.keys import Keys
import pytest

users = [("Виктор Иванов Ига", 11111995, 4444666666, 11072023, 'Мамаева ш., 27А, стр. 2', 9999999999, '@absolutins.ru'),
         ("Виктор", 111119, 'qweqwe', 11072023, 'Мамаева ш., 27А, стр. 2', 9999999999, '@absolutins.ru'),
         ("Виктор 2", 11, 4444666666, 11072023, ',,,', 9999999999, '@absolutins.ru'),
         ("Виктор Иванов Ига", 11111995, 4444666666, 11072023, 'Мамаева ш., 27А, стр. 2', 9999999999, '@absolutins.ru'),
         (". . .", '"', '@absolutins.ru', 11072023, 'Мамаева ш., 27А, стр. 2', 9999999999, '@absolutins.ru'),
         (", , ,", 11111995, 4444666666, 'один два три', 'asdadasd', 9999999999, "@absolutins.ru"),
         ("! ! !", 11111995, '/////', 11072023, 'Мамаева ш., 27А, стр. 2', 9999999999, '@absolutins.ru'),
         ("   ", 11111995, 4444666666, 11072023, '2222222', 9999999999, '@absolutins.ru'),
         ("                  ", 11111995, 4444666666, 11072023, 'Мамаева ш., 27А, стр. 2', 'qwewqeqwe',
          '@absolutins.ru'),
         ("111 1111 111", 11111995, 4444666666, 11072023, 'Мамаева ш., 27А, стр. 2', 9999999999,
          "qwe@absolutins.ru') drop table qweqwwasasddasdqdsdsffqf--")]


# Заменить на Faker или сгенирировать через Copilot


@allure.description("Valid status")
@allure.title("Test status")
# @pytest.mark.run(order=3)
@allure.story('Позитивный сценарий по запросу')
def test_status_code(browser):
    """
    python -m pytest test_1.py --alluredir ./results
    allure serve ./results
    """
    with allure.step("Проверка ответа на запрос"):
        try:
            page_info = requests.get('https://old.absolutins.ru/kupit-strahovoj-polis'
                                     '/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/')
            assert page_info.status_code == 200
        except:
            allure.attach(name='fileName', body=browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise


@allure.story('Позитивный сценарий')
def test_positive(browser):
    with allure.step("Заполнение, как предполагается правильно"):
        try:
            # начало сессии
            absolute_page = SearchMethods(browser)
            # открытие тестовой страницы
            absolute_page.go_to_site("https://old.absolutins.ru/"
                                     "kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/")
            # клик по чекбоксу 'контакт с вирусом'
            absolute_page.click_on_the_search_checkbox_corona()
            # клик по чекбоксу
            absolute_page.click_on_the_search_checkbox_agree()
            # клик по кнопке 'Продолжить
            absolute_page.click_on_the_search_checkbox_calculate()
            # заполнение Имени
            absolute_page.enter_fullname('Alexey Buravilin')
            # заполнение даты рождения паспорта
            absolute_page.enter_date_birth(11111995)
            # заполнение поля серия паспорта
            absolute_page.enter_series_numbers_passport('4444666666')
            # заполнение поля дата
            absolute_page.enter_date_passport(11072023)
            # заполнение поля адрес
            absolute_page.enter_address('Алтуфьевское ш., 27А, стр. 2')
            # заполнение поля телефон
            absolute_page.enter_phone(9999999999)
            # заполнение поля email
            absolute_page.enter_email('testmail@absolutins.ru')
            # заполнение поля email
            absolute_page.click_on_the_search_button_payment()
            WebDriverWait(browser, 15).until(lambda driver: browser.current_url != "https://old.absolutins.ru/"
                                                                                   "kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/")
            assert browser.execute_script("return document.URL;")[:33] == 'https://securepayments.tinkoff.ru'
        except:
            allure.attach(name='fileName', body=browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise


@allure.story('Заполнение некорректным типом данных')
@allure.severity('critical')
def test_negative_1(browser):
    with allure.step("Проверка негативного сценария 1"):
        try:
            # начало сессии
            absolute_page = SearchMethods(browser)
            # открытие тестовой страницы
            absolute_page.go_to_site("https://old.absolutins.ru/"
                                     "kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/")
            # клик по чекбоксу 'контакт с вирусом'
            absolute_page.click_on_the_search_checkbox_corona()
            # клик по чекбоксу
            absolute_page.click_on_the_search_checkbox_agree()
            # клик по кнопке 'Продолжить
            absolute_page.click_on_the_search_checkbox_calculate()
            # заполнение Имени
            absolute_page.enter_fullname('111')
            # заполнение даты рождения паспорта
            absolute_page.enter_date_birth('qwe')
            # заполнение поля серия паспорта
            absolute_page.enter_series_numbers_passport('qwe')
            # заполнение поля дата
            absolute_page.enter_date_passport('qwe')
            # заполнение поля адрес
            absolute_page.enter_address('...')
            # заполнение поля телефон
            absolute_page.enter_phone('qwe')
            # заполнение поля email
            absolute_page.enter_email('111')
            # заполнение поля email
            absolute_page.click_on_the_search_button_payment()
            print(absolute_page.check_error_name())
            assert absolute_page.check_error_name() is not None
            assert absolute_page.check_error_date_birth() is not None
            assert absolute_page.check_error_passport_series_numbers() is not None
            assert absolute_page.check_error_passport_series_numbers() is not None
            assert absolute_page.check_error_name() is not None
            assert absolute_page.check_error_name() is not None
        except:
            allure.attach(name='fileName', body=browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise


@allure.description("Negative_2")
@allure.title("invalid test")
@pytest.mark.parametrize("fullname, date_birth, series_numbers_passport, date_passport, address, phone, email", users)
# @pytest.mark.run(order=3)
@allure.story('Заполнение пустотой')
@allure.severity('critical')
def test_negative_2(browser, fullname, date_birth, series_numbers_passport, date_passport, address, phone, email):
    with allure.step("Проверка негативного сценария 2"):
        try:
            # начало сессии
            absolute_page = SearchMethods(browser)
            # открытие тестовой страницы
            absolute_page.go_to_site("https://old.absolutins.ru/"
                                     "kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/")
            # клик по чекбоксу 'контакт с вирусом'
            absolute_page.click_on_the_search_checkbox_corona()
            # клик по чекбоксу
            absolute_page.click_on_the_search_checkbox_agree()
            # клик по кнопке 'Продолжить
            absolute_page.click_on_the_search_checkbox_calculate()
            # заполнение Имени
            absolute_page.enter_fullname(fullname)
            # заполнение даты рождения паспорта
            absolute_page.enter_date_birth(date_birth)
            # заполнение поля серия паспорта
            absolute_page.enter_series_numbers_passport(series_numbers_passport)
            # заполнение поля дата
            absolute_page.enter_date_passport(date_passport)
            # заполнение поля адрес
            absolute_page.enter_address(address)
            # заполнение поля телефон
            absolute_page.enter_phone(phone)
            # заполнение поля email
            absolute_page.enter_email(email)
            # заполнение поля email
            absolute_page.click_on_the_search_button_payment()
            print(absolute_page.check_error_name())
            assert absolute_page.check_error_name() is not None


        except:
            allure.attach(name='fileName', body=browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            raise
        with allure.step("ЧНЕ"):
            try:
                assert absolute_page.check_error_date_birth() is not None
                assert absolute_page.check_error_passport_series_numbers() is not None
                assert absolute_page.check_error_passport_series_numbers() is not None
                assert absolute_page.check_error_name() is not None
                assert absolute_page.check_error_name() is not None
            except:
                allure.attach(name='fileName', body=browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
                raise
