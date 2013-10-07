import shelve

from collections import OrderedDict

d = shelve.open("shelve.db")

d['fruits'] = OrderedDict(enumerate(["Banana","Apple"]))
d['1'] = 1000;
d['list'] = range(10)

print("Keys are ",d.keys())


d.close()






