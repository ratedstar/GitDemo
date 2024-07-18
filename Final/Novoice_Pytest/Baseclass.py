import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        # for the object to know in which file it has to print add handler
        # In add handler we need to pass file handler object as parameter
        # Basically add handler will take which file n what format
        # file handler will give file location
        fileHandler = logging.FileHandler("Test.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger