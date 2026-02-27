#!/usr/bin/env python3

def main():
    import optparse
    parser = optparse.OptionParser(usage="%prog [options]")
    parser.add_option("-k", "--capacity", metavar="N", type="int", default=5, help="cache size [default: %default]")
    parser.add_option("-n", "--count", metavar="N", type="int", default=50, help="number of items to generate [default: %default]")
    parser.add_option("-r", "--range", metavar="N", type="int", default=10, help="range of request IDs [default: %default]")
    opts, args = parser.parse_args()

    import random
    import sys

    sys.stdout.reconfigure(newline="")
    print(f"{opts.capacity} {opts.count}")
    print(" ".join(str(random.randint(1, opts.range)) for i in range(opts.count)))

if __name__ == "__main__":
    main()
