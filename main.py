import json
import re

LINES_TO_READ = 100

f = open('data/search_log_10000.txt', 'r')

i = 0
for line in f:
    a = json.loads(line)
    print(str(i+1)+'get line of ' + str(len(a)) + ' elements.')
    if len(a) > 0:
        print("    1st element is: timestamp = " + str(a[0]['ts']) + '; address = ' + a[0]['url'])
        match = re.match(r".*(yandex|google)(.*\.tr).*", a[0]['url'])
        if match:
            print('    in the beginning was... ' + str(match.group(1)) + " in domen " + str(match.group(2)))
        else:
            print('    Site isn\'t recognized.  ')
    else:
        print('    Nothing to show')
    i += 1
    if i > LINES_TO_READ:
        break