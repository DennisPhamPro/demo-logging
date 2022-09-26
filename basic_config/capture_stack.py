import logging as lg

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    lg.error("Exception occurred", exc_info=True) #set exc_info to True make log show about an error 
    lg.exception("Exception occurred") # lg.exception("Exception occurred") == lg.error(exc_info=True)