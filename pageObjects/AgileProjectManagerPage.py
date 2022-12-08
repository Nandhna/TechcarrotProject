from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AgileProjectManagerPage:

    def __init__(self, driver):                                         #driver as an argument in constructor
        self.driver = driver

    viewalljobs = (By.LINK_TEXT, "View all jobs")
    signin = (By.XPATH, "//ul[@class='cw-candidate-login cw-Dcandidate-login']/li[1]")
    registerlink = (By.XPATH, "//ul[@class='cw-candidate-login cw-Dcandidate-login']/li[3]")
    visitwebsite = (By.LINK_TEXT, "Visit website")
    visittechcarrot = (By.LINK_TEXT, "techcarrot")


    def getviewalljobs_link(self):
        return self.driver.find_element(*AgileProjectManagerPage.viewalljobs)
    def getsignin_link(self):
        return self.driver.find_element(*AgileProjectManagerPage.signin)
    def getregisterbutton_link(self):
        return self.driver.find_element(*AgileProjectManagerPage.registerlink)
    def getvisitwebsite_link(self):
        return self.driver.find_element(*AgileProjectManagerPage.visitwebsite)
    def getvisittechcarrotwebsite_link(self):
        return self.driver.find_element(*AgileProjectManagerPage.visittechcarrot)


