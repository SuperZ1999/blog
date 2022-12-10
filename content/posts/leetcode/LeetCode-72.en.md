---
title: "LeetCode 72"
date: 2022-12-10T15:01:28+08:00
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

利用动态规划的思想，dp数组里存*s1[0..i-1] 和 s2[0..j-1]*的编辑距离，可以由以下元素推出来：

![img](https://labuladong.gitee.io/algo/images/editDistance/4.jpg)

base case是第一行和第一列，可以优化空间复杂度但是懒得弄了

补充：具体s1是怎么转换为s2的，可以在dp数组的每个元素里补充额外的信息，详见：<https://labuladong.gitee.io/algo/3/26/75/>

### 代码

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int i = 0; i <= n; i++) {
            dp[0][i] = i;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1] + 1, Math.min(dp[i][j - 1] + 1, dp[i - 1][j] + 1));
                }
            }
        }
        return dp[m][n];
    }
}
```

### References

---

#### 1. [编辑距离](https://leetcode.cn/problems/edit-distance/)
