# -*- coding: utf-8 -*-
# @Author:varcer
import requests as req
import threading
def adjust(url):
    temp=url.replace(' ','').split('/')
    if 'http:' in temp or 'https:' in temp:
        temp.pop(0)
    if '.' in temp[-1]:
        temp.pop()
    url='/'.join(temp)+'/'
    url=url.lstrip('/')
    return 'http://'+url
def scan(url,ext):
    temp=url
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}
    f=open('file/directory-list.txt',encoding='utf-8')
    fe=open('file/suffix',encoding='utf-8')
    if '?' in ext and '*' in ext:
        for i in fe:#读取文件路径文件
                for j in f:
                    direc=ext.replace('?',j.replace('\n','')).replace('*',i.replace('\n',''))
                    url = temp + direc
                    html = req.get(url).text
                    singer=open('./file/singer')
                    flage = True
                    for s in singer:
                        if s.replace('\n', '') in html:
                            flage = False
                            break
                    if flage:
                        print(url)
                    singer.close()
    elif '?' in ext:
        for j in f:
            direc = ext.replace('?', j.replace('\n', ''))
            url = temp + direc
            html = req.get(url).text
            singer = open('./file/singer')
            flage = True
            for s in singer:
                if s.replace('\n', '') in html:
                    flage = False
                    break
            if flage:
                print(url)
            singer.close()
    else:
        url = temp +ext
        html=req.get(url,headers=header).text
        singer = open('./file/singer')
        flage = True
        for s in singer:
            if s.replace('\n','') in html:
                flage = False
                break
        if flage:
            print(url)
        singer.close()
def control(num,url):
    th=[]
    f=open('file/extend',encoding='utf-8')
    for i in f:#读文件后缀名文件
        while 1:#空时线程数
            if int(num)>=threading.activeCount():
                T=threading.Thread(target=scan,args=(url,i.replace('\n','')))
                T.start()
                th.append(T)
                break
    for t in th:
        t.join()
def start(url,num):
    url=adjust(url)
    try:
        num=int(num)
    except:
        num=1
    control(num, url)
if __name__=='__main__':
    print('只支持当前url下爆破')
    url=input("输入url:")
    num=input('输入线程数:')
    start(url,num)
