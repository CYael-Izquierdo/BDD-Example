from enum import Enum
import os


class Constants:
    BASE_URL = 'http://192.168.64.2'
    CHROMEDRIVER_PATH = os.path.abspath('chromedriver')


class DriverName(Enum):
    chrome = 1
    firefox = 2
