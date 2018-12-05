import logging
import sys
import datetime
import certstream
import yaml

from src.filters.check_ports import check
from src.filters.check_valid_certificate import check_valid_certificate
from src.filters.parse_source import parse_source
from src.filters.check_redirect import check_redirect
from src.filters.check_suspicious_words import check_words
from src.filters.check_blacklist import blacklist
import src.producers.styx_output as styx

BUNDLE_SIZE = 300 # How many analysis before exporting to a file?
VIRUSTOTAL_APIKEY = '' # your virustotal api key (optionnal)


def analyze_url_callback(message, content):
    global BUNDLE_SIZE
    print (BUNDLE_SIZE)

    if message['message_type'] == "heartbeat":
        return

    if message['message_type'] == "certificate_update":
        all_domains = message['data']['leaf_cert']['all_domains']

        if len(all_domains) != 0:
            domain = all_domains[0]

            if BUNDLE_SIZE == 0:
                print ("Writing in file!")
                indicators = []
                for url in suspicious_urls:
                    indicators.append(styx.forge_indicator(url[0], url[1]))
                if len(indicators) != 0:
                    styx.list_to_file(indicators, "out.json")
                exit(1)

            BUNDLE_SIZE -= 1
            launch_analysis(domain)
        
def ponderate(list_of_scores):
    ponderation = {"ports": 1,
                   "certificate": 2,
                   "parse_source": 1.5,
                   "redirect": 3,
                   "suspicious_word": 1,
                   "blacklist" : 0.1 # max score is 100, then result between 0 and 10
                  }              

    # maximum_score = sum(ponderation[c] for c in ponderation)
    # counter = 0
    total = 0
    for score in list_of_scores:
        # counter += 1
        if score[0] in ponderation:
            x = ponderation[score[0]]
            total += (score[1] * x)
        else:
            total += score[1] # Just in case we forget to add a ponderation, let's just add the score

    # return (100 * total) / maximum_score
    return total

def launch_analysis(url):

    """ Removing wildcards from domains """
    if url.startswith('*.'):
        url = url[2:]

    scores = []

    # print ("PORTS")
    scores.append(["ports", check(url)])
    # print ("parse_source")
    scores.append(["parse_source", parse_source(url)])
    # print("REDIRECT")
    scores.append(["redirect", check_redirect(url)])
    # print ("WORDS")
    scores.append(["suspicious_word", check_words(url, suspicious)])
    if VIRUSTOTAL_APIKEY != '':
        scores.append(["blacklist", blacklist(url, VIRUSTOTAL_APIKEY)])

    final_score = ponderate(scores)
    print (url + " => " + str(final_score))
    if final_score >= 8:
       suspicious_urls.append([url, final_score])

if __name__ == "__main__":

    with open('suspicious.yaml', 'r') as f:
        suspicious = yaml.safe_load(f)

    suspicious_urls = []
    certstream.listen_for_events(analyze_url_callback, "wss://certstream.calidog.io")

