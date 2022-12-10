---
title: "LeetCode 53"
date: 2022-12-10T15:39:44+08:00
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

dp数组里放以该元素结尾的最大子数组和，可以由前面那个元素推出来，base case是dp[0] = nums[0]，可以优化空间复杂度

#### 滑动窗口

其实和动态规划一样，就是窗口里的元素和如果大于0，就扩大窗口（因为是正的加上后面的元素才有可能更大），窗口里的元素和如果小于0，就缩小窗口（因为是负的加上后面的元素只会更大），和动态规划其实一样的

#### 前缀和数组

利用前缀和数组的思想，最大子数组之和其实就是 preSum[i+1] - min(preSum[0..i])

### 代码

#### 动态规划

```java
class Solution {
    public int maxSubArray(int[] nums) {
        // 动态规划
        int n = nums.length;
        int dp_0 = nums[0], res = dp_0;
        for (int i = 1; i < n; i++) {
            dp_0 = Math.max(dp_0 + nums[i], nums[i]);
            res = Math.max(res, dp_0);
        }
        return res;
    }
}
```

#### 滑动窗口

```java
class Solution {
    public int maxSubArray(int[] nums) {
        // 滑动窗口
        int left = 0, right = 0;
        int windowSum = 0, res = Integer.MIN_VALUE;
        while (right < nums.length) {
            windowSum += nums[right];
            right++;
            res = Math.max(res, windowSum);
            while (windowSum < 0) {
                windowSum -= nums[left];
                left++;
            }
        }
        return res;
    }
}
```

#### 前缀和数组

```java
class Solution {
    public int maxSubArray(int[] nums) {
        // 前缀和数组
        int n = nums.length;
        int[] preSum = new int[n + 1];
        for (int i = 0; i < n ; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
        int minVal = Integer.MAX_VALUE, res = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            minVal = Math.min(minVal, preSum[i]);
            res = Math.max(res, preSum[i + 1] - minVal);
        }
        return res;
    }
}
```

### References

---

#### 1. [最大子数组和](https://leetcode.cn/problems/maximum-subarray/)
