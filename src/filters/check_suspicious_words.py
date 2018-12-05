def check_words(url, wordlist):

    """                      Mostly based on the work of x0rz                  """
    """ https://github.com/x0rz/phishing_catcher/blob/master/catch_phishing.py """

    score = 0
    for word in wordlist['keywords']:
        if word in url:
            score += (wordlist['keywords'][word] / 10)

    """ Now check TLD """
    for t in wordlist['tlds']:
        if url.endswith(t):
            score += 1

    """ Too many . ? """
    if url.count('.') >= 3:
        score += 1

    return score
    