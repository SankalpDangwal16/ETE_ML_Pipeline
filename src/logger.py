import logging
import os
from datetime import datetime

# Create log filename with UTC timestamp
LOG_FILE = f"{datetime.utcnow().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory and file path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging to both file and console
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s]",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # File handler for logs
        logging.StreamHandler()              # Stream handler for console output
    ]
)

# Example of logging in the logger.py script
if __name__ == "__main__":
    logging.info("Logging has started")
