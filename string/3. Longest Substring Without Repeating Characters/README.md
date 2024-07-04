
想像你在逛街，看到喜歡的就放進去包包。如果包包已經有重複的就照順序拿出來直到重複的沒有。並且每次計算最大值。但因為我們不能回頭，所以用 left 作為標記。

為什麼要用 set 不用 list，是因為 set 的 in 是 O(1) [1]

如果想要在優化，你可以將 index 記錄起來。也就是用 hash 的方式。[2]


## Recommend Reference Resource
[1]: https://missterhao.me/2019/02/01/%E3%80%90python%E3%80%91list-v-s-set-%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E6%AF%94%E8%BC%83-time-complexity/
[2]: https://medium.com/@bfh1104/%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98%E7%B3%BB%E5%88%97-%E8%A7%A3%E6%B1%BA-%E9%A1%8C%E7%9B%AE-longest-substring-without-repeating-characters-cbd62764b2d4