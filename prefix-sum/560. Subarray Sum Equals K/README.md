這題的暴力解法很明顯，就是 迴圈跑兩次，然後每個都比對後找出相加等於 k 的 sub_array。

從過去學的幾個點來思考一下，因為談到 Contiguous Subsequence(different from subsequence and contiguous subsequence)，會想考慮雙指針或是 sliding window。如果是 sliding window，雖然我可以在正數的時候，找出可以相加等於 k 的區間，假設 < K ，我可以把區間左減一個減少值。但題目有提到有負數，這會造成增加一個元素不一定會增加總和，移除一個元素也不一定會減少總和，所以不適用。

我們從頭來看一下，如果我們希望走一次（O(N)）就可以得到結果，我們可以將已經算過的數總加起來，這邊我們稱為 prefix。當我們算當前的數是否加總為 K 時，可以用當前加總 - K，看看有沒有對應的 prefix，假設有，代表之前曾經有過 prefix + current num 可以得到 K。(current_sum - k = prefix_sum)

而每次不同組合的 prefix_sum 都可能是新的 result，舉例 [1,2,1] ，則 prefix_sum 為 3 就會有 2 次[1,2] & [2,1]，所以我們要記住 count 的值
```
{“prefix_sum“:”count”}
```
## Recommend Reference Resource
[Subarray Sum Equals K - Prefix Sums - Leetcode 560 - Python](https://www.youtube.com/watch?v=fFVZt-6sgyo)