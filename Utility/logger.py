import os
import logging
class Loggen:

        @staticmethod
        def loggen():

            logger=logging.getLogger("My framework")
            logger.setLevel(logging.INFO)
            if not logger.handlers:
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                LOG_DIR = os.path.join(BASE_DIR, "Logs")
                os.makedirs(LOG_DIR, exist_ok=True)
                LOG_FILE = os.path.join(LOG_DIR, "automation.log")

                file_handler = logging.FileHandler(LOG_FILE)

                formatter=logging.Formatter(" %(asctime)s:%(levelname)s:%(message)s",datefmt="%m/%d/%Y %I:%M:%S %p")
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

            return logger

