# Programming Assignment 2: Greedy Algorithms

COP4533 - Algorithm Abstraction and Design

Daniel Li - 99157575

## Running

You will need a recent version of Python (tested with Python 3.14.3).

`cache.py` reads from the specified file or standard input. Example:

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

where the three policies are:

* FIFO = first-in-first-out
* LRU = least recently used
* OPTFF = Belady's farthest-in-future, optimal offline

## Empirical Comparison

## Bad Sequence for LRU or FIFO

## Proof of OPTFF Optimality
