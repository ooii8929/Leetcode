class Solution(object):
    # arr 排序
    # 切半 arr
    # arr 排序
    # ...
    # 切到不能切 合併
    # 排序比較
    # 合併
    def sortArray(self, nums): #排序
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            # Divide
            
            mid = len(nums)//2 

            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            # Conquter
            return merge(left,right)
        def merge(left, right):
            arr = []
            li = 0
            ri = 0
            while len(left) > li and len(right) > ri:
                if left[li] < right[ri]:
                    arr.append(left[li])
                    li+=1
                else:
                    arr.append(right[ri])
                    ri+=1
            while li < len(left): 
                arr.append(left[li]) 
                li+=1

            while ri < len(right): 
                arr.append(right[ri]) 
                ri+=1
            return arr
        return mergeSort(nums)

            

                