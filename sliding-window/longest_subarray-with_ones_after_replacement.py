# Given an array containing 0s and 1s, if you are allowed to replace no more
# than ‘k’ 0s with 1s, find the length of the longest contiguous subarray
#  having all 1s.


def max_consecutive_ones(array: list, k: int):
    window_start = max_length = 0

    for window_end in range(len(array)):
        if array[window_end] == 0:
            k -= 1
        if k < 0:
            if array[window_start] == 0:
                k += 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    print(max_length)


max_consecutive_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)
