import requests
from requests.exceptions import SSLError

def check_valid_certificate(url):
    url = url if url.startswith('https') else "https://%s" % url

    try:
        requests.get(url, verify=True)
    except SSLError:
        # SSL error, returning 1
        return 1
    return 0

if __name__ == "__main__":
    print(check_valid_certificate("macuisinefrancaise.pro"))