---
title: "LeetCode 221"
date: 2022-12-31T14:27:39+08:00
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

两种思路：

#### 暴力解法

遍历数组，将每个元素当成正方形的左上角，并检查此时正方形的面积，计算最大值即可，代码略

#### 动态规划

同[LeetCode-85](https://superz1999.github.io/blog/posts/leetcode/leetcode-85/)，只不过85是矩形，这里是正方形，计算面积的时候注意长宽一致即可，其实也可以不用85这种思路，也可以建立dp数组，dp\[i\]\[j\] = x表示以\[i\]\[j\]元素为正方形右下角的正方形边长最长为x，状态转移方程为：

```java
dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
```

为什么状态转移方程是这样的，想象一下就知道了，base case为第一行和第一列，可以优化空间复杂度，通过动态规划计算最长边长就行了

### 代码

```java
class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[][] dp_left = new int[m + 1][n + 1], dp_up = new int[m + 1][n + 1];
        int res = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] == '0') {
                    continue;
                }
                dp_left[i][j] = dp_left[i][j - 1] + 1;
                dp_up[i][j] = dp_up[i - 1][j] + 1;
                int up = Integer.MAX_VALUE;
                for (int left = 1; left <= dp_left[i][j]; left++) {
                    up = Math.min(up, dp_up[i][j + 1 - left]);
                    if (up < left) {
                        break;
                    }
                    res = Math.max(res, left * left);
                }
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [最大正方形](https://leetcode.cn/problems/maximal-square/)
