from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ApplicationformPage:

    def __init__(self, driver):                                         #driver as an argument in constructor
        self.driver = driver

    lastname = (By.XPATH,"(//input[@class='cxBorderBottom '])[1]")
    drpdown_firstnameelmnt = (By.XPATH,"//lyte-drop-item[@id='Lyte_Drop_Item_2']")
    firstname = (By.XPATH, "(//input[@class='cxBorderBottom '])[2]")
    email = (By.XPATH, "(//input[@class='cxBorderBottom '])[3]")
    mobile = (By.XPATH,"(//input[@class='cxBorderBottom '])[4]")
    zipostal = (By.XPATH, "(//input[@id='inputId'])[1]")
    state = (By.XPATH, "(//input[@id='inputId'])[2]")
    captcha = (By.LINK_TEXT, "Reload")
    submit = (By.XPATH, "//lyte-button[@id='cw-submit-btn']//button[@id='']")
    scrollup = (By.ID ,"back-top")
    cancel = (By.XPATH, "//button[@type='button']")









    def getlast_name(self):
        return self.driver.find_element(*ApplicationformPage.lastname)
    def getfirst_name(self):
        return self.driver.find_element(*ApplicationformPage.firstname)
    def getfirstname_drpdown(self):
        return Select(self.driver.find_element(*ApplicationformPage.drpdown_firstnameelmnt))
    def getemail_name(self):
        return self.driver.find_element(*ApplicationformPage.email)
    def getmobile_num(self):
        return self.driver.find_element(*ApplicationformPage.mobile)
    def getzipostal_tab(self):
        return self.driver.find_element(*ApplicationformPage.zipostal)
    def getstate_tab(self):
        return self.driver.find_element(*ApplicationformPage.state)
    def getcaptcha_reload(self):
        return self.driver.find_element(*ApplicationformPage.captcha)
    def get_submitbutton(self):
        return self.driver.find_element(*ApplicationformPage.submit)
    def get_scrollupbutton(self):
        return self.driver.find_element(*ApplicationformPage.scrollup)

    def get_cancelbutton(self):
        return self.driver.find_element(*ApplicationformPage.cancel)

