---
title: "LeetCode 1143"
date: 2022-12-10T17:18:32+08:00
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

利用动态规划的思想，dp数组里存s1[0...i]和s2[0...j]的最长公共子序列，如果s1[i]==s2[j]，dp\[i\]\[j\]由dp\[i-1\]\[j-1\]+1得来，否则dp\[i\]\[j\]由max(dp\[i\]\[j-1\], dp\[i-1\]\[j\])得来，base case是dp\[0\]\[...\]和dp\[...\]\[0\]为0，可以优化空间复杂度

### 代码

```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][n];
    }
}
```

### References

---

#### 1. [最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)
