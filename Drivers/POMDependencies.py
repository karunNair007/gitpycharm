class xpathclick():
    # init nale constructor tan
    def __init__(self, driver):
        self.driver = driver

    def clickxpath(self,loc1):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(loc1).click()

    def sendxpath(self,loc2,send):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(loc2).send_keys(send)






