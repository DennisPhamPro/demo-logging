import logging 
logging.basicConfig(filename='Phat_conf.log',format= '%(asctime)s : %(levelname)s :\
 %(lineno)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
