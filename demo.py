from us_visa.logger import logging
from us_visa.exceptions import USvisaException
import sys

#logging.info("Hey Bhagii, your first custom log ")

try:
    "2"+2
except Exception as e:
    raise USvisaException(e,sys)