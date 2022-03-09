import logging

def log1():
    logging.basicConfig(filename="D:/check/LogFolder1/kk.log", format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)
    k = logging.getLogger()


    return k

jj=log1()
jj.info("sjhgjsajsa")


