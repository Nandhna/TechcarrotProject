from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import time

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


driver = None


@pytest.fixture(scope="class")
def setup(request):
    print('Executing setup fixture')

    global driver
    headless_mode = True

    browser_name = request.config.getoption("browser_name")
    print(browser_name)
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\NandhanaRajendran\\chromedriver_win32\\chromedriver.exe")
    # Firefox invocation Gecko Driver
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path="C:\\Users\\NandhanaRajendran\\geckodriver-v0.31.0-win64\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\Users\\NandhanaRajendran\\edgedriver_win32\\msedgedriver.exe")

    driver.get("https://techcarrot.ae/")
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    print(driver.current_window_handle)
    request.cls.driver = driver



























'''@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            full_file_name = report.nodeid.replace("::", "_")
            timestr = time.strftime("%Y%m%d-%H%M%S")
            file_name = "../screenshots/" + full_file_name + "_" + timestr + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)'''
