---
title: "LeetCode 583"
date: 2022-12-10T17:36:14+08:00
categories: ["leetcode"]
tags: ["leetcode"]
description: ""
weight:
slug: ""
draft: false
disableShare: false
cover:
    image: ""
    caption: ""
    alt: ""
    relative: false
---

### 思路

基本同最长公共子序列：[LeetCode-1143](https://superz1999.github.io/blog/posts/leetcode/leetcode-53/)，也可以直接重用LCS，因为删除的结果不就是它俩的最长公共子序列，那么删除的次数就是`word1.length() + word2.length() - 2 * lcsLen`

### 代码

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            dp[0][i] = i;
        }
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i][j - 1] + 1, dp[i - 1][j] + 1);
                }
            }
        }
        return dp[m][n];
    }
}
```

### References

---

#### 1. [两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/)
