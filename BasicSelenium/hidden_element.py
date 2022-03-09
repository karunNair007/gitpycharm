import time
import pytest
from POM1 import Global

@pytest.mark.hidden_elements
def test_hidden():
    x = Global("chrome")
    x.login("login credentials", "link", "un", "pswd", "locator", "unxpath", "pswdxpath", "loginxpath")
    x.open_screen("locator", "batchmenuxpath", "batchcreationscreenxpath")
    x.config_click("locator","batch_creation_add_button_xpath")
    x.config_click("locator", "batch_creation_add_popup_ProductCategory_Dropdown")
    # x.sendxpath("//*[@class='react-select__input']//*[@id='nproductcatcode']","Albumins")
    x.scrolled_down_locate_element("(//*[text()='Vaccines - Other'])[1]")
    x.scroll_up("//*[@name='smanufsitename']")
    time.sleep(3)



