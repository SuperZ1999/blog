---
title: "LeetCode 300"
date: 2022-12-09T19:57:21+08:00
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

两种解法：

#### 动态规划

利用动态规划的思想，y=f(x)的x是数组的索引，y是以这个索引的元素结尾的最长递增子序列的长度，选择为x之前所有元素的索引，base case为f(0) = 1，具有最优子结构，状态转移方程为f(x) = ....(懒得写了)，会有重叠子问题所以用dp数组记录，无法优化空间复杂度

#### 动态规划+二分查找

没看懂，也不重要，以后再说吧 	// TODO

### 代码

#### 动态规划

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length, res = 1;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

### References

---

#### 1. [最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)
