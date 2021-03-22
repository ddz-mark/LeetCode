import sys

def minDis(arr):
    fast = slow = front = 0
    res = -1
    while fast < len(arr):

        if arr[fast] != arr[slow] or arr[front] != arr[slow]:
            res = max(res, min(fast - slow, abs(front) + slow))
            slow += 1
            fast = slow
            front = slow
        fast += 1
        front -= 1

    return res


if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(minDis(arr))
