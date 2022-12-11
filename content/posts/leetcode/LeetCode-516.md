---
title: "LeetCode 516"
date: 2022-12-11T20:18:17+08:00
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

利用动态规划的思想，dp数组里存s[i...j]的最长回文子序列，状态转移方程如下：

```java
if (s.charAt(j) == s.charAt(j + i)) {
    dp[j][j + i] = 2 + dp[j + 1][j + i - 1];
} else {
    dp[j][j + i] = Math.max(dp[j + 1][j + i], dp[j][j + i - 1]);
}
```

base case为如下的0和1：

![img](https://pic.leetcode-cn.com/1600677121-aGPcPu-file_1600677121456)

可以斜着遍历，也可以从下往上遍历，可以优化空间复杂度

### 代码

```java
class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n - i; j++) {
                if (s.charAt(j) == s.charAt(j + i)) {
                    dp[j][j + i] = 2 + dp[j + 1][j + i - 1];
                } else {
                    dp[j][j + i] = Math.max(dp[j + 1][j + i], dp[j][j + i - 1]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
```

### References

---

#### 1. [最长回文子序列](https://leetcode.cn/problems/longest-palindromic-subsequence/)
