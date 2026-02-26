#!/usr/bin/env python3

import sys

def fifo(capacity, requests):
    cache = []
    misses = 0
    for req in requests:
        if req not in cache:
            if len(cache) == capacity:
                cache.pop(0)
            cache.append(req)
            misses += 1
    return misses

def lru(capacity, requests):
    cache = []
    misses = 0
    for req in requests:
        if req not in cache:
            if len(cache) == capacity:
                cache.pop(0)
            cache.append(req)
            misses += 1
        else:
            cache.remove(req)
            cache.append(req)
    return misses

def optff(capacity, requests):
    cache = []
    misses = 0
    for i, req in enumerate(requests):
        if req not in cache:
            if len(cache) == capacity:
                latest = None
                latest_i = 0
                for item in cache:
                    try:
                        item_i = requests.index(item, i + 1)
                    except ValueError:
                        latest = item
                        break
                    if item_i > latest_i:
                        latest = item
                        latest_i = item_i
                cache.remove(latest)
            cache.append(req)
            misses += 1
    return misses

def main():
    import optparse
    parser = optparse.OptionParser(usage="%prog [options] [file]")
    opts, args = parser.parse_args()

    if args:
        file = open(args[0])
    else:
        file = sys.stdin

    capacity, count, *requests = [int(value) for value in file.read().split()]

    for mode in fifo, lru, optff:
        name = mode.__name__.upper()
        misses = mode(capacity, requests)
        print(f"{name:6}: {misses}")

if __name__ == "__main__":
    main()
