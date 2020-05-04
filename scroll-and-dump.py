#!/usr/local/bin/python3
import json
from elasticsearch import Elasticsearch, helpers

ES_HOST = 'localhost:9200'
ES_USER = 'elastic'
ES_PASSWORD = 'elastic'
INDEX_TO_DUMP = 'kibana_sample_data_ecommerce'
OUT_FILE = '/tmp/dump-example.txt'
es = Elasticsearch([ES_HOST], http_auth=(ES_USER, ES_PASSWORD))


def scroll_and_dump():

    with open(OUT_FILE, 'w') as out_file:

        # Before scroll, process current batch of hits
        for data in helpers.scan(es, index=INDEX_TO_DUMP):
            out_file.write(f"{json.dumps(data['_source'])}\n")


if __name__ == "__main__":
    scroll_and_dump()
