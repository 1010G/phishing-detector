import requests
from bs4 import BeautifulSoup
from bs4 import Comment

def check_for_httrack(url):
    url = url if url.startswith('http') else "http://%s" % url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    comments=soup.find_all(string=lambda text:isinstance(text,Comment))

    for c in comments:
        if "HTTrack" in c:
            return 1
    return 0


if __name__ == '__main__':
    # print (check_for_httrack("http://chronopaiement.eu/a0a6a3e2a0e2b3a6e5ae7a8e5b6e9a8e/e0a6e3b2q10b2e3q2e5b4q/8639c668f01fbfd4db3b43014ba29e26/index.php"))
    print (check_for_httrack("macuisinefrancaise.pro"))