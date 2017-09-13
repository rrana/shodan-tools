#!/usr/bin/env python

import argparse

import redis


def run(host):
    conn = redis.StrictRedis(host=host, port="6379", db=0)

    for key in conn.scan_iter("*"):
        print key


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', dest='host', required=True, help='Redis host address')
    args = parser.parse_args()

    run(args.host)
