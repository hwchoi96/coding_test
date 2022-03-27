def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        p = (left + right) // 2

        if arr[p] == target:
            return p
        elif arr[p] > target:
            right = p - 1
        else:
            left = p + 1
    return None

print(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 7))
