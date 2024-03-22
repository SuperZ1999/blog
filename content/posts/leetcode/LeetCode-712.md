---
title: "LeetCode 712"
date: 2022-12-10T20:40:33+08:00
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

利用动态规划的思想，同[LeetCode-583](https://superz1999.github.io/blog/posts/leetcode/leetcode-583/)，只不过不是计算删除操作数，而是删除的ASCII码

### 代码

```java
class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            dp[0][i] = dp[0][i - 1] + s2.charAt(i - 1);
        }
        for (int i = 1; i <= m; i++) {
            dp[i][0] = dp[i - 1][0] + s1.charAt(i - 1);
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i][j - 1] + s2.charAt(j - 1), dp[i - 1][j] + s1.charAt(i - 1));
                }
            }
        }
        return dp[m][n];
    }
}
```

### References

---

#### 1. [两个字符串的最小ASCII删除和](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/)
