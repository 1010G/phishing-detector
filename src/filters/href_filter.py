#!/usr/bin/python3
# -*- coding: utf-8 -*-

#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
#import urllib2
import requests


def getDomain(url):
    spltAr = url.split("://")
    i = (0,1)[len(spltAr)>1]
    dm = spltAr[i].split("?")[0].split('/')[0].split(':')[0].lower()
    return dm

def href_filter(url,prct):
    """
    :param url: url
    :param prct: % of domain on href
    :return: 0 if fitler is OK, 1 if malicious
    """
    hrefs=[]
    #html_page = urllib2.urlopen(url)
    html_page = requests.get("http://"+url)
    soup = BeautifulSoup(html_page.text,"html.parser")
    for link in soup.findAll('a'):
        #print(link)
        if link.get('href') is not None:#bypass None problem
            if "://" in link.get('href') : # href contain ://   /login.php will not be concerned
                tmp=getDomain(link.get('href'))
                if tmp != "":hrefs.append(tmp)
    domains=[]
    for i in hrefs:
        tmpres=str(i.split(".")[-2])+"."+str(i.split(".")[-1])
        domains.append(tmpres)
    domain=url.split(".")
    nbDomain=domains.count(domain[-2]+"."+domain[-1])
    nbAll=len(domains)

    if float(nbAll)> 0 :
        tauxSimi=float(float(nbDomain) / float(nbAll))
        if ( tauxSimi <= prct):
            return 1
        else:
            return 0
    return 0


if __name__ == "__main__":
    print(href_filter("http://www.9gag.com",0.1))
    print(href_filter("http://www.lorinmoshe.com/",0.1))
    #print(href_filter("http://chronopaiement.eu/a0a6a3e2a0e2b3a6e5ae7a8e5b6e9a8e/e0a6e3b2q10b2e3q2e5b4q/8639c668f01fbfd4db3b43014ba29e26/index.php",0.1))


