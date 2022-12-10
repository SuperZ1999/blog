---
title: "LeetCode 416"
date: 2022-12-10T22:02:28+08:00
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

其实就是背包问题，直接套背包问题模板，构造二维dp数组，dp\[i\]\[w\] 的定义如下：对于前 i 个物品，当前背包的容量为 w，这种情况下 dp\[i\]\[w\]表示能否将该背包装满。base case是第一列取值为true，可以优化空间复杂度，但是要注意j需要倒着遍历

### 代码

#### 原版

```java
class Solution {
    public boolean canPartition(int[] nums) {
        int n = nums.length, sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }
        if (sum % 2 != 0) {
            return false;
        }
        boolean[][] dp = new boolean[n + 1][sum / 2 + 1];
        for (int i = 0; i <= n; i++) {
            dp[i][0] = true;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sum / 2; j++) {
                if (j < nums[i - 1]) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
                }
            }
        }
        return dp[n][sum / 2];
    }
}
```

#### 优化空间复杂度

```java
class Solution {
    public boolean canPartition(int[] nums) {
        int n = nums.length, sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }
        if (sum % 2 != 0) {
            return false;
        }
        boolean[] dp = new boolean[sum / 2 + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = sum / 2; j >= 1; j--) {
                if (j >= nums[i - 1]) {
                    dp[j] = dp[j] || dp[j - nums[i - 1]];
                }
            }
        }
        return dp[sum / 2];
    }
}
```

### References

---

#### 1. [分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)
