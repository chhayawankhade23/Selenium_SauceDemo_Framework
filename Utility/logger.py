
import logging
from pathlib import Path
class Loggen:

        @staticmethod
        def loggen():
            Path("Logs").mkdir(exist_ok=True)
            logger=logging.getLogger("My framework")
            logger.setLevel(logging.INFO)
            if not logger.handlers:
                file_handler= logging.FileHandler("C:\\Users\\chhay\\PycharmProjects\\Selenium_SauceDemo_Framework\\Logs\\automation.log")
                formatter=logging.Formatter(" %(asctime)s:%(levelname)s:%(message)s",datefmt="%m/%d/%Y %I:%M:%S %p")
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
                logger.info("This will be logged")
            return logger
# import logging
# from pathlib import Path
# from datetime import datetime
#
#
# class Loggen:
#
#     @staticmethod
#     def loggen():
#
#         log_dir = Path.cwd() / "Logs"
#         log_dir.mkdir(exist_ok=True)
#         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         log_file = log_dir / f"automation_{timestamp}.log"
#
#         logger = logging.getLogger("My framework")
#         logger.setLevel(logging.INFO)
#
#         if not logger.handlers:
#             file_handler = logging.FileHandler(log_file)
#
#             formatter = logging.Formatter(
#                 "%(asctime)s : %(levelname)s : %(message)s",
#                 datefmt="%m/%d/%Y %I:%M:%S %p"
#             )
#             file_handler.setFormatter(formatter)
#
#             logger.addHandler(file_handler)
#
#         return logger
# import logging
# from pathlib import Path
#
# class Loggen:
#
#     @staticmethod
#     def loggen():
#         # Get project root (2 levels up from this file)
#         project_root = Path(__file__).resolve().parents[2]
#
#         # Create Logs folder at root level
#         logs_dir = project_root / "Logs"
#         logs_dir.mkdir(exist_ok=True)
#
#         log_file = logs_dir / "automation.log"
#
#         logger = logging.getLogger("SauceDemoFramework")
#         logger.setLevel(logging.INFO)
#
#         if not logger.handlers:
#             file_handler = logging.FileHandler(log_file)
#             formatter = logging.Formatter(
#                 "%(asctime)s : %(levelname)s : %(message)s",
#                 datefmt="%d-%m-%Y %H:%M:%S"
#             )
#             file_handler.setFormatter(formatter)
#             logger.addHandler(file_handler)
#
#         return logger
