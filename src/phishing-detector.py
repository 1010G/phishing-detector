#!/usr/bin/python3
# -*- coding: utf-8 -*-
from filters.href_filter import href_filter
import re

def phishing_detector():
    lines=[]
    urls=[] # list des urls
    with open('FLURL.txt') as f:
        lines = f.readlines()
    for i in lines:
        t = re.sub ('[^A-Za-z0-9-.]+', '', i.split(" - ")[-1])#del specials chars
        t=t[+5:-2] #chars
        urls.append(t)
    lines=None

    #Application des filtres
    for url in urls:
        urltmp="http://www."+url[+1:-2]+"/"
        urltmp2=url.replace(" ","").strip()
        print(urltmp2)
        print(href_filter("http://"+urltmp2,0.1))
if __name__ == "__main__":
    phishing_detector()