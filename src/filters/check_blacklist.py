import urllib
import json
import socket

APIKEY = 'APIKEY'

def blacklist(domain):
    ip = socket.gethostbyname(domain)
    blacklistIp(ip)
    blacklistDomain(domain)

    return

def blacklistIp(ip):
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    parameters = {'ip': ip, 'apikey': APIKEY}
    response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
    response_dict = json.loads(response)
    #TODO detected_urls alors detected
    print response_dict

    return

def blacklistDomain(domain):
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    parameters = {'domain': domain, 'apikey': APIKEY}
    response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
    response_dict = json.loads(response)
    print(response_dict)
    # TODO detected_urls alors detected
    return

if __name__ == '__main__':
    blacklist("DOMAIN")