class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # 遍尋第一個
        # 每個都遍尋
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



# Below is sorted practice

# list_a = [1,1,1,0]
# list_b = [1,1,0,0]

# list_combine = [list_a, list_b]
# print(list_combine)

# print(sorted(list_combine))

# # 數字列表
# print(sorted([[1, 2], [1, 1], [1, 3]]))
# # 輸出: [[1, 1], [1, 2], [1, 3]]

# # 字符串列表
# print(sorted(['apple', 'banana', 'Apple']))
# # 輸出: ['Apple', 'apple', 'banana']  (大寫字母在小寫字母之前)

# list_sorted = sorted(range(len(list_combine)), key=lambda i: list_combine[i])
# print(list_sorted)