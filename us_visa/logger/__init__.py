import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m-%d-%Y-%H:%M:%S')}.log"

logs_path=os.path.join(from_root(),'logs',LOG_FILE)

os.makedirs('logs',exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format='[%(asctime)s] %(name)s - %(levelname)s %(message)s',
    level=logging.DEBUG,
)