#coding=GB2312
import requests
import re
import threading


def get_pics(num):
    url = 'http://jandan.net/ooxx/page-%i' % num
    a = requests.get(url)
    a.encoding = a.apparent_encoding
    result = ['http:' + x[10:].encode(encoding='utf-8') for x in re.findall('<img src=".+.jpg{1}?', a.text)]
    for url in result:
        pic = requests.get(url)
        with open(url[28:], 'wb') as f:
            f.write(pic.content)
        print '%s�������' % url[28:]


def webspider():
    start = input('�����뿪ʼҳ����')
    end = input('���������ҳ����')
    pages = range(start, end+1)
    threads = []
    for i in pages:
        threads.append(threading.Thread(target=get_pics, args=(i,)))
    for t in threads:
        t.setDaemon(True)
        t.start()


webspider()
raw_input('�ȴ���������س����˳���\n')