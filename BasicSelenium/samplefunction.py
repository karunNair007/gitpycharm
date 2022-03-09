import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC







def d(driver,link):
    driver.get(link)



def kk(link, loc1, sendvalue):
    d().driver.get(link)
    WebDriverWait(d().driver, 10).until(EC.presence_of_element_located((By.XPATH, loc1)))
    d().driver.find_element_by_xpath(loc1).send_keys(sendvalue)
    print("ll")

#def get(link):
    #driver.get(link)





#def sendkeys(loc, sendvalue):
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, loc)))
    #driver.find_element_by_xpath(loc).send_keys(sendvalue)



#def click1(loc):
    #time.sleep(3)
    #jj = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, loc)))
    #jj.click()


#def scroll(loc2):
    #kk = driver.find_element_by_xpath(loc2)
    #objectaxis = kk.location_once_scrolled_into_view
    #print(objectaxis)
    #kk.click()


#def radiobutton(loc3):
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, loc3)))
    #FTPresult = driver.find_element_by_xpath(loc3).is_selected()
    #print(FTPresult)




