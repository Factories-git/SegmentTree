# import sys
#
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
# treeheight = 0
# length = n
#
# while length != 0:
#     length //= 2
#     treeheight += 1
#
# treeSize = pow(2, treeheight + 1)
# leftNodeStartIndex = treeSize // 2 - 1
# tree = [0] * (treeSize + 1)
#
# for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + n + 1):
#     tree[i] = int(input())
#
#
# def setTree(i):
#     while i != 1:
#         tree[i // 2] += tree[i]
#         i -= 1
#
#
# setTree(treeSize - 1)
#
#
# def changeVal(index, value):
#     diff = value - tree[index]
#     while index > 0:
#         tree[index] = tree[index] + diff
#         index = index // 2
#
#
# def getSum(s, e):
#     partSum = 0
#     while s <= e:
#         if s % 2 == 1:
#             partSum += tree[s]
#             s += 1
#         if e % 2 == 0:
#             partSum += tree[e]
#             e -= 1
#         s = s // 2
#         e = e // 2
#     return partSum
#
#
# for _ in range(m + k):
#     question, s, e = map(int, input().split())
#     if question == 1:
#         changeVal(leftNodeStartIndex + s, e)
#     elif question == 2:
#         s = s + leftNodeStartIndex
#         e = e + leftNodeStartIndex
#         print(getSum(s, e))

def seg_init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = seg_init(start,mid,idx * 2) + seg_init(mid+1,end,idx*2+1)
    return tree[idx]


def prefix_sum(start,end,idx,left,right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[idx]
    mid = (start + end) // 2
    return prefix_sum(start, mid, idx*2, left, right) + prefix_sum(mid+1, end, idx*2+1, left, right)


def seg_update(start, end, idx, target_node, value):
    if target_node < start or target_node > end:
        return
    tree[idx] += value
    if start == end:
        return
    mid = (start + end) // 2
    seg_update(start, mid, idx*2, target_node, value)
    seg_update(mid+1, end, idx*2+1, target_node, value)


n, m, k = map(int, input().split())
arr = [int(input()) for i in range(n)]
tree = [0] * (n * 4)

seg_init(0, n-1, 1)
for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        temp = c - arr[b-1]
        arr[b-1] = c
        seg_update(0, n-1, 1, b-1, temp)
    else:
        print(prefix_sum(0, n-1,1, b-1, c-1))

