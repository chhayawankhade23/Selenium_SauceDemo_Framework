import logging
from pathlib import Path

class Loggen:

        @staticmethod
        def loggen():
            Path("Logs").mkdir(exist_ok=True)
            logger=logging.getLogger("My framework")
            logger.setLevel(logging.INFO)
            if not logger.handlers:
                file_handler= logging.FileHandler("C:\\Users\\chhay\\PycharmProjects\\Selenium_Framework_SauceDemo\\Logs\\automation.log")
                formatter=logging.Formatter(" %(asctime)s:%(levelname)s:%(message)s",datefmt="%m/%d/%Y %I:%M:%S %p")
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
                logger.info("This will be logged")
            return logger
