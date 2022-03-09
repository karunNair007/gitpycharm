
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="../chromedriver.exe")

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.maximize_window()
driver.implicitly_wait(1)


draggable = driver.find_element_by_id("draggable")
droppable = driver.find_element_by_id("droppable")


ActionChains(driver).drag_and_drop(draggable,droppable).perform()


