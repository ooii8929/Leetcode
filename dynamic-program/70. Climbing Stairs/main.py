class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[n] = dp[n-1]+dp[n-2] 第n階有 dp[n-1]種方式跟dp[n-2]種方式
        # if n < 3，n 的數量固定。2階有 0, 2 跟 1,1
        # def dp(i):
        #     if i < 3: return i
        #     return dp(i-1)+dp(i-2)
        
        # return dp(n)

        # 前者太耗效能，1->2, 2->4 是2^n 次方。用 list 紀錄算過的值
        # 一個一個加上去

        # 由終而始，由始算終
        if n > 2:
            lis = [1,2]
            for i in range(2,n):
                lis.append(lis[i-1] + lis[i-2])
            print(lis)
            return lis[n-1]
        else:
            return n


