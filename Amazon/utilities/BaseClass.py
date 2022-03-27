import logging
import inspect
import pytest

@pytest.mark.usefixtures("setup")
class Baseclass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        path = "C:\\Users\\DELL\\PycharmProjects\\pythonProject2\\Log Files\\logfile.log"

        filehandler = logging.FileHandler(path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)

        return logger


