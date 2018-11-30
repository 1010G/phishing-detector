#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests


def webService_filter80(url):
    r = requests.get("http://www.google.fr")
    print(r)
    print("wow")

if __name__ == "__main__":
    webService_filter80(1)