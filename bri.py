#!/usr/bin/python
# -*- coding: gbk -*-
# author: nullne
# Email: co.crary@gmail.com

import urllib, urllib2, cookielib
import sys
import os
from getpass import getpass
try:
    from bs4 import BeautifulSoup
except:
    print "Error,this may help:"
    print "    pip install BeautifulSoup4"
try:
    import requests
except:
    print "Error,this may help:"
    print "    pip install requests"

try:
    sys_encode = os.popen('locale').readlines()[0].split('.')[1].strip()[:-1]
except:
    print "please make sure running this script on *nix system"
    sys.exit(0)
username = raw_input("ID: ")
password = getpass("PASSWORD: ")
comment = raw_input("COMMENT: ")
comment = comment.decode(sys_encode)
degree = raw_input("degree(1-8,1 is the best): ")
degree = degree.decode(sys_encode).encode('GBK')
if int(degree)  not in range(1,8):
    print "input out of range,retry again"
    sys.exit(0)

degree_const = {
        1: '0.99',
        2: '0.95',
        3: '0.9',
        4: '0.85',
        5: '0.8',
        6: '0.7',
        7: '0.6',
        8: '0.4'}
login_data = {
        'zjh': username.decode(sys_encode),
        'mm': password.decode(sys_encode),
        'type': 'sso'}
login = requests.post('http://10.3.240.70/jwLoginAction.do', data=login_data)
cook = "JSESSIONID=" + login.cookies['JSESSIONID']
fetch_list = requests.get('http://10.3.240.70/jxpgXsAction.do?oper=listWj',cookies=login.cookies)
soup = BeautifulSoup(fetch_list.content.decode('gbk'))
data_init = soup.find_all(title="评估")
data = []
for i in data_init:
    data.append({'wjbm':i['name'].split('#@')[0],
        'bpr':i['name'].split('#@')[1],
        'pgnr':i['name'].split('#@')[5],
        'wjmc':i['name'].split('#@')[3],
        'bprm':i['name'].split('#@')[2],
        'pgnrm':i['name'].split('#@')[4],})
if len(data) == 0:
    print "login error OR you have already done"
    sys.exit(0)

for i in data:
    pre_post_data = {
        'wjbm': i['wjbm'].encode('GBK'),
        'bpr': i['bpr'].encode('GBK'),
        'pgnr': i['pgnr'].encode('GBK'),
        'oper': 'wjShow',
        'wjmc': i['wjmc'].encode('GBK'),
        'bprm': i['bprm'].encode('GBK'),
        'pgnrm': i['pgnrm'].encode('GBK'),
        'pageSize': '20',
        'page': '1',
        'currentPage': '1',
        'pageNo':''}
    headers = {
            'Host': '10.3.240.70',
            'Referer': 'http://10.3.240.70/jxpgXsAction.do?oper=listWj',
            }
    fake_click = requests.post('http://10.3.240.70/jxpgXsAction.do', data=pre_post_data, cookies=login.cookies, headers=headers)
    post_data = {
        'wjbm':i['wjbm'].encode('GBK'),
        'bpr':i['bpr'].encode('GBK'),
        'pgnr':i['pgnr'].encode('GBK'),
        '0000000021':'10_'+degree_const[int(degree)],
        '0000000022':'10_'+degree_const[int(degree)],
        '0000000023':'5_'+degree_const[int(degree)],
        '0000000024':'20_'+degree_const[int(degree)],
        '0000000025':'10_'+degree_const[int(degree)],
        '0000000026':'5_'+degree_const[int(degree)],
        '0000000027':'5_'+degree_const[int(degree)],
        '0000000028':'20_'+degree_const[int(degree)],
        '0000000029':'10_'+degree_const[int(degree)],
        '0000000030':'5_'+degree_const[int(degree)],
        'zgpj': comment.encode('GBK')
    }
    headers = {
            'Host': '10.3.240.70',
            'Referer': 'http://10.3.240.70'
            }
    vote = requests.post('http://10.3.240.70/jxpgXsAction.do?oper=wjpg', data=post_data, cookies=login.cookies, headers=headers)
    out =  vote.content
    if str(out).find('成功') >= 0:
        print "---- success on " + i['bprm']
    else:
        print "---- fail on " + i['bprm']
        print "so embarrassed.."

print "Done,see you"
