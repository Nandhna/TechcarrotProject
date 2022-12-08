from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):                                         #driver as an argument in constructor
        self.driver = driver


    #popup = (By.XPATH, "//span[contains(text(),'DigiTrendz')]")
    digitrendzbox = (By.LINK_TEXT, "digitrendz")
    register = (By.XPATH, "//a[contains(text(),'Register')]")
    firstnameBox = (By.NAME, "Name")
    lastnameBox = (By.NAME, "last-name")
    jobtitleBox = (By.NAME, "job-title")
    orgnameBox = (By.NAME, "organization")
    industrynameDrop = (By.XPATH, "//option[contains(text(),'Finance')]")
    emailBox = (By.XPATH, "//input[@name='emailid']")
    phonenumberBox = (By.NAME, "Phoneno")
    employeenumberBox = (By.NAME, "Domain")
    rmeCheckBox = (By.XPATH, "//input[@type='checkbox']")


    infolink = (By.LINK_TEXT,"More info")

    homelink = (By.LINK_TEXT,"Home")
    viewclients = (By.LINK_TEXT,"View all clients")

    viewlocation = (By.XPATH,"//a[@class='view-location-map']")


    facebooklink = (By.XPATH,'//*[@id="facebook"]')
    linkedInlink = (By.XPATH,'//*[@id="linkedin"]')
    twitterlink =  (By.XPATH,'//*[@id="twitter"]')
    instagramlink = (By.XPATH,'//*[@id="instagram"]')




    def getRegister(self):
        return self.driver.find_element(*HomePage.register)

    def getfirstname(self):
        return self.driver.find_element(*HomePage.firstnameBox)
    def getlastname(self):
        return self.driver.find_element(*HomePage.lastnameBox)
    def getjob(self):
        return self.driver.find_element(*HomePage.jobtitleBox)
    def getorg(self):
        return self.driver.find_element(*HomePage.orgnameBox)
    def getindustrydropdown(self):
        return self.driver.find_element(*HomePage.industrynameDrop)
    def getemail(self):
        return self.driver.find_element(*HomePage.emailBox)
    def getphonenumber(self):
        return self.driver.find_element(*HomePage.phonenumberBox)
    def getemployeenumber(self):
        return self.driver.find_element(*HomePage.employeenumberBox)
    def rme_checkbox(self):
        return self.driver.find_element(*HomePage.rmeCheckBox)



    def moreinfo_link(self):
        return self.driver.find_element(*HomePage.infolink)

    def home_link(self):
        return self.driver.find_element(*HomePage.homelink)

    def viewclients_link(self):
        return self.driver.find_element(*HomePage.viewclients)

    def viewlocation_link(self):
        return self.driver.find_element(*HomePage.viewlocation)


    def facebookmedia_link(self):
        return self.driver.find_element(*HomePage.facebooklink)
    def linkedInmedia_link(self):
        return self.driver.find_element(*HomePage.linkedInlink)
    def twittermedia_link(self):
        return self.driver.find_element(*HomePage.twitterlink)
    def instagrammedia_link(self):
        return self.driver.find_element(*HomePage.instagramlink)



































'''      #initialization of driver happens here
    shop = (By.XPATH, "//a[contains(text(),'Shop')]")
    name = (By.CSS_SELECTOR,  "[name='name']")
    email = (By.CSS_SELECTOR,  "[name='email']")
    passwrd = (By.CSS_SELECTOR, "[type='Password']")
    check = (By.ID, "exampleCheck1")
    status = (By.ID, "inlineRadio2")
    gender = (By.ID, "exampleFormControlSelect1")
    dateofbirth = (By.XPATH, "/html/body/app-root/form-comp/div/form/div[7]/input")
    # dateofbirth = (By.XPATH, "//input[@type='date']")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.XPATH, "/html/body/app-root/form-comp/div/div[2]/div")

    # Initialization of driver and fetch "shop" element

    def shop_Items(self):
         return self.driver.find_element(*HomePage.shop)            #calling class and object created    # "*" -> to understand the shop created in HomePage as tuple
         # checkOutPage = CheckOutPage(self.driver)
         # return checkOutPage

        # self.driver.find_element(By.XPATH, value="//a[contains(text(),'Shop')]").click()

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPasswrd(self):
        return self.driver.find_element(*HomePage.passwrd)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getEmpStatus(self):
        return self.driver.find_element(*HomePage.status)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getDateBirth(self):
        return self.driver.find_element(*HomePage.dateofbirth)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)'''


