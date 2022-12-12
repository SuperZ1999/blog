---
title: "LeetCode 198"
date: 2022-12-12T13:51:41+08:00
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

利用动态规划的思想，dp数组里存截止到当前户最多偷到多少钱，状态转移方程为：

```java
dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i - 2]);
```

base case 为dp[0]和dp[1]为0，可以优化空间复杂度

### 代码

#### 原版

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 2];
        for (int i = 2; i < n + 2; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i - 2]);
        }
        return dp[n + 1];
    }
}
```

#### 优化空间复杂度

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int dp_i_0 = 0, dp_i_1 = 0, dp_i_2 = 0;
        for (int i = 2; i < n + 2; i++) {
            dp_i_2 = Math.max(dp_i_1, dp_i_0 + nums[i - 2]);
            dp_i_0 = dp_i_1;
            dp_i_1 = dp_i_2;

        }
        return dp_i_2;
    }
}
```

### References

---

#### 1. [打家劫舍](https://leetcode.cn/problems/house-robber/)
