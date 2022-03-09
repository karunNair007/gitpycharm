from POM1 import Global

a=Global("chrome")

a.get("https://www.google.co.in/webhp?tab=rw")
a.sendxpath("(//*[@class='sub-menu'])[1]//*[text()='Selenium']","Selenium")