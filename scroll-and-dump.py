#!/usr/local/bin/python3
import json
from elasticsearch import Elasticsearch

ES_HOST = 'localhost:9200'
ES_USER = 'elastic'
ES_PASSWORD = 'elastic'
INDEX_TO_DUMP = 'kibana_sample_data_ecommerce'
OUT_FILE = '/tmp/dump-example.txt'
es = Elasticsearch([ES_HOST], http_auth=(ES_USER, ES_PASSWORD))


def dump_hits(hits, out_file):
    for hit in hits:
        out_file.write(f"{json.dumps(hit['_source'])}\n")


def scroll_and_dump():
    with open(OUT_FILE, 'w') as out_file:
        data = es.search(index=INDEX_TO_DUMP, scroll='1m', body={"query": {"match_all": {}}})

        # Get the scroll ID
        sid = data['_scroll_id']
        scroll_size = len(data['hits']['hits'])

        # Before scroll, process current batch of hits
        dump_hits(data['hits']['hits'], out_file)

        while scroll_size > 0:
            data = es.scroll(scroll_id=sid, scroll='2m')

            # Process current batch of hits
            dump_hits(data['hits']['hits'], out_file)

            # Update the scroll ID
            sid = data['_scroll_id']

            # Get the number of results that returned in the last scroll
            scroll_size = len(data['hits']['hits'])


if __name__ == "__main__":
    scroll_and_dump()
