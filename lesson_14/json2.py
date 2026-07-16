import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)
print('User count:', len(info))

comments = info['comments']
commentsTotal = list()
for item in comments:
    print('Name', item['name'])
    print('Count', item['count'])
    commentsTotal.append(item['count'])

print(sum(commentsTotal))