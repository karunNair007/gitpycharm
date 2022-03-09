from POM1 import Global
from configparser import ConfigParser

kk=Global("chrome")
kk.login("login credentials","link","un","pswd","locator","unxpath","pswdxpath","loginxpath")
kk.open_screen("locator","batchmenuxpath","batchcreationscreenxpath")