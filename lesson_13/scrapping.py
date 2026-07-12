# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
numbers = list()
rows = soup('span')
for row in rows:
    print(row)
    # Look at the parts of a row
    print('ROW:', row)
    print('Contents:', row.contents[0])
    numbers.append(int(row.contents[0]))

print('the sum is: ', sum(numbers))
