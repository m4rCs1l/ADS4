def quick_sort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return arr


def comb_sort(arr):
    n = len(arr)
    step = n
    swaps = True
    while step > 1 or swaps:
        step = max(1, int(step / 1.25))
        swaps = False
        for i in range(n - step):
            j = i+step
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps = True
