import json
import re

f = open('data/search_log_10000.txt', 'r', encoding='utf-8')
f1 = open('data/res_cut.txt', 'w', encoding='utf-8')
log = open('data/log_initial.txt', 'w', encoding='utf-8')

i = 0
j=0
count_yandex = [0 for line_ya in f]
count_google = list(count_yandex)
count_yandex_google = list(count_yandex)
count_google_yandex = list(count_yandex)

f = open('data/search_log_10000.txt', 'r')
#main part
for line in f:
    a = json.loads(line)
    print(str(i+1)+': get line of ' + str(len(a)) + ' elements.', file=log)
    if len(a) > 0:
       # print("    1st element is: timestamp = " + str(a[0]['ts']) + '; address = ' + a[0]['url'], file=log)
        match = re.match(r".*(yandex|google)\.com\.tr.*", a[0]['url'])
        if match:
            print('    in the beginning was... ' + str(match.group(1)), file=log)
        else:
            print('    Site isn\'t recognized.  ', file=log)
        j = 0
        j_for_deleting = []
        #analysis of each dictionary
        for a_i in a:
            match2 = re.match(r"^((\w+://)?[^/]*(yandex|google)\.com\.tr/((url\?|clck/).*|installcounter\..?.?.?\.html)?|((\w+://)?[^/]*(yandex\.com\.tr/(\?clid=|.*goo?g?gll?e?.*))|google\.com\.tr/.*yandex.*))$", a_i['url'])
            if match2:
                j_for_deleting.append(j)
                print(str(j)+":  Search results and start pages: " + a_i['url'], file=log)
                a[j]['url'] = str(match2.group(3))+"_search_results_or_start_page"
            else:
                match = re.match(r"^(\w+://)?[^/]*(yandex|google)\.com\.tr/.*?$", a_i['url'])
                if match:
                    #print(str(j)+":  Work_in: " + a_i['url'], file=log)
                    a[j]['url'] = str(match.group(2))
                    if str(match.group(2)) == 'yandex':
                        count_yandex[i] += 1
                    else:
                        count_google[i] += 1
                else:
                    j_for_deleting.append(j)
                    #print(str(j)+":  Nothing matched in: " + a_i['url'], file=log)
                    inner_match = re.match(r"^(\w+://)?([^/]+)/.*(yandex|google).*", a_i['url'])
                    if inner_match:
                        #print("    User redirected to " + str(inner_match.group(3)) + " from " + str(inner_match.group(2)), file=log)
                        a[j]['url'] = str(inner_match.group(2))
                    else:
                        print("    Shit happens", file=log)
                        a[j]['url'] = "    Shit happens"
            j +=1
        print('Yandex: '+str(100*count_yandex[i]/len(a))+
              '%  Google: '+ str(100*count_google[i]/len(a))+
              '% All: ' + str(100*(count_yandex[i]+count_google[i])/len(a))+'%'
              'for del'+ str(j_for_deleting), file=log)
        k = 0
        for x in j_for_deleting:
            del a[x-k]
            k += 1
        if len(a) > 5:
            print(json.dumps(a), file=f1)
    else:
        print("    Nothing to show", file=log)
    i += 1
