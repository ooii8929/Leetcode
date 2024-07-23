# class Solution(object):
#     def kWeakestRows(self, mat, k):
#         """
#         :type mat: List[List[int]]
#         :type k: int
#         :rtype: List[int]
#         """
#         # 遍尋第一個
#         # 每個都遍尋
#         record = []
#         for i in range(len(mat)):
#             num = 0
#             for j in range(len(mat[i])):
#                 if mat[i][j] == 1:
#                     num += 1
#             record.append((num,i))
#         print(record)
#         sorted_records = sorted(record)

#         indices = [record[1] for record in sorted_records]

#         return indices[:k]

list_a = [1,1,1,0]
list_b = [1,1,0,0]

list_combine = [list_a, list_b]
print(list_combine)

print(sorted(list_combine))

list_sorted = sorted(range(len(list_combine)), key=lambda i: list_combine[i])
print(list_sorted)