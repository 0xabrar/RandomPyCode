def merge_sort(A):
    # pre: A is a list of numbers (or empty)
    if len(A) < 2:
        return A

    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    return merge(left, right)


def merge(left, right):

    final = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1

    final.extend(left[i:])
    final.extend(right[j:])
    return final
