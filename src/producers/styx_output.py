from stix2 import Indicator
from stix2 import Bundle
import datetime

def forge_indicator(url, timestamp):

    indicator = Indicator(name="Suspicious URL",
                      labels=["malicious-activity"],
                      created=timestamp,
                      pattern="[url:value = '" + url + "']")

    return indicator

def get_bundle(list_of_objects):
    return Bundle(objects=list_of_objects)

def get_time():
    now = datetime.datetime.now()
    format_iso_now = now.isoformat()
    return (str(now))

def output_to_file(bundle, filename):
    file = open(filename, "w")
    file.write(bundle)
    file.close()

if __name__ == "__main__":
    i = forge_indicator("http://test.com", get_time())
    b = get_bundle([i, i])
    print (b)
    output_to_file(b.serialize(indent=4), "test.txt")
