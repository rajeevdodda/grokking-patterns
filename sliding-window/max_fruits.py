# Given an array of characters where each character represents a fruit tree,
# you are given two baskets and your goal is to put maximum number of fruits in
# each basket. The only restriction is that each basket can have only one
# type of fruit.


# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']


# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']


def fruits_into_basket(string: str) -> int:
    window_start = 0
    fruit_frequency = {}
    max_lenth = 0

    for window_end in range(len(string)):
        right_fruit = string[window_end]
        fruit_frequency[right_fruit] = fruit_frequency.get(right_fruit, 0) + 1

        while len(fruit_frequency) > 2:
            left_fruit = string[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1
        max_lenth = max(max_lenth, window_end-window_start + 1)
    return max_lenth


print(fruits_into_basket(['A', 'B', 'C', 'A', 'C']))
print(fruits_into_basket(['A', 'B', 'C', 'B', 'B', 'C']))
