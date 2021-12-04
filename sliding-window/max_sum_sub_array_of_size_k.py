# Given an array of positive numbers and a positive number ‘k’, find the maximum
#  sum of any contiguous subarray of size ‘k’.


def max_sub_array_of_size_k(array: list, k: int):
    window_start = max_sum = current_sum = 0
    for window_end in range(len(array)):
        current_sum += array[window_end]

        while window_end - window_start > k:
            current_sum -= array[window_start]
            window_start += 1

        max_sum = max(max_sum, current_sum)

    print(max_sum)


max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], k=3)
max_sub_array_of_size_k([2, 3, 4, 1, 5], k=2)
