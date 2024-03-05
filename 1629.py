import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())


def multi(A, N):
    if N == 1:
        return A % C
    else:
        tmp = multi(A, N // 2)
        if N % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C

print(multi(A, B))
