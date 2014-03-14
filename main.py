import json

f = open('data/res_cut.txt', 'r', encoding='utf-8')
f1 = open('data/res.txt', 'w', encoding='utf-8')
log = open('data/log.txt', 'w', encoding='utf-8')

i = 0
count_yandex = [0 for line_ya in f]
f = open('data/res_cut.txt', 'r')
count_google = [0 for line_go in f]
f = open('data/res_cut.txt', 'r')
#main part
for line in f:
    a = json.loads(line)
    print(str(i+1)+': get line of ' + str(len(a)) + ' elements.', file=log)
    print("    1st element is: timestamp = " + str(a[0]['ts']) + '; address = ' + a[0]['url'], file=log)
    j = 0
    for a_i in a:
        if a[j]['url'] == 'yandex':
            count_yandex[i] += 1
        else:
            count_google[i] += 1
        j +=1
    print('Yandex: '+str(100*count_yandex[i]/len(a))+
              '%  Google: '+ str(100*count_google[i]/len(a))+
              '% All: ' + str(100*(count_yandex[i]+count_google[i])/len(a))+'%', file=log)
    i += 1