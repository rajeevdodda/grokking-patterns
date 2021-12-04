# Given a string, find the length of the longest substring in it with no more
# than K distinct characters.


# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters
# is "araa".


def longest_substring_with_k_distinct(string: str, k: int):
    max_length = 0
    hash_map = {}
    windows_start = 0

    for window_end in range(len(string)):
        hash_map[string[window_end]] = hash_map.get(string[window_end], 0) + 1

        while len(hash_map) > k:
            hash_map[string[windows_start]] -= 1
            if hash_map[string[windows_start]] == 0:
                del hash_map[string[windows_start]]

            windows_start += 1
        max_length = max(max_length, window_end - windows_start + 1)
    print(max_length)


longest_substring_with_k_distinct("arrai", 2)
longest_substring_with_k_distinct("arraci", 1)
longest_substring_with_k_distinct("cbbebi", 3)
