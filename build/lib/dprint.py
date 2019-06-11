# -*- coding:utf8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import inspect
import re
import pandas as pd

def dprint(x, tag='unknown'):
    pd.options.display.max_columns = None
    pd.set_option('display.width', 1000)
    if tag == 'unknown' :
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        tag = "line : %s : " %(caller.lineno)
    frame = inspect.currentframe().f_back
    s = inspect.getframeinfo(frame).code_context[0]
    r = re.search(r"\((.*)\)", s).group(1)
    print("{} : {} = \n{}".format(tag, r,x))