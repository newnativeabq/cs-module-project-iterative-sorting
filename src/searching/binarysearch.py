"""
Binary Search
"""


def _test_sorted(arr):
    ## Dummy function.  Implement if time.
    return True


def _average(arr):
    return int(sum(arr)/len(arr))


def _get_midpoint(mini, maxi):
    return _average([mini, maxi])


def _get_left(mini, maxi, mid):
    return mini, mid 

def _get_right(mini, maxi, mid):
    return mid, maxi


def binary_search(arr, item, mini=None, maxi=None):
    if mini is None:
        mini = 0
    if maxi is None:
        maxi = len(arr)

    try:
        if arr[mini] == item:
            return mini
    except:
        print('Index out of bounds')
        return -1

    mid = _get_midpoint(mini, maxi)

    if _test_sorted(arr):
        if item < arr[mid]:
            mini, maxi = _get_left(mini, maxi, mid)
        elif item > arr[mid]:
            mini, maxi = _get_right(mini, maxi, mid)
        elif item == arr[mid]:
            return mid

        return binary_search(arr=arr, item=item, mini=mini, maxi=maxi)
        




if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = []

    print(binary_search(arr1, 1))