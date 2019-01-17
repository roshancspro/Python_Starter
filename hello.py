import re
msg ="Hello World"
print(msg)

def maskify(cc):
    hashStr = ''+cc[:-4]
    hashStr = hashStr.replace('\d','#')


