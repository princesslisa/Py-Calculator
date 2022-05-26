import pprint

p = "hello world hello"
keys = set(p.split(" "))
mydict = {}
for i in keys:
    mydict[i] = p.count(i)

print(mydict)

pprint.pprint(sorted(mydict, key=lambda x: x[p]))
