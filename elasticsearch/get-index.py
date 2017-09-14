#!/usr/bin/env python

import argparse

from elasticsearch  import Elasticsearch


def main(es_host, es_port):
    es = Elasticsearch([es_host], port=es_port)

    list_indices = es.indices.get_alias()

    for index in list_indices:
        print index


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--host', dest='es_host', required=True, help='Elasticsearch host address')
    parser.add_argument('--port', dest='es_port', default=9200, help='Elasticsearch port address')

    args = parser.parse_args()

    main(args.es_host, args.es_port)
