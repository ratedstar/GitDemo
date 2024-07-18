import logging

def test_Logging():
    logger = logging.getLogger(__name__)

    # for the object to know in which file it has to print add handler
    # In add handler we need to pass file handler object as parameter
    # Basically add handler will take which file n what format
    # file handler will give file location
    fileHandler = logging.FileHandler("Test.log")
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    logger.debug("This message is for debug")
    logger.info("This is for info")
    logger.warning("This is for warnings")
    logger.error("This is for error")
    logger.critical("This is for critical")