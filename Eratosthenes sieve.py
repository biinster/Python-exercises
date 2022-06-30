'''An implementation of the Eratosthenes sieve'''

def primes_sieve(num):
'''Prints out a comma-separated lsit of primes up to "num".'''
    ps=set(range(2,num+1))
    pfs=set()
    while min(ps)<max(ps)**0.5:
        pfs.add(min(ps))
        ps.difference_update(set(list(range(max(pfs),max(ps)+1))[::max(pfs)]))
    ps|=pfs
    print(', '.join(str(p) for p in list(ps)))

#User input
while True:
    print("Please enter a positive integer for the upper limit (""minus"" sign will be discarded):")
    try: primes_sieve(abs(int(input())))
    except: continue
    break
