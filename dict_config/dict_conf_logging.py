import logging
from logging import config

log_config = {
    "version":1,
    "root":{
        "handlers":["console"],
        "level":"DEBUG"
    },
    "handlers":{
        "console":{
            "formatter":"std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        }
    },
    "formatters":{
        "std_out":{
            "format":"%(asctime)s-%(levelname)s-%(lineno)s >>> %(message)s",
            "datefmt":"%d-%m-%Y %H:%M:%S"
        }
    },
}

# %(message)s is important
config.dictConfig(log_config) #Initiate the config

def addition(a, b):
    logging.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logging.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logging.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    try:
        result = float(a) + float(b)
        logging.info("Addition Function Completed Successfully")
        return result
    except Exception as e:
        logging.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
        return None


if __name__ == "__main__":
    #logging.info("Current Log Level : {}\n".format(logging.getLevel()))

    result = addition(10,20)
    logging.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition("20",20)
    logging.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition("A",20)
    logging.info("Addition of {} & {} is : {}".format("A",20, result))