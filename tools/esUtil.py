from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("104.140.18.185")
text_str = "lisi"
doc = {
    'author': 'kimchy',
    'text': text_str,
    'timestamp': datetime.now(),
}
# res = es.index(index="test-index", doc_type='tweet', id=2, body=doc)  
res = es.index(index="test-index", doc_type='tweet', body=doc) # id不指定 将默认生成
print(res['created'])

res = es.get(index="test-index", doc_type='tweet', id=2)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])