class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 總次數 
        result = 0
        # 目前加總
        current_sum = 0
        prefix_sum = {0:1}
        # for loop
        for n in nums:
            # 得到新的值 n
            current_sum += n
            if current_sum-k in prefix_sum:

                # prefix 有結合的加起來
                result += prefix_sum[current_sum-k]

            # prefix_sum ++
            prefix_sum[current_sum] = prefix_sum.get(current_sum,0) + 1
        print(prefix_sum)
        return result
