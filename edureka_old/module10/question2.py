from bs4 import BeautifulSoup as BS
import time
import urllib2
url = "https://www.imdb.com/chart/top"
    # http://www.imdb.com/search/title?genres=action&release_date=2010-01-01,&title_type=feature&user_rating=6.5,10

connected_url = urllib2.urlopen(url)
readHtml = connected_url.read()

connected_url.close()

soup = BS(readHtml,'html.parser')

my_info = soup.findAll("td",
{"class":"titleColumn"})
for i in range(len(my_info)):
    number = my_info[i].contents[0]
    number = number.strip()
    title = my_info[i].contents[1].get_text()
    year = my_info[i].contents[3].get_text()
    time.sleep(2)
    print(number + " " + title + " " + year)
#content = my_info[0].get_text()
#lines = content.split('\n')
#print(lines)
#print(dir(my_info[0]))
