from enum import Enum
import os


class Constants:
    BASE_URL = 'http://192.168.64.2'
    CHROMEDRIVER_PATH = os.path.abspath('chromedriver')
    TL_DEV_KEY = '5d542da97633d8c98afe20464202a7b7'
    TL_URL = 'http://192.168.64.3/lib/api/xmlrpc/v1/xmlrpc.php'


class DriverName(Enum):
    chrome = 1
    firefox = 2
