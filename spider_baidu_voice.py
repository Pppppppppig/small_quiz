# import requests
# hea = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"}
# url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4"
# r = requests.get(url)
# r.encoding = r.apparent_encoding
# with open('page.htm', 'w') as f:
#     f.write(r.text)
import csv
import json

from bs4 import BeautifulSoup

r = open('page.htm', 'r').read()
soup = BeautifulSoup(r, "html.parser")
data = json.loads(str(soup.find_all('script', id="captain-config")[0]).replace(
    '<script id="captain-config" type="application/json">', '').replace('</script>', ''))
table_header = ['疫情地区', '新增', '现有', '累计', '治愈', '死亡']
table = list()
for i in data['component'][0]['caseList']:
    temp = dict()
    temp['疫情地区'] = i['area']
    temp['新增'] = i['confirmedRelative']
    temp['现有'] = i['curConfirm']
    temp['累计'] = i['confirmed']
    temp['治愈'] = i['crued']
    temp['死亡'] = i['diedRelative']
    table.append(temp)

with open('voice.csv', 'a', newline='', encoding='utf_8_sig') as f:
    writer = csv.DictWriter(f, fieldnames=table_header)
    writer.writeheader()
    writer.writerows(table)
