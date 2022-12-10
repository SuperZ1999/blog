---
title: "LeetCode 494"
date: 2022-12-10T23:32:55+08:00
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

有三种思路：

#### 递归思路

findTargetSumWays(nums, i, remain) = findTargetSumWays(nums, i + 1, remain - nums[i]) + findTargetSumWays(nums, i + 1, remain + nums[i])，直接看代码

#### 回溯思路

经典回溯问题，套模板即可

#### 动态规划

这道题还可以转换为子集划分问题，如果我们把 `nums` 划分成两个子集 `A` 和 `B`，分别代表分配 `+` 的数和分配 `-` 的数，那么他们和 `target` 存在如下关系：

```python
sum(A) - sum(B) = target
sum(A) = target + sum(B)
sum(A) + sum(A) = target + sum(B) + sum(A)
2 * sum(A) = target + sum(nums)
```

综上，可以推出 `sum(A) = (target + sum(nums)) / 2`，也就是把原问题转化成：**`nums` 中存在几个子集 `A`，使得 `A` 中元素的和为 `(target + sum(nums)) / 2`**？这就是一个子集背包问题了，直接套模板即可，详见思想篇章

### 代码

#### 递归解法

```java
class Solution {
    private int findTargetSumWays(int[] nums, int i, int remain) {
        if (i == nums.length) {
            if (remain == 0) {
                return 1;
            }
            return 0;
        }
        return findTargetSumWays(nums, i + 1, remain - nums[i]) + findTargetSumWays(nums, i + 1, remain + nums[i]);
    }

    public int findTargetSumWays(int[] nums, int target) {
        // 递归解法
        return findTargetSumWays(nums, 0, target);
    }
}
```

#### 回溯解法

```java
class Solution {
    private int count = 0;

    private void backtrack(int[] nums, int i, int remain) {
        if (i == nums.length) {
            if (remain == 0) {
                count++;
            }
            return;
        }
        remain -= nums[i];
        backtrack(nums, i + 1, remain);
        remain += nums[i];

        remain += nums[i];
        backtrack(nums, i + 1, remain);
        remain -= nums[i];
    }

    public int findTargetSumWays(int[] nums, int target) {
        // 回溯解法
        backtrack(nums, 0, target);
        return count;
    }
}
```

#### 子集背包解法

```java
// 原版
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        // 动态规划(子集背包问题)
        int n = nums.length, sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }
        if (Math.abs(target) > sum || (sum + target) % 2 == 1) {
            return 0;
        }
        sum = (sum + target) / 2;
        int[][] dp = new int[n + 1][sum + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= sum; j++) {
                if (j < nums[i - 1]) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]];
                }
            }
        }
        return dp[n][sum];
    }
}

// 优化空间复杂度
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        // 动态规划(子集背包问题)
        int n = nums.length, sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }
        if (Math.abs(target) > sum || (sum + target) % 2 == 1) {
            return 0;
        }
        sum = (sum + target) / 2;
        int[] dp = new int[sum + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = sum; j >= 0; j--) {
                if (j >= nums[i - 1]) {
                    dp[j] = dp[j] + dp[j - nums[i - 1]];
                }
            }
        }
        return dp[sum];
    }
}
```

### References

---

#### 1. [目标和](https://leetcode.cn/problems/target-sum/)
