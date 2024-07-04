# Problem 1 - Bubble sort
def bubble_sort(sequence):
    # Write your bubble sort code here.
    seq_len = len(sequence)
    for i in range(seq_len):
      for j in range(0, seq_len - i - 1):
        if sequence[j] > sequence[j+1]:
          sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    print(sequence)
    return sequence

assert bubble_sort([5, 1, 3, 2, 4]) == [1, 2, 3, 4, 5]