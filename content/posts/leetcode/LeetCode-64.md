---
title: "LeetCode 64"
date: 2022-12-11T14:03:02+08:00
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

经典动态规划问题，构造dp\[\]\[\]数组，里面存放从(0, 0)到(i, j)的最小路径，dp\[i\]\[j\]由min(dp\[i - 1\]\[j\], dp\[i\]\[j - 1\]) + grid\[i\]\[j\]得来，base case为第一行和第一列，可以优化空间复杂度

### 代码

```java
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        dp[0][0] = grid[0][0];
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }
        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i - 1] + grid[0][i];
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }
        return dp[m - 1][n - 1];
    }
}
```

### References

---

#### 1. [最小路径和](https://leetcode.cn/problems/minimum-path-sum/)
