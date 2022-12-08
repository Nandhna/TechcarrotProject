import pytest
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.AgileProjectManagerPage import AgileProjectManagerPage
from pageObjects.ApplicationformPage import ApplicationformPage
from pageObjects.HomePage import HomePage
from pageObjects.ServicesPage import ServicesPage
from python_utilities.Logger import Logger
from python_utilities.readData import readData
from tests.conftest import driver
import pyperclip


@pytest.mark.usefixtures("setup")
class Testtech:

    #
    def test_title(self):
        log = Logger.getlogger(self,"../logs/logfile.log")
        log.info(self.driver.title)
        title = self.driver.title
        assert title== "techcarrot - Digital, Information Technology, Business Solutions"

    def test_homePage(self):

        #log = self.getLogger()
        #homePage = HomePage(self.driver)
        wait = WebDriverWait(self.driver, 100)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class = 'x']")))
        time.sleep(5)




#popup
        success_alert1 = self.driver.find_element(By.XPATH, value="(//span[contains(text(),'tech')])[1]").text
        assert "tech" in success_alert1
        print(success_alert1)
        time.sleep(5)





#scroll popup
        bar = self.driver.find_element(By.XPATH,value="//div[@class='popupinner']")
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', bar)
        time.sleep(5)

        self.driver.find_element(By.XPATH, value="//div[@class = 'x']").click()
        time.sleep(5)

    @pytest.mark.skip
    def test_digitrendz(self):

        self.driver.find_element(By.XPATH, value="/html/body/div[1]/a/img").click()

        log = Logger.getlogger(self, "../logs/logfile.log")
        log.info(self.driver.title)
        title = self.driver.title
        assert title == "DigiTrendz HCL DX - techcarrot"




    @pytest.mark.skip
    def test_registerpage(self):

        # Register  button
        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Register')]").click()
        time.sleep(2)
        data_obj = readData()
        data = data_obj.getData("..\\test_data\\test_registerdata.xlsx", 1)
        print(type(data))

        homepage_obj = HomePage(self.driver)
        print("Inside test_homePage")


        firstname_elt = homepage_obj.getfirstname()
        firstname_elt.send_keys(data["FirstName"])
        lastname_elt = homepage_obj.getlastname()
        lastname_elt.send_keys(data["LastName"])
        jobtitle_elt = homepage_obj.getjob()
        jobtitle_elt.send_keys(data["JobTitle"])
        orgname_elt = homepage_obj.getorg()
        orgname_elt.send_keys(data["Organisation"])
        dropdown_obj = HomePage(driver)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//option[contains(text(),'Finance')]").click()
        #drpdwn_elt = dropdown_obj.getindustrydropdown()
        #drpdwn_elt.select_by_visible_text("Finance")
        emailid_elt = homepage_obj.getemail()
        emailid_elt.send_keys(data["EmailID"])
        phonenumber_elt = homepage_obj.getphonenumber()
        phonenumber_elt.send_keys(data["Phone Number"])
        time.sleep(2)

        #bar2 = self.driver.find_element(By.XPATH, value="//div[@class='popupinner']")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

        employeenumber_elt = homepage_obj.getemployeenumber()
        employeenumber_elt.send_keys(data["Employee Number"])
        checkbox_elt = homepage_obj.rme_checkbox()
        checkbox_elt.click()
        time.sleep(2)

    @pytest.mark.skip
    def test_homepageelmnts(self):

# Moving back to previous webpage

        self.driver.execute_script("window.history.go(-1)")
        #print("Current Page title after back: " + driver.title)
        time.sleep(2)

        self.driver.find_element(By.XPATH, value="//div[@class = 'x']").click()
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT,value="More info").click()

#get url of the "more info"
    @pytest.mark.skip
    def test_moreinfoelmnts(self):

        get_url1 = self.driver.current_url
        print("The current url is:" + str(get_url1))
        time.sleep(5)

#Moving back to homepage from the navigated page
    @pytest.mark.skip
    def test_viewallclientselmnt(self):

        self.driver.find_element(By.LINK_TEXT, value="Home").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, value="//div[@class = 'x']").click()
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0, 1800);")
        time.sleep(5)

        self.driver.find_element(By.LINK_TEXT, value="View all clients").click()

#count images in the View all clients page
    @pytest.mark.skip
    def test_clientscount(self):

        all_images = self.driver.execute_script("return document.getElementsByTagName('img')")
        for image in range(0, len(all_images)):
            print(self.driver.execute_script("return document.getElementsByTagName('img')[{}].src".format(image)))
            time.sleep(5)

    @pytest.mark.skip
    def test_locationmap(self):
        #timebeing
        # self.driver.execute_script("window.scrollBy(0, 1800);")
        # time.sleep(5)
        # self.driver.find_element(By.LINK_TEXT, value="View all clients").click()

        # To move bottom of the page
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)

        self.driver.find_element(By.XPATH, value="//a[@id='cookie_action_close_header']").click()
        time.sleep(3)


        #explicitwait
        wait = WebDriverWait(self.driver, 100)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@class='view-location-map']")))

        time.sleep(2)
        elm = self.driver.find_element(By.CLASS_NAME, "view-location-map")
        self.driver.execute_script("arguments[0].click();", elm)
        time.sleep(5)


        log = Logger.getlogger(self, "../logs/logfile.log")
        log.info(self.driver.title)
        title = self.driver.title
        assert title == "Clients - techcarrot"
        print(title)

#To close the current tab (child window)

        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        self.driver.close()
        self.driver.switch_to.window(parent)

        time.sleep(2)

#To print all header level tabs

    @pytest.mark.skip
    def test_headertabs(self):

        success_alert3 = self.driver.find_element(By.LINK_TEXT, value="Home").text
        assert "Home" in success_alert3
        print(success_alert3)

        success_alert4 = self.driver.find_element(By.LINK_TEXT, value="Services").text
        assert "Services" in success_alert4
        print(success_alert4)

        success_alert5 = self.driver.find_element(By.LINK_TEXT, value="About Us").text
        assert "About Us" in success_alert5
        print(success_alert5)

        success_alert6 = self.driver.find_element(By.LINK_TEXT, value="Digitrendz").text
        assert "Digitrendz" in success_alert6
        print(success_alert6)

        success_alert7 = self.driver.find_element(By.LINK_TEXT, value="Careers").text
        assert "Careers" in success_alert7
        print(success_alert7)

        success_alert8 = self.driver.find_element(By.LINK_TEXT, value="Blogs").text
        assert "Blogs" in success_alert8
        print(success_alert8)

        success_alert9 = self.driver.find_element(By.LINK_TEXT, value="Contact Us").text
        assert "Contact Us" in success_alert9
        print(success_alert9)

#Social media icons
    @pytest.mark.skip
    def test_socialmedia(self):

        self.driver.find_element(By.XPATH, value='//*[@id="facebook"]').click()
        time.sleep(3)
        get_url2 = self.driver.current_url
        print("The current url is:" + str(get_url2))
        time.sleep(3)
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        self.driver.close()
        time.sleep(5)
        self.driver.switch_to.window(parent)

        self.driver.find_element(By.XPATH, value='//*[@id="linkedin"]').click()
        time.sleep(3)
        get_url3 = self.driver.current_url
        print("The current url is:" + str(get_url3))
        time.sleep(2)
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent)


        self.driver.find_element(By.XPATH, value='//*[@id="twitter"]').click()
        time.sleep(3)
        get_url4 = self.driver.current_url
        print("The current url is:" + str(get_url4))
        time.sleep(2)
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent)

        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="instagram"]').click()
        time.sleep(3)
        get_url5 = self.driver.current_url
        print("The current url is:" + str(get_url5))
        time.sleep(2)
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(parent)


#Services section
    @pytest.mark.skip
    def test_servicePage(self):

        services_obj = ServicesPage(self.driver)
        print("Inside test_servicePage")

 #mouse hover action
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.LINK_TEXT,value="Services")
        a.move_to_element(m).perform()

        self.driver.find_element(By.LINK_TEXT,value="Quality Assurance Services").click()

    @pytest.mark.skip
    def test_movingactions(self):

        self.driver.find_element(By.XPATH, value="//a[@class='lSPrev']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value="//a[@class='lSNext']").click()
        time.sleep(3)

    @pytest.mark.skip
    def test_enterpriseapplications(self):
        self.driver.find_element(By.LINK_TEXT, "Enterprise Applications").click()
        log = Logger.getlogger(self, "../logs/logfile.log")
        log.info(self.driver.title)
        title = self.driver.title
        assert title == "Enterprise Application Service in Dubai | Techcarrot"
        print(title)

#CloudServices section

    def test_cloudservicePage(self):

        services_obj = ServicesPage(self.driver)
        print("Inside test_cloudservicePage")

        # mouse hover action
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.LINK_TEXT, value="Services")
        a.move_to_element(m).perform()

        self.driver.find_element(By.LINK_TEXT, value="Cloud Services").click()
        log = Logger.getlogger(self, "../logs/logfile.log")
        log.info(self.driver.title)
        title = self.driver.title
        assert title == "Cloud Service Providers in UAE | Cloud Computing Service In Dubai"
        print(title)

#assert highlightened tab
        element=self.driver.find_element(By.LINK_TEXT, value="Value-Added Services")
        class_name = element.get_attribute('class')
        assert class_name == "active-slide"

#assert not highlighted tab

        element_name = self.driver.find_element(By.LINK_TEXT, value="Enterprise Applications")
        class_name = element_name.get_attribute('class')
        assert class_name != "active-slide"


#Careers section

    def test_careersPage(self):
        self.driver.find_element(By.LINK_TEXT, value="Careers").click()
        get_careerurl = self.driver.current_url
        print("The current url is:" + str(get_careerurl))
        time.sleep(3)

        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(4)

    def test_viewopeningsPage(self):

        self.driver.find_element(By.LINK_TEXT, value="View Openings").click()

        log = Logger.getlogger(self, "../logs/logfile.log")
        log.info(self.driver.title)
        title = self.driver.title
        assert title == "Careers - techcarrot"
        print(title)
        time.sleep(5)

        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        time.sleep(2)

    def test_jobsPage(self):

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Jobs')]").click()
        time.sleep(5)

    def test_countryName(self):

        self.driver.find_element(By.XPATH, value="//span[@id='lyte-checkbox-label-2']").click()
        time.sleep(5)

        filter_countryjobcount = self.driver.find_elements(By.CLASS_NAME,"cw-filter-joblist")
        print(len(filter_countryjobcount))

    def test_jobsearchElemnt(self):

        input_job=self.driver.find_element(By.XPATH, value="//input[@placeholder='Job title or skill']")
        input_job.send_keys("Agile")
        time.sleep(5)
        input_job.send_keys(Keys.ENTER)
        time.sleep(2)

    def test_countrysearchElmnt(self):

        input_place = self.driver.find_element(By.XPATH, value="//input[@placeholder='City, state/province or country']")
        input_place.send_keys("United Arab Emirates")
        time.sleep(5)
        input_place.send_keys(Keys.ENTER)
        time.sleep(2)

    def test_industrysearchElmnt(self):

        # input_industry = self.driver.find_element(By.CLASS_NAME, value="cw-left-fillter-search")
        # input_industry.send_keys("Retail & Wholesale")
        # time.sleep(5)
        # input_industry.send_keys(Keys.ENTER)
        # time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[@id='lyte-checkbox-label-8']").click()
        time.sleep(2)

        filter_jobcount = self.driver.find_elements(By.CLASS_NAME, "cw-filter-joblist")
        print(len(filter_jobcount))

    # def test_clearElmnt(self):
    #
    #     self.driver.find_element(By.LINK_TEXT, value="Clear").click()
    #     time.sleep(5)

    def test_jobElmnt(self):

        self.driver.find_element(By.LINK_TEXT, value="Project Manager - Agile").click()
        time.sleep(5)

        element_header = self.driver.find_element(By.TAG_NAME, value="h1")
        assert element_header.text == 'Project Manager - Agile'

    def test_linkcopyElmnt(self):

        self.driver.find_element(By.ID, value="share-cp-link").click()
        time.sleep(5)

        self.driver.execute_script('window.open(' ');')
        new_window = self.driver.window_handles[2]
        self.driver.switch_to.window(new_window)
        self.driver.get(pyperclip.paste())

        time.sleep(5)
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER)
        time.sleep(2)
        old_window = self.driver.window_handles[0]
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(2)

        old_windowElement = self.driver.find_element(By.TAG_NAME, value="h1")
        new_windowElement = self.driver.find_element(By.TAG_NAME, value="h1")
        assert old_windowElement.text == new_windowElement.text
        time.sleep(2)
        self.driver.close()
        time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)


    def test_interestedbutton(self):

        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        interested_buttons = self.driver.find_elements(By.TAG_NAME, value="button")
        self.driver.execute_script("arguments[0].click();", interested_buttons[1])
        time.sleep(5)


    def easyapplybutton(self):

        apply_button = self.driver.find_element(By.XPATH, "//input[@class='cw-btn-primary cnl-smart-bg']")
        self.driver.execute_script("arguments[0].click();", apply_button)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(2)

        get_careerurl = self.driver.current_url
        print("The current url is:" + str(get_careerurl))
        time.sleep(3)

        self.driver.close()

        self.driver.switch_to.window(self.driver.window_handles[1])

    @pytest.mark.skip
    def test_applicationform(self):

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)

        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(4)

        data_obj = readData()
        data = data_obj.getData("..\\test_data\\test_applicationdata.xlsx", 1)
        print(type(data))

        applicationform_obj = ApplicationformPage(self.driver)
        print("Inside test_ApplicationPage")

        # lastname_elmt = applicationform_obj.getlast_name()
        # lastname_elmt.send_keys(data["Last Name"])

        lastname_elmt = applicationform_obj.getlast_name()
        lastname_elmt.send_keys(data["Last Name"])

        firstname_drpdwn = self.driver.find_element(By.XPATH, "//span[contains(text(),'-None-')]")
        firstname_drpdwn.click()
        self.driver.find_element(By.XPATH, "//lyte-drop-item[@id='Lyte_Drop_Item_2']").click()

        firstname_elmt = applicationform_obj.getfirst_name()
        firstname_elmt.send_keys(data["First Name"])

        email_elmt = applicationform_obj.getemail_name()
        email_elmt.send_keys(data["Email"])

        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(4)

        mobile_numberelmnt = applicationform_obj.getmobile_num()
        mobile_numberelmnt.send_keys(data["Mobile Number"])

        zip_postalelmnt = applicationform_obj.getzipostal_tab()
        zip_postalelmnt.send_keys(data["Zip Postal"])

        state_elmnt = applicationform_obj.getstate_tab()
        state_elmnt.send_keys(data["State"])
        time.sleep(2)

    @pytest.mark.skip
    def test_clearbutton(self):

        self.driver.find_element(By.LINK_TEXT, value ="Clear").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    @pytest.mark.skip
    def test_reloadicon(self):

        self.driver.find_element(By.LINK_TEXT, value="Reload").click()
        time.sleep(5)

#submit Application
    @pytest.mark.skip
    def test_submitapplication(self):

        # Submit_button = self.driver.find_element(By.CLASS_NAME, value="lyte-button lyteBackgroundColorBtn")
        # self.driver.execute_script("arguments[0].click();", Submit_button)
        # time.sleep(5)
        self.driver.find_element(By.XPATH, value="//lyte-button[@id='cw-submit-btn']//button[@id='']").click()
        time.sleep(2)

    @pytest.mark.skip
    def test_scrollbutton(self):
        self.driver.find_element(By.ID, "back-top").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)


 #cancel button
    @pytest.mark.skip
    def test_deletebutton(self):
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        time.sleep(2)

    @pytest.mark.skip
    def test_projectmanager(self):

        manager_obj = AgileProjectManagerPage(self.driver)
        print("Inside test_projectmanager")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    # mobile_numberelmnt = applicationform_obj.getmobile_num()
    # mobile_numberelmnt.send_keys(data["Mobile Number"])
        viewjobselmnt = manager_obj.getviewalljobs_link()
        viewjobselmnt.click()
        time.sleep(3)
        get_careerurl = self.driver.current_url
        print("The current url is:" + str(get_careerurl))
        time.sleep(3)

    @pytest.mark.skip
    def test_signinlink(self):

        # self.driver.find_element(By.XPATH, value="//ul[@class='cw-candidate-login cw-Dcandidate-login']/li[1]").click()
        manager_obj = AgileProjectManagerPage(self.driver)
        signinlinkelmnt = manager_obj.getsignin_link()
        signinlinkelmnt.click()

        time.sleep(2)
        candidate_page = self.driver.window_handles[2]
        job_page = self.driver.window_handles[1]
        self.driver.switch_to.window(candidate_page)
        time.sleep(2)

        candidatepage_header =  self.driver.find_element(By.TAG_NAME, value="h1").text
        print(candidatepage_header)
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)

    @pytest.mark.skip
    def test_registerlink(self):

        manager_obj = AgileProjectManagerPage(self.driver)
# Moving back to previous webpage


        reglinkelmnt = manager_obj.getregisterbutton_link()
        reglinkelmnt.click()
        time.sleep(2)

        get_careerurl = self.driver.current_url
        print("The current url is:" + str(get_careerurl))
        time.sleep(3)

        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.close()

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    @pytest.mark.skip
    def test_visitwebsitelink(self):

        manager_obj = AgileProjectManagerPage(self.driver)
        print("Inside test_visitwebsite")

        visitwebelmnt = manager_obj.getvisitwebsite_link()
        visitwebelmnt.click()

        job_page = self.driver.window_handles[1]
        website_page = self.driver.window_handles[2]
        self.driver.switch_to.window(self.driver.window_handles[2])

        time.sleep(2)

        get_careerurl = self.driver.current_url
        print("The current url is:" + str(get_careerurl))
        time.sleep(3)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)

    @pytest.mark.skip
    def test_techcarrotlink(self):

        manager_obj = AgileProjectManagerPage(self.driver)
        print("Inside test_visittechcarrotwebsite")

        visittechcarrotwebelmnt = manager_obj.getvisittechcarrotwebsite_link()
        visittechcarrotwebelmnt.click()

        job_page = self.driver.window_handles[1]
        techwebsite_page = self.driver.window_handles[2]
        self.driver.switch_to.window(self.driver.window_handles[2])

        time.sleep(2)

        get_careerurl = self.driver.current_url
        print("The current url is:" + str(get_careerurl))
        time.sleep(3)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)






































    # def test_signInlink(self):
    #
    #     self.driver.execute_script("return document.body.scrollHeight")
    #     self.driver.find_element(By.LINK_TEXT,value="Job listing").click()
    #     time.sleep(2)
    #     self.driver.find_element(By.LINK_TEXT, value="Sign In").click()
    #
    #     candidate_page = self.driver.window_handles[2]
    #     job_page = self.driver.window_handles[1]
    #     self.driver.switch_to.window(candidate_page)
    #     time.sleep(2)
    #
    #     candidatepage_header =  self.driver.find_element(By.TAG_NAME, value="h1").text()
    #     print(candidatepage_header.text)
    #     time.sleep(2)
    #
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     time.sleep(5)























































'''  self.driver.find_element(By.XPATH, value="//div[@class = 'x']").click()


        self.driver.find_element(By.XPATH, value="//li[@id='menu-item-311']").click()

        self.driver.find_element(By.XPATH, value="//li[@id='menu-item-311']").click()
        time.sleep(5)
        success_alert1 = self.driver.find_element(By.XPATH, value="//li[@id='menu-item-311']").text

        assert "Services" in success_alert1



    def test_sales(self):

        self.driver.find_element(By.LINK_TEXT, value="Salesforce").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, value="Quality Assurance Services").click()
        time.sleep(2)
        success_alert2 = self.driver.find_element(By.XPATH, value="//span[contains(text(),'Assurance Services')]").text

        assert "Assurance Services" in success_alert2
        print(success_alert2)

    def test_careers(self):

        self.driver.find_element(By.LINK_TEXT, value="Careers").click()
        time.sleep(5)

        success_alert3 = self.driver.find_element(By.XPATH, value="//h1/span").text
        assert "100% EMPLOYEE STRENGTH" in success_alert3
        print(success_alert3)
        time.sleep(5)

        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(5)

        self.driver.find_element(By.XPATH, value="//a[contains(text(),'View Openings')]").click()
        time.sleep(3)

        windowsOpened = self.driver.window_handles
        self.driver.switch_to.window(windowsOpened[1])

        #self.driver.find_element(By.XPATH, value="//a[contains(text(),'Start your journey with us.')]").click()


        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(5)

        self.driver.find_element(By.XPATH, value="//span[@id='lyte-checkbox-label-1']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[@id='lyte-checkbox-label-2']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, value="//span[@id='lyte-checkbox-label-0']").click()
        time.sleep(5)

        input=self.driver.find_element(By.XPATH, value="//input[@placeholder='Job title or skill']")
        input.send_keys("Agile")
        time.sleep(5)
        input.send_keys(Keys.ENTER)
        time.sleep(5)


        self.driver.find_element(By.LINK_TEXT, value="Agile Project Manager").click()
        time.sleep(5)

        self.driver.find_element(By.LINK_TEXT, value="Job listing").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, value="//a[contains(text(),'Home')]").click()
        time.sleep(5)'''




