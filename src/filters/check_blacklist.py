import requests
import json
import socket


def blacklist(domain, APIKEY):
    score = 0
    try:
        score+=blacklistDomain(domain, APIKEY)
    except:
        score+=0
    try:
        ip = socket.gethostbyname(domain)
        score+=blacklistIp(ip, APIKEY)
    except:
        score+=0

    #print("final score : " + str(score))

    return score

def blacklistIp(ip,APIKEY):
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    parameters = {'ip': ip, 'apikey': APIKEY}
    response = requests.get(url, params=parameters)
    response_json = response.json()

    return len(response_json['detected_urls'])

def blacklistDomain(domain,APIKEY):
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    parameters = {'domain': domain, 'apikey': APIKEY}
    response = requests.get(url, params=parameters)
    response_json = response.json()
    if(response_json['verbose_msg'] == 'Domain not found'):
        return 0

    return len(response_json['detected_urls'])

if __name__ == '__main__':
    apikey = ''
    blacklist("domain.fr",apikey)