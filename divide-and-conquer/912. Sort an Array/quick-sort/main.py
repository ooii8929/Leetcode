class Solution(object):

    
    def sortArray(self, nums):
        
        def quickSort(nums):
            partition(nums, 0, len(nums)-1)

        def partition (arr, l_b , r_b):
            if l_b > r_b: return # 如果 l_b 跟 r_b 交叉，代表 arr 剩下一格，不需計算
            # print(l_b, r_b)
            # print(arr)
            # 確認我要設定的邊界 l_b r_b(Left/Right Boundary)
            l_index = l_b
            r_index = r_b

            mid = (l_b + r_b) // 2
            pivot_candidates = [arr[l_b], arr[mid], arr[r_b]]
            pivotNumber = sorted(pivot_candidates)[1]
            # # print("pivotIndex", pivotIndex)
            # pivotNumber = arr[pivotIndex]

            # # 最右邊當 pivot
            # arr[pivotIndex] , arr[r_b] = arr[r_b], arr[pivotIndex]

            # r_index -= 1 # 最右邊給 pivotNumber

            # Sorted
            while l_index < r_index: # 一直查找，直到左右 index 遇到。這邊 = 要注意，因為我們要確保 l_index 是指向 > pivot 的。r_index 有可能同時停在<pivot 上
                if arr[l_index] < pivotNumber: # l 要小於 pivot，若符合，則 index 往右走
                    l_index += 1
                elif arr[r_index] > pivotNumber: # r 要大於等於 pivot，若符合，則 index 往左走
                    r_index -= 1
                else: # when l_i 指向的值大於 pivotNumber & r_i 指向的值小於 pivotNumber, swap
                    arr[l_index] , arr[r_index] =  arr[r_index], arr[l_index]
                    l_index += 1 # swap 後 index 往後走
                    r_index -= 1


            # # 查找完了， r_b 左手邊全部排序完，將他跟 l_index 交換 -> Now, l_index 左邊的值都是小於 pivotNum, r_index 的右邊的值都是大於 pivotNum
            # arr[l_index] , arr[r_b] =  arr[r_b], arr[l_index]
            # print("After partition", arr)
            # 因為 l_index 左邊跟右邊都還要再繼續排序，所以呼叫 partition
            partition(arr, l_b, l_index-1)
            partition(arr, l_index+1, r_b)
        quickSort(nums)
        return nums