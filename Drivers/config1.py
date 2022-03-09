from configparser import ConfigParser


def confg2(section,key1,key2):
    config = ConfigParser()
    config.read("C:\\Users\\Karun\\PycharmProjects\\Sel;enium with Python\\Drivers\\configuration.ini")
    k1=config.get(section, key1)
    k2 = config.get(section, key2)
    kk = []
    kk.insert(0, k1)
    kk.insert(1, k2)
    return kk


print(confg2("login credentials","un","pswd"))