import json
import re

f = open('data/search_log_10000.txt', 'r')

i = 0
for line in f:
    a = json.loads(line)
    print('get line of ' + str(len(a)) + ' elements.')
    if len(a) > 0:
        print('-> 1st element is: timestamp = ' + str(a[0]['ts']) + '; address = ' + a[0]['url'])
        print(a[0]['ts'])
    else:
        print('-> Nothing to show')
    i += 1
    if i > 2:
        break