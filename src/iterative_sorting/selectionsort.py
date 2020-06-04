"""
Selection Sort
"""

def _find_min(x, i_start):
    min_val = min(x[i_start:])
    for index, item in enumerate(x[i_start:]):
        if item == min_val:
            print('Found', index, min_val)
            return index + i_start


def _swap(x1, x2):
    return x2, x1


def selection_sort(x: list) -> list:
    temp = x.copy()
    for i in range(len(temp)):
        min_index = _find_min(temp, i)
        if min_index is not None:
            temp[i], temp[min_index] = _swap(temp[i], temp[min_index])

    return temp



if __name__ == "__main__":
    test_list = [7, 2, 4, 3, 4, 6]
    print(selection_sort(test_list))