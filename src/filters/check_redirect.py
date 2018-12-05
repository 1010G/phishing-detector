""" Check if the domain redirects to another """
import sys
import requests

""" Sub function """
def check_for_redirects(url):
    try:
        r = requests.get(url, allow_redirects=False, timeout=0.5)
        if 300 <= r.status_code < 400:
            return r.headers['location']
        else:
            # return '[no redirect]'
            return 0
    except requests.exceptions.Timeout:
        return '[timeout]'
    except requests.exceptions.ConnectionError:
        return '[connection error]'


""" If no protocol is defined, use http """
def check_redirect(url):

    url_to_check = url if url.startswith('http') else "http://%s" % url

    redirect_url = check_for_redirects(url_to_check)
    # print("%s => %s" % (url_to_check, redirect_url))

    if redirect_url != 0:
        """ Take into account HTTPS redirections """
        if ("https://" + url + "/") == redirect_url:
            return 0
        else:
            return 1
    else:
        return 0


if __name__ == '__main__':
    print(check_redirect("tafsiralahlam.com"))
