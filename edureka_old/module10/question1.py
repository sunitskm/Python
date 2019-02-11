import sys
from bs4 import BeautifulSoup as BS
import urllib2
print("Hello")
print(sys.argv[1])
for i in range(1,len(sys.argv)):
    test_url = urllib2.urlopen(sys.argv[i])
    readhtml = test_url.read()
    test_url.close()

    soup = BS(readhtml)
    first_10_a_tags = soup.find_all("a")

    for links in first_10_a_tags:
        print (links.get('href'))
