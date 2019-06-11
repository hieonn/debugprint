# -*- coding:utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import inspect
import re
import pprint

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
        tag = "line : %s : " %(caller.lineno)
    frame = inspect.currentframe().f_back
    s = inspect.getframeinfo(frame).code_context[0]
    r = re.search(r"\((.*)\)", s).group(1)
    #d = ("{} : {} = {}".format(tag, r,x))
    data_type = type(x)
    if data_type is list or data_type is dict or data_type is tuple or data_type is set:
        d = ("{} : {} ->".format(tag, r))
        print d
        PrettyPrinter().pprint(x)
    else :
        d = ("{} : {} = {}".format(tag, r, x))
        print d

def dprintPretty(x) :
    PrettyPrinter().pprint(x)