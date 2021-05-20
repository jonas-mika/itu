# solving kattis problem 'flights'
import sys
from datetime import datetime, timedelta
from itu.algs4.searching.red_black_bst import RedBlackBST

lines = sys.stdin.readlines()
n, m = [int(i) for i in lines[0].strip().split()]

# read flights into ST (with support for operations)
ST = RedBlackBST()
for line in lines[1: n+1]:
    time, destination = line.strip().split()
    ST.put(datetime.strptime(time, '%H:%M:%S'), destination)

# answer queries
for q in lines[n+1: len(lines)]:
    query = q.strip().split()
    command = query[0]

    # cancel flight by deleting from ST
    if command == 'cancel':
        ST.delete(datetime.strptime(query[1], '%H:%M:%S'))

    # delay a flight by d amount of seconds
    elif command == 'delay':
        s, d = query[1:]
        time = datetime.strptime(s, '%H:%M:%S')
        val = ST.get(time)
        ST.delete(time)
        updated_t = time + timedelta(seconds=int(d))
        ST.put(updated_t, val)

    # reroute a flight such that the destination changes for a given key
    elif command == 'reroute':
        s, c = query[1:]
        ST.put(datetime.strptime(s, '%H:%M:%S'), c)

    # query ST for time, print destination if time exists, else '-'
    elif command == 'destination':
        time = datetime.strptime(query[1], '%H:%M:%S')
        if ST.get(time) is not None:
            print(ST.get(time))
        else:
            print('-')

    # query ST for next available flight, which is equal to computing the ceiling of the given key
    elif command == 'next':
        time = datetime.strptime(query[1], '%H:%M:%S')
        ceiling = ST.ceiling(time)
        print(ceiling.time(), ST.get(ceiling))

    # query ST for number of flights in given time interval
    elif command == 'count':
        t1, t2 = datetime.strptime(
            query[1], '%H:%M:%S'), datetime.strptime(query[2], '%H:%M:%S')
        print(ST.size_range(t1, t2))
