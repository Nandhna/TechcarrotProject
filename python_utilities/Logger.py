import inspect
import logging

class Logger:
    def getlogger(self, filename):
        print("Inside Logger")
        loggerName = inspect.stack()[1][3]
        # The above step is to get the proper testcasename in the log,
        # if we didn't give this, in Log it will print this utility filename
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler(filename)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        return logger