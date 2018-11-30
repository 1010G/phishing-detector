#!/usr/bin/python3
# -*- coding: utf-8 -*-
from filters.href_filter import href_filter


def phishing_detector():
    lines=[]
    urls=[] # list des urls
    with open('FLURL.txt') as f:
        lines = f.readlines()
    for i in lines:
        urls.append(i.split("-")[-1])
    lines=None

    #Application des filtres
    for url in urls:
        #print(str(url))
        urltmp="http://www."+url[+1:-2]+"/"
        urltmp2=url.replace(" ","").strip()
        print(urltmp)
        print(urltmp2)
        href_filter("http://"+urltmp2,0.1)
        #href_filter(urltmp,0.1)
        #href_filter("http://www.protcom.com/",0.1)
        #href_filter("http://www."+url,0.1)

if __name__ == "__main__":
    phishing_detector()