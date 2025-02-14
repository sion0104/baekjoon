import sys
from collections import deque
import queue

input = sys.stdin.readline

N = int(input())

queue = deque()


def execution(command):
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) <= 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) <= 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) <= 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) <= 0:
            print(-1)
        else:
            print(queue[-1])


for _ in range(N):
    command = list(input().split())
    execution(command)
