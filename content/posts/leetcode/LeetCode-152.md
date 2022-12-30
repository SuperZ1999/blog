---
title: "LeetCode 152"
date: 2022-12-30T16:10:49+08:00
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

#### 暴力枚举

把所有情况都列举出来，直接看代码

#### 动态规划

这里需要构建两个dp数组，因为以当前元素结尾的乘积最大子数组不一定是由前面元素结尾的乘积最大子数组推出来的，也有可能是由乘积最小子数组推出来的，所以需要dp_min和dp_max连个数组，里面存放以当前元素结尾的乘积最小子数组和乘积最大子数组，状态转移方程为：

```java
dp_max[i] = Math.max(nums[i], Math.max(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]));
dp_min[i] = Math.min(nums[i], Math.min(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]));
```

base case为`dp_min[0] = dp_max[0] = nums[0];`，可以优化空间复杂度

### 代码

#### 暴力枚举

```java
class Solution {
    public int maxProduct(int[] nums) {
        int res = Integer.MIN_VALUE, n = nums.length;
        for (int i = 0; i < n; i++) {
            int mul = 1;
            for (int j = i; j < n; j++) {
                mul *= nums[j];
                res = Math.max(res, mul);
            }
        }
        return res;
    }
}
```

#### 动态规划

```java
class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int[] dp_min = new int[n], dp_max = new int[n];
        dp_min[0] = dp_max[0] = nums[0];
        int res = dp_max[0];
        for (int i = 1; i < n; i++) {
            dp_max[i] = Math.max(nums[i], Math.max(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]));
            dp_min[i] = Math.min(nums[i], Math.min(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]));
            res = Math.max(res, dp_max[i]);
        }
        return res;
    }
}
```

### References

---

#### 1. [乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/)
