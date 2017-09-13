#!/usr/bin/env python

import argparse
import json

from pymongo import MongoClient


def get_dbs(conn):

    return conn.database_names()


def get_collections(conn, db):
    database = conn[db]
    collections = database.collection_names(include_system_collections=False)

    return collections


def get_data_from_collection(conn, db, collection):
    database = conn[db]
    collection_name = database[collection]

    cursor = collection_name.find({})

    for document in cursor:
        print(document)


def main(host, show_dbs, show_collections, get_collection_data, db_name, collection_name):
    mongo_port = 27017
    conn = MongoClient(host, mongo_port)

    if show_dbs:
        for db in get_dbs(conn):
            print "Database: %s" % db
        print "\n"

    if show_collections:
        for db in get_dbs(conn):
            print "Collections in database: %s" % db
            for collection in get_collections(conn, db):
                print collection
            print "\n"

    if get_collection_data:
        get_data_from_collection(conn, db_name, collection_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--host', dest='host', required=True, help='MongoDB host address')
    parser.add_argument('--show-dbs', dest='show_dbs')
    parser.add_argument('--show-collections', default=True, dest='show_collections')
    parser.add_argument('--get-collection-data', dest='get_collection_data')
    parser.add_argument('--db-name', dest='db_name')
    parser.add_argument('--collection-name', dest='collection_name')

    args = parser.parse_args()

    main(args.host, args.show_dbs, args.show_collections, args.get_collection_data,
         args.db_name, args.collection_name)
