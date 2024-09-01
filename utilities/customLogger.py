import logging
import os
from datetime import datetime

class LogGen:
        def loggen(test_case_name):
            log_dir = "./Logs"
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            # Generate a log file name based on test case name and timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            log_file = os.path.join(log_dir, f"{test_case_name}_{timestamp}.log")

            logger = logging.getLogger()
            logger.setLevel(logging.INFO)

            # Remove existing handlers to prevent duplicate logs
            if logger.hasHandlers():
                logger.handlers.clear()

            # Create file handler and set formatter
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', '%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            return logger
