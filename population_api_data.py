import urllib
import urllib2
url = 'https://api.dandelion.eu/datagems/v2/SpazioDati/administrative-regions/data?$select=parentNames,population,name&$limit=100000000&$where=parentNames.country="ITALIA"+AND+level=70&$offset=0&$order=level+asc&$app_id=3dc2ee0e&$app_key=e265d74765762b59bdce606ac0ff0afc'
# url = 'https://api.dandelion.eu/datagems/v2/SpazioDati/administrative-regions/data?$select=parentNames,population,name&$where=parentNames.country="ITALIA"+AND+level=70&$offset=0&$order=level+asc&$app_id=3dc2ee0e&$app_key=e265d74765762b59bdce606ac0ff0afc'
response = urllib2.urlopen(url)
html = response.read()
print html

text_file = open("dandelion_by_municipality_api_large_limit_2.txt", "w")
text_file.write(html)
text_file.close()