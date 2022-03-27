import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    path = "C:\\Users\\DELL\\PycharmProjects\\pythonProject2\\Log Files\\logfile.log"

    filehandler = logging.FileHandler(path)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)

    logger.debug("A debug statement is executed")
    logger.info("Information Statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")
