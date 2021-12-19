import logging

class LogGen():
    @staticmethod
    def loggen():

        logging.basicConfig(filename=r"C://Users//PAVAN KUMARA//PycharmProjects//selenium//driver//IEDriverServer_x64_3.150.1//test6.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')



        logger=logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger

