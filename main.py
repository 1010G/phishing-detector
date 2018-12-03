import logging
import sys
import datetime
import certstream
from src.filters.check_ports import check
from src.filters.check_valid_certificate import check_valid_certificate
from src.filters.check_for_httrack import check_for_httrack
from src.filters.check_redirect import check_redirect
import src.producers.styx_output as styx

BUNDLE_SIZE = 10 # How many analysis before exporting to a file?

def analyze_url_callback(message, content):
    global BUNDLE_SIZE

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
                styx.list_to_file(indicators, "out.json")
                BUNDLE_SIZE = 10

            BUNDLE_SIZE -= 1
            launch_analysis(domain)
        
def ponderate(list_of_scores):
    ponderation = {"ports": 1,
                   "certificate": 2,
                   "httrack": 5,
                   "redirect": 3
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

    print("PORTS")
    scores.append(["ports", check(url)])
    print("CERT")
    scores.append(["certificate", check_valid_certificate(url)])
    print("HTTRACK")
    scores.append(["httrack", check_for_httrack(url)])
    print("REDIRECT")
    scores.append(["redirect", check_redirect(url)])

    final_score = ponderate(scores)
    print (final_score)
    if final_score >= 4:
       suspicious_urls.append([url, final_score])

if __name__ == "__main__":

    suspicious_urls = []
    certstream.listen_for_events(analyze_url_callback, "wss://certstream.calidog.io")

