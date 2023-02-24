---
title: "LeetCode 70"
date: 2023-02-23T23:45:19+08:00
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

三种思路：

#### 动态规划

类似于斐波那契数列，定义一个dp数组，dp[i] = j的含义是，到达第i个台阶有j种方法，那么递推公式为：

```java
dp[i] = dp[i - 2] + dp[i - 1];
```

base case为`dp[0] = dp[1] = 1`，可以优化空间复杂度，但是懒得弄了

#### 矩阵快速幂

感觉没必要看

#### 通项公式

感觉没必要看

### 代码

```java
class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n + 1];
        dp[0] = dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 2] + dp[i - 1];
        }
        return dp[n];
    }
}
```

### References

---

#### 1. [爬楼梯](https://leetcode.cn/problems/climbing-stairs/)
