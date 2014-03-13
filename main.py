import json
import re

f = open('data/search_log_10000.txt', 'r', encoding='utf-8')
f1 = open('data/res_cut.txt', 'w', encoding='utf-8')
log = open('data/log_initial.txt', 'w', encoding='utf-8')

i = 0
count_yandex = [0 for line_ya in f]
f = open('data/search_log_10000.txt', 'r')
count_google = [0 for line_go in f]
f = open('data/search_log_10000.txt', 'r')
#main part
for line in f:
    a = json.loads(line)
    print(str(i+1)+': get line of ' + str(len(a)) + ' elements.', file=log)
    if len(a) > 0:
        print("    1-st element is: timestamp = " + str(a[0]['ts']) + '; address = ' + a[0]['url'], file=log)
        match = re.match(r".*(yandex|google)\.com\.tr.*", a[0]['url'])
        if match:
            print('    in the beginning was... ' + str(match.group(1)), file=log)
        else:
            print('    Site isn\'t recognized.  ', file=log)
        j = 0
        for a_i in a:
            match = re.match(r".*(yandex|google)\.com\.tr.*", a_i['url'])
            a[j]['url'] = str(match.group(1))
            if match:
                if str(match.group(1)) == 'yandex':
                    count_yandex[i] += 1
                else:
                    count_google[i] += 1
            j +=1
        print('Yandex: '+str(100*count_yandex[i]/len(a))+'%  Google: '+ str(100*count_google[i]/len(a))+'% All: ' + str(100*(count_yandex[i]+count_google[i])/len(a))+'%', file=log)
        if count_google[i] != len(a):
            print(json.dumps(a), file=f1)
    else:
        print("    Nothing to show", file=log)
    i += 1