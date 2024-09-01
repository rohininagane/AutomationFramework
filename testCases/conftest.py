import os
import shutil
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

@pytest.fixture()
def setup():
    browser = ReadConfig.getBrowserName()
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver


@pytest.fixture(scope="function")
def login(request,setup):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    driver = setup
    driver.implicitly_wait(5)  # Adjust wait time as necessary
    driver.maximize_window()
    try:
        driver.get(baseURL)
        lp = LoginPage(driver)
        lp.setUserName(username)
        lp.setPassword(password)
        lp.clickLogin()
    except:
        driver.save_screenshot(".\\Screenshots\\login_error.png")
        raise
    yield driver
    driver.quit()

    # Fixture to clear the logs directory at the start of the session
    @pytest.fixture(scope="session", autouse=True)
    def clear_logs_directory():
        logs_dir = os.path.join(".", "Logs")
        if os.path.exists(logs_dir):
            shutil.rmtree(logs_dir)  # Remove the logs directory and all its contents
        os.makedirs(logs_dir, exist_ok=True)  # Recreate the logs directory
        print(f"Logs directory cleared and recreated at: {logs_dir}")

