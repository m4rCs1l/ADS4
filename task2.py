def bucket_sort(arr):
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]

            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    n = len(arr)
    block_size = max(arr) / n
    blocks = [[] for i in range(n)]
    for item in arr:
        i = int(item/block_size)
        i = i if i < n else i-1

        blocks[i].append(item)
    arr = []
    for item in blocks:
        if item != []:
            insertion_sort(item)
            arr += item
    return arr


def max_heapify(arr, index, size):
    def left(i):  return 2 * i + 1
    def right(i): return 2 * i + 2

    l = left(index)
    r = right(index)
    if (l < size and arr[l] > arr[index]):
        largest = l
    else:
        largest = index
    if (r < size and arr[r] > arr[largest]):
        largest = r
    if (largest != index):
        arr[largest], arr[index] = arr[index], arr[largest]
        max_heapify(arr, largest, size)

def build_max_heap(arr):
    def parent(i): return (i - 1) // 2

    length = len(arr)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(arr, index=start, size=length)
        start = start - 1

def heapsort(arr):
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, index=0, size=i)
    return arr