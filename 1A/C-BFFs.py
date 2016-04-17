import sys
import os
import itertools

def main():
    T = int(input())
    for t in xrange(T):
        N = int(input())
        F = map(lambda s: int(s)-1, raw_input().strip().split(' '))

        r = 0

        # Find cycles
        for i in xrange(N):
            visited = [False] * N
            l = 1
            cur = F[i]
            while cur != i and not visited[cur]:
                visited[cur] = True
                cur = F[cur]
                l += 1

            if cur == i:
                r = max(r, l)

        # Find 2-cycles
        is2Cycle = [False] * N
        cycle_lens = [-1] * N
        for i in xrange(N):
            if F[F[i]] == i:
                is2Cycle[i] = True
                cycle_lens[i] = 0

        # Find the longest chain for every 2-cycle
        for i in xrange(N):
            visited = [False] * N
            cur = i
            l = 0
            while not is2Cycle[cur] and not visited[cur]:
                visited[cur] = True
                cur = F[cur]
                l += 1

            if is2Cycle[cur]:
                cycle_lens[cur] = max(cycle_lens[cur], l)

        # Compute the sum of chain lengths
        sum_chains = 0
        used = [False] * N
        for i in xrange(N):
            if is2Cycle[i] and not used[i]:
                 sum_chains += cycle_lens[i] + 2 + cycle_lens[F[i]] # the length of the two ends and the 2-cycle
                 used[i] = used[F[i]] = True

        r = max(sum_chains, r)
        print "Case #%d: %d" % (t+1, r)

if __name__ == "__main__":
    main()
