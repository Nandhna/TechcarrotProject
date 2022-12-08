from selenium.webdriver.common.by import By



class CloudServicesPage:

    def __init__(self, driver):                                         #driver as an argument in constructor
        self.driver = driver

    cloudservicemenu = (By.LINK_TEXT, "Cloud Services")




    def cloudservicemenu_link(self):
        return self.driver.find_element(*CloudServicesPage.cloudservicemenu)