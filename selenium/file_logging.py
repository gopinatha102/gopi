#import logging
#logging.basicConfig(filename="C://Users\PAVAN KUMARA//PycharmProjects//selenium\driver//IEDriverServer_x64_3.150.1//test.log", format='%(asctime)s: %(levelname)s: %(message)s',
#datefmt='%m/%d/%Y %I:%M:%S %p')


#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)

#logger.debug("this is debug message")
#logger.info("This is info message")
#logger.warning("this is warning message")
#logger.error("this is error message")
#logger.critical("this is critical message")

from test_Login import *

class test_01:
    #logger=LogGen.loggen()
    def homepage(self):
        logger = LogGen.loggen()
        self.logger.info("********************HI home page*****************")

