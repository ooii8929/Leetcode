# Problem 2 - Find second largest
def find_second_largest(sequence):
    # Write your algorithm with O(n) time complexity here.
    first = second = float("-inf")
    for i in range(len(sequence)):
      if sequence[i] > first:
        second = first
        first = sequence[i]
      elif sequence[i] > second and sequence[i] != first:
        second = sequence[i]
    return second

assert find_second_largest([3, 3, 2, 1]) == 2
assert find_second_largest([3, 3, 3, 3, 3, 2, 2, 1]) == 2
assert find_second_largest([-1, 2, 3, 5, 3, 1, 2, 4]) == 4
