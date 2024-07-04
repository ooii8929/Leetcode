class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        left = 0
        char_set = set()
        for right in range(len(s)):
            current_char = s[right]
            while current_char in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(current_char)
            right += 1
            max_length = max(max_length, len(char_set))
        return max_length
        

# 測試案例
def test_length_of_longest_substring():
    solution = Solution()
    
    # 測試案例 1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    print("測試案例 1 通過")
    
    # 測試案例 2
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    print("測試案例 2 通過")
    
    # 測試案例 3
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    print("測試案例 3 通過")
    
    # 測試案例 4
    assert solution.lengthOfLongestSubstring("") == 0
    print("測試案例 4 通過")
    
    # 測試案例 5
    assert solution.lengthOfLongestSubstring("au") == 2
    print("測試案例 5 通過")
    
    # 測試案例 6
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    print("測試案例 6 通過")
    
    # 測試案例 7
    assert solution.lengthOfLongestSubstring("anviaj") == 5
    print("測試案例 7 通過")

# 執行測試
test_length_of_longest_substring()