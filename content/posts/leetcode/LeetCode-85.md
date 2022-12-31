---
title: "LeetCode 85"
date: 2022-12-31T12:00:50+08:00
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

#### 动态规划

构造两个dp数组，分别存放当前元素上面有几个连续的1和左边有几个连续的1，状态转移方程为：

```java
dp_left[i][j] = dp_left[i][j - 1] + 1;
dp_up[i][j] = dp_up[i - 1][j] + 1;
```

base case为第一行和第一列，怎么根据这两个dp数组计算面积才是重点，可以将竖着连续的1看成一个个柱体，然后把当前遍历的元素当成矩阵的右下角，从当前元素往左遍历，同时根据柱体的高度，计算面积，取面积最大值即可

#### 单调栈

感觉没什么看的必要，没看

### 代码

#### 动态规划

```java
class Solution {
    public int maximalRectangle(char[][] matrix) {
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
                    res = Math.max(res, left * up);
                }
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [最大矩形](https://leetcode.cn/problems/maximal-rectangle/)
