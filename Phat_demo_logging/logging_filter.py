import logging
from logging import config
import datetime

class InfoAnWarningsOnly(logging.Filter):
    def filter(self, record):
        if record.levelno >10 and record.levelno < 31:
            return True
        else:
            return False

log_config = {
    "version":1,
    "root":{
        "handlers":["console","file"],
        "level":"DEBUG"
    },
    "handlers":{
            "console":{
                "formatter":"std_out",
                "class": "logging.StreamHandler",
                "level": "DEBUG"
            },
        "file":{
            "formatter":"std_out",
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename" : '[PHAT]'+datetime.datetime.now().strftime('%Y_%m_%d_%H:%M:%S%p.log')
            },
    },
    "formatters":{
        "std_out":{
            "format":"%(asctime)s : %(levelname)s : %(lineno)s >>> %(message)s",
            "datefmt":"%d-%m-%Y %H:%M:%S %p"
        }
    },
    "filters":{
        "info_&_warning":{
            "()" : InfoAnWarningsOnly
        }
    }
}

config.dictConfig(log_config) 

logging.debug("This is debug")
logging.info("This is info")
logging.warning("ALARM!!!")

