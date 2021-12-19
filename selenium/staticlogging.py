from file_logging import LogGen
import os

class Test_001_Login:
    logger = LogGen.loggen()

    def test_homePageTitle():
        self.logger.info("test_homePageTitle")
        self.logger.info("verfying home page title ")
