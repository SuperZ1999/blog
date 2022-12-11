---
title: "LeetCode 174"
date: 2022-12-11T14:42:53+08:00
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

与[LeetCode-64](https://blog.zhangmengyang.tk/posts/leetcode/leetcode-64/)类似，只不过dp数组中dp\[i\]\[j\]的定义是从 grid\[i\]\[j\] 到达终点（右下角）所需的最少生命值

### 代码

```java
class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length, n = dungeon[0].length;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            dp[i][n] = Integer.MAX_VALUE;
        }
        for (int i = 0; i < m; i++) {
            dp[i][n] = Integer.MAX_VALUE;
        }
        for (int i = 0; i < n; i++) {
            dp[m][i] = Integer.MAX_VALUE;
        }
        dp[m - 1][n - 1] = dungeon[m - 1][n - 1] >= 0 ? 1 : -dungeon[m - 1][n - 1] + 1;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i != m - 1 || j != n - 1) {
                    int temp = Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
                    dp[i][j] = temp > 0 ? temp : 1;
                }
            }
        }
        return dp[0][0];
    }
}
```

### References

---

#### 1. [地下城游戏](https://leetcode.cn/problems/dungeon-game/)
