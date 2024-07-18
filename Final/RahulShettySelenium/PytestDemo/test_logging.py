import logging

# we need to create an obj with that obj we will log getLogger will help to create logger obj
# to get test case name pass name in getLogger
def test_loggingDemo():
    logger = logging.getLogger(__name__)

    # logger should know in which file it should print what is the format should be send to add handler method
    # add handler will take file handler obj, file handler is nothing but file location
    # create a file handler obj to pass it in add handler
    # We have to set the format from logging.Formatter()
    # Now we have to create a formatter obj and pass it to fileHandler.setformatter()

    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)


    # Now we have to set level if we want see only error logs
    # if set level only that will be visible

    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Credit card balance is low")
    logger.error("Assert got failed")
    logger.critical("critical issue")
