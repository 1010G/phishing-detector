import logging
import sys
import datetime
import certstream
from src.filters.check_ports import check
from src.filters.check_valid_certificate import check_valid_certificate
from src.filters.check_for_httrack import check_for_httrack
from src.filters.check_redirect import check_redirect


def print_callback(message, context):
    logging.debug("Message -> {}".format(message))

    if message['message_type'] == "heartbeat":
        return

    if message['message_type'] == "certificate_update":
        all_domains = message['data']['leaf_cert']['all_domains']

        if len(all_domains) == 0:
            domain = "NULL"
        else:
            domain = all_domains[0]

        sys.stdout.write(u"[{}] {} (SAN: {})\n".format(datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S'), domain, ", ".join(message['data']['leaf_cert']['all_domains'][1:])))
        sys.stdout.flush()

def analyze_url_callback(message, content):
    if message['message_type'] == "heartbeat":
        return

    if message['message_type'] == "certificate_update":
        all_domains = message['data']['leaf_cert']['all_domains']

        if len(all_domains) != 0:
            domain = all_domains[0]
            print ("Sendign to scorer")
            launch_analysis(domain)
        

def launch_analysis(url):

    """ Removing wildcards from domains """
    if url.startswith('*.'):
        url = url[2:]

    ports = check(url)
    valid_certificate = check_valid_certificate(url)
    httrack = check_for_httrack(url)
    redirect = check_redirect(url)

    # print (url, redirect)
    print ([url, ports, valid_certificate, httrack, redirect])
    None

    

logging.basicConfig(format='[%(levelname)s:%(name)s] %(asctime)s - %(message)s', level=logging.INFO)

certstream.listen_for_events(analyze_url_callback, "wss://certstream.calidog.io")