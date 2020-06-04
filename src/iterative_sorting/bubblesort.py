"""
Bubble Sort
"""


def _swap(x1, x2):
    return x2, x1


def _forward_pass(x: list):
    swaps = 0
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = _swap(x[i], x[i + 1])
            swaps += 1
    return swaps



def bubble_sort(x: list):
    temp = x.copy()
    swaps = _forward_pass(temp)

    while swaps > 0:
        swaps = _forward_pass(temp)

    return temp



if __name__ == "__main__":
    test_list = [7, 2, 4, 3, 4, 6]

    print(bubble_sort(test_list))