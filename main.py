import json
import matplotlib.pyplot as plt


f = open('data/res_cut.txt', 'r', encoding='utf-8')
f1 = open('data/res.txt', 'w', encoding='utf-8')
log = open('data/log.txt', 'w', encoding='utf-8')

i = 0
count_yandex = [0 for line_ya in f]
count_google = list(count_yandex)
count_percent = list(count_yandex)
yandex_all = 0
google_all = 0
time_dif = []
time_dif_yandex = []
time_dif_google = []
time_dif_different_yg = []
time_dif_different_gy = []
f = open('data/res_cut.txt', 'r')
#main part
for line in f:
    a = json.loads(line)
    #print(str(i+1)+': get line of ' + str(len(a)) + ' elements.', file=log)
    #print("    1st element is: timestamp = " + str(a[0]['ts']) + '; address = ' + a[0]['url'], file=log)
    j = 0
    j_yandex = -1
    j_google = -1
    for a_i in a:
        if j != 0:
            time_dif.append(a[j]['ts']-a[j-1]['ts'])
        if a[j]['url'] == 'yandex':
            count_yandex[i] += 1
            if j_yandex != -1:
                time_dif_yandex.append(a[j]['ts']-a[j_yandex]['ts'])
            j_yandex = j
            if (j - j_google) == 1 and j_google != -1:
                time_dif_different_yg.append(a[j]['ts']-a[j-1]['ts'])
                if a[j]['ts']-a[j-1]['ts'] < 5:
                    print(str(i+1)+':   Yandex: '+str(a[j]['ts'])+'  Google: '+str(a[j-1]['ts']), file=log)
        else:
            count_google[i] += 1
            if j_google != -1:
                time_dif_google.append(a[j]['ts']-a[j_google]['ts'])
            j_google = j
            if (j - j_yandex) == 1 and j_yandex != -1:
                time_dif_different_gy.append(a[j]['ts']-a[j-1]['ts'])
        j +=1
    count_percent[i] = 100*count_yandex[i] / (count_yandex[i]+count_google[i])
    if count_percent[i] == 100:
        yandex_all +=1
    if count_percent[i] == 0:
        google_all +=1
    i += 1
data = [x for x in count_percent]
print(yandex_all)
print(google_all)
plt.hist(data, 40)
plt.xlabel(u"Процент использования Яндекса", family="verdana")
plt.ylabel(u"Количество пользователей", family="verdana")
plt.show()

sum_yandex = 0
sum_google = 0
i = 0
j_yandex_ = 0
j_google_ = 0
for x in count_yandex:
    sum_yandex += count_percent[i]/100
    sum_google += (100-count_percent[i])/100
    if count_percent[i] == 0:
        j_yandex_ += 1
    if count_percent[i] == 100:
        j_google_ += 1
    i += 1
sum_yandex /= i - j_yandex_
sum_google /= i - j_google_

print('Yandex   '+str(sum_yandex)+' Google  '+str(sum_google))
