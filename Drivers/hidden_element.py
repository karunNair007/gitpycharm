import time

from POM1 import Global


x=Global("chrome")
x.login()
x.global_screen_open("//*[text()='Batch']","//*[text()='Batch Creation']")
x.clickxpath("//*[@data-tip='Add']")
time.sleep(6)
x.clickxpath("(//*[@aria-hidden='true'])[15]")
# x.sendxpath("//*[@class='react-select__input']//*[@id='nproductcatcode']","Albumins")
x.scrolled_dowm("(//*[text()='Vaccines - Other'])[1]")

