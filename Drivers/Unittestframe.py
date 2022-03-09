import unittest
from selenium import webdriver

driverpath="E:\KRN Files\Python\Selenium\Youtube\Browser Driver\chromedriver.exe"
class kk(unittest.TestCase):



    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path=driverpath)
        cls.driver.maximize_window()



    def test_hj(self):
        self.driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
        kk=self.driver.current_url
        print(kk)

    def test_hj1(self):
        self.driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
        self.driver.find_element_by_xpath("//*[@id='sloginid']").send_keys("cdolman")

        self.driver.find_element_by_xpath("//*[@id='spassword']").send_keys("Admin@123")
        self.driver.find_element_by_xpath("//*[text()='Login']").click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()




if __name__=="__main__":
    unittest.main()




