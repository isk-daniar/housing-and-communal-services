import queue
import time
import datetime
from datetime import datetime
import threading
import random
from random import randrange

kw_hour = 0

def electrometer():
    global kw_hour
    kw_hour = 1 * random.uniform(15, 30)
    return kw_hour

def asd():
    print(kw_hour)
    t = threading.Timer(1, electrometer).start()
