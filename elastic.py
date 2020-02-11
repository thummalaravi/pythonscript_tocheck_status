import requests
import json, os
from elasticsearch import Elasticsearch
res = requests.get('http://172.31.6.226:9200')
#print (res.content)
directory = '/home/ubuntu/services-metrics/'
es = Elasticsearch([{'host': '172.31.6.226', 'port': '9200'}])
print(es)
i = 1
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        file=directory+filename
        f = open(file)
        docket_content = f.read()
        # Send the data into es
        es.index(index='rbcapp1', ignore=400, doc_type='docket',
        id=i, body=json.loads(docket_content), request_timeout=30)
        i = i + 1
