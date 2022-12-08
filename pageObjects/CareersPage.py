from selenium.webdriver.common.by import By



class CareersPage:

    def __init__(self, driver):                                         #driver as an argument in constructor
        self.driver = driver


    careerstab = (By.LINK_TEXT, "Careers")
    viewopeningstab = (By.LINK_TEXT,"View Openings")
    jobstab = (By.XPATH,"//a[contains(text(),'Jobs')]")
    countrycheckbox = (By.XPATH, "//span[@id='lyte-checkbox-label-2']")
    inputwhatbox = (By.XPATH, "//input[@placeholder='Job title or skill']")
    inputwherebox = (By.XPATH,"//input[@placeholder='City, state/province or country']")
    industrycheckbox = (By.XPATH,"//span[@id='lyte-checkbox-label-9']")
    # clearbutton = (By.LINK_TEXT, "Clear")
    jobelement = (By.LINK_TEXT,"Agile Project Manager")
    linkcopyicon = (By.ID,"share-cp-link")
    interestedbutton = (By.CSS_SELECTOR, "button")
    signIn = (By.LINK_TEXT,"Sign In")




    def careertab_link(self):
        return self.driver.find_element(*CareersPage.careerstab)
    def viewopening_link(self):
        return self.driver.find_element(*CareersPage.viewopeningstab)
    def jobstab_link(self):
        return self.driver.find_element(*CareersPage.jobstab)
    def countrycheckbox_box(self):
        return self.driver.find_element(*CareersPage.countrycheckbox)
    def inputwhatbox_box(self):
        return self.driver.find_element(*CareersPage.inputwhatbox)
    def inputwherebox_box(self):
        return self.driver.find_element(*CareersPage.inputwherebox)
    def inputindustry_box(self):
        return self.driver.find_element(*CareersPage.industrycheckbox)
    # def clearbutton_link(self):
    #     return self.driver.find_element(*CareersPage.clearbutton)
    def jobelement_link(self):
        return self.driver.find_element(*CareersPage.jobelement)
    def linkcopyicon_button(self):
        return self.driver.find_element(*CareersPage.linkcopyicon)
    def interestedbutton_link(self):
        return self.driver.find_element(*CareersPage.interestedbutton)
    def signIn_link(self):
        return self.driver.find_element(*CareersPage.signIn)







