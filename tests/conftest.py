import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser() -> webdriver:
    options = Options()
    # options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("force-device-scale-factor=0.75")
    options.add_argument("high-dpi-support=0.75")
    # options.add_argument("--width=1020")
    # options.add_argument("--height=800")
    # options.add_argument("--disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")
    # service = Service(ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=service, options=options)

    driver = webdriver.Chrome(options=options)

    #driver.implicitly_wait(10)
    yield driver
    driver.quit()
