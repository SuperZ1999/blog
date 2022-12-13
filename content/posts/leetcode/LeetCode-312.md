---
title: "LeetCode 312"
date: 2022-12-13T14:15:00+08:00
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

利用动态规划的思想，**`dp[i][j] = x`表示，戳破气球`i`和气球`j`之间（开区间，不包括`i`和`j`）的所有气球，可以获得的最高分数为`x`**。状态转移方程为：

```java
for (int k = i + 1; k < j; k++) {
    dp[i][j] = Math.max(dp[i][j], dp[i][k] + dp[k][j] + points[i] * points[j] * points[k]);
}
```

base case和遍历顺序如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibkIz0MVqdGVd9E2bQKH5gM83O0pzWrWb4jBL12WCXJdmbwftblZo5P87r2ibrr7SxUByVguBiaguACg2BnAaNiag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

可以优化空间复杂度

### 代码

```java
class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length;
        int [] points = new int[n + 2];
        for (int i = 0; i < n; i++) {
            points[i + 1] = nums[i];
        }
        points[0] = points[n + 1] = 1;
        int[][] dp = new int[n + 2][n + 2];
        for (int i = n; i >= 0; i--) {
            for (int j = i + 1; j < n + 2; j++) {
                for (int k = i + 1; k < j; k++) {
                    dp[i][j] = Math.max(dp[i][j], dp[i][k] + dp[k][j] + points[i] * points[j] * points[k]);
                }
            }
        }
        return dp[0][n + 1];
    }
}
```

### References

---

#### 1. [戳气球](https://leetcode.cn/problems/burst-balloons/)
