import string
import math


t = (0, 4, 132.42222, 10000, 12345.67)
print("day_0{}, ex0{} : {}, {}, {}".format(t[0], t[1], round(t[2], 2), "%.2e" % t[3], "%.2e" % t[4]))
