# Programming Assignment 2: Greedy Algorithms

COP4533 - Algorithm Abstraction and Design

Daniel Li - 99157575

## Running

You will need a recent version of Python (tested with Python 3.14.3).

`cache.py` reads from the provided file,
or standard input if no file is specified. Example:

```
./cache.py examples/example.in
```

Compare the output with `examples/example.out`.

## Input and Output

The input format is:

```
k m
r1 r2 r3 ... rm
```

where:

* k = cache capacity
* m = number of requests
* r1, ..., rm = integer request IDs

The output format is:

```
FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
```
