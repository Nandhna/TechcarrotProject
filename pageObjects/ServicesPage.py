from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ServicesPage:

    def __init__(self, driver):                                         #driver as an argument in constructor
        self.driver = driver


    qualityassurance = (By.LINK_TEXT, "Quality Assurance Services")
    forwardbutton = (By.XPATH,"//a[@class='lSPrev']")
    backwardbutton = (By.XPATH,"//a[@class='lSNext']")
    enterpriseapptab = (By.LINK_TEXT, "Enterprise Applications")








    def qualityassurance_link(self):
        return self.driver.find_element(*ServicesPage.qualityassurance)

    def forwardbutton_action(self):
        return self.driver.find_element(*ServicesPage.forwardbutton)

    def backwardbutton_action(self):
        return self.driver.find_element(*ServicesPage.backwardbutton)

    def enterprise_actiontab(self):
        return self.driver.find_element(*ServicesPage.enterpriseapptab)

