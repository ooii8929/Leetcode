# 入門
這題是 easy，要簡單也很簡單，iterater list 內的值，看是加總或是逐個比較，然後將 index 同步帶入就可以解。

## 暴力解法
1. 每個遞迴將 1 加總，並補上index。額外存成 list(tuple)
2. list(tuple) 做排序
```
    record = []
    for i in range(len(mat)):
        num = 0
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                num += 1
        record.append((num,i))
    print(record)
    sorted_records = sorted(record)

    indices = [record[1] for record in sorted_records]

    return indices[:k]
```

## 進階
這邊有個 python 可以學習的重點，就是 sorted 在 list 的應用。

假設 lists 為 a vector of vectors，也就是 [[1, 2], [1, 1], [1, 3]] list內為多個 list 的形式，當你使用 sorted(lists) 會逐一比較每個 item 並進行排序。根據這個特性我們就可以寫出 sorted(題目給的list)，但因為最終要回傳index，所以我們可以在最後 mutate index

```
           index
            ||
            \/
[1,1,0,0,0, 0],
[1,1,1,1,0, 1],
[1,0,0,0,0, 2],    
[1,1,0,0,0, 3],
[1,1,1,1,1, 4]

list_sorted = sorted(range(len(list_combine)), key=lambda i: list_combine[i])
```
ref: [@arnabsen1729 Solution](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/solutions/1201679/c-python3-no-heap-no-bs-simple-sort-99-20/)

另外一種解法一樣是使用此特性，只是不使用 mutate，而是直接把 index 帶入 tuple
```
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    m = len(mat)
    rows = sorted(range(m), key=lambda i: (mat[i], i))
    del rows[k:]
    return rows
```

ref: [@rcomesan Solution](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/solutions/1201679/c-python3-no-heap-no-bs-simple-sort-99-20/comments/1272679)

這樣的複雜度是 O(m * n * log(m))，O(m * log(m))的m是題目給的i rows 數量，然後n是題目的j的長度
空間複雜度是O(m)，額外創建了m的rows

# Ref
1. [1337. The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/)

