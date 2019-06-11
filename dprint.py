# -*- coding:utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import inspect
import re
import pprint

desired_width=320

try:
    import numpy as np
    np.set_printoptions(linewidth=desired_width)
    import pandas as pd
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns', 10)
except ImportError:
    pass

class PrettyPrinter(pprint.PrettyPrinter):
	def format(self, _object, context, maxlevels, level):
		if isinstance(_object, unicode):
			return "'%s'" % _object.encode('utf8'), True, False
		elif isinstance(_object, str):
			_object = unicode(_object,'utf8')
			return "'%s'" % _object.encode('utf8'), True, False
		return pprint.PrettyPrinter.format(self, _object, context, maxlevels, level)

def dprint(x, tag='unknown'):
    if tag == 'unknown' :
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        tag = "line : %s " %(caller.lineno)
    frame = inspect.currentframe().f_back
    s = inspect.getframeinfo(frame).code_context[0]
    r = re.search(r"\((.*)\)", s).group(1)
    #d = ("{} : {} = {}".format(tag, r,x))
    data_type = type(x)
    #if data_type is list or data_type is dict or data_type is tuple or data_type is set or data_type is pandas.core.series.Series :
    if not (data_type is int or data_type is float or data_type is str or data_type is tuple) :
        try :
            d = ("{} : {} -> {}".format(tag, r, type(x)))
        except :
            d = ("{} : {} -> {}".format(tag, r, 'type error : maybe pd or np'))
        print d
        PrettyPrinter().pprint(x)
    else :
        d = ("{} : {} = {} {}".format(tag, r, x, type(x)))
        print d

# def dprintPretty(x) :
#     PrettyPrinter().pprint(x)