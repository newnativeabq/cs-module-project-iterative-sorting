"""
Linear Search
"""


def _get_index(arr, item):
    for index, val in enumerate(arr):
        if val == item:
            return index


def linear_search(arr, item):
    if item in arr:
        return _get_index(arr, item)
    else:
        return -1



if __name__ == "__main__":
    arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
    arr2 = []

    print(linear_search(arr1, -6))