import requests
from bs4 import BeautifulSoup
from bs4 import Comment

""" Since we are parsing the source for HTTRACK, why not use it to also search for login inputs? """

def parse_source(url):
    url = url if url.startswith('http') else "http://%s" % url
    try:
        response = requests.get(url, timeout=3)
    except:
        return 1
    soup = BeautifulSoup(response.text, 'html.parser')
    comments=soup.find_all(string=lambda text:isinstance(text,Comment))

    score = 0
    for c in comments:
        if "HTTrack" in c:
            score += 1

    form = soup.find('form')
    if (len(form) != 0):
        score += 2

    inputs = soup.find_all('input')
    if (len(inputs) != 0):
        score += 1
        password = soup.findAll(True, {'id':['pwd', 'pass', 'password', 'passw', 'mdp', 'pass']})
        if (len(inputs) != 0):
            score += 1

    return score

if __name__ == '__main__':
    # print (check_for_httrack("http://chronopaiement.eu/a0a6a3e2a0e2b3a6e5ae7a8e5b6e9a8e/e0a6e3b2q10b2e3q2e5b4q/8639c668f01fbfd4db3b43014ba29e26/index.php"))
    print (parse_source("macuisinefrancaise.pro"))