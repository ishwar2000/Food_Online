
from datetime import datetime

def getOrderNumber(pk):
    key = datetime.now().strftime("%Y%m%d%H%M%S")
    key += str(pk)

    return key