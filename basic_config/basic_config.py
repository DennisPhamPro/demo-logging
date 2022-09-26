import logging as lg

# lg.basicConfig(level=lg.DEBUG); """set level of log messages to Debug level
#         (enable all logging calls at or above that level to be logged)"""
# lg.debug("This will get logged")
# lg.info("This info will get logged too")

lg.basicConfig(filename="basic.log", filemode="w", format="%(message)s  --- %(name)s --- %(levelname)s"); """This will create a log file
        and edit message format"""
lg.warning("This will create a log contain file")