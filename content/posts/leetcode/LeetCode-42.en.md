---
title: "LeetCode 42"
date: 2022-12-23T12:26:57+08:00
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

每个格子能装多少水取决于这个格子左边最高的格子和右边最高的格子，所以可以使用双指针，分别指向左边和右边的格子，遍历这个数组，当左边最大值小于右边最大值时就可以确定左指针的元素能装多少水，因为能装多少水取决于这个格子左边最高的格子和右边最高的格子，而左边最大值小于右边最大值，即使右边有更大的也对结果没影响，然后移动左指针，并且更新左边的最大值即可

### 代码

```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int l_max = height[left], r_max = height[right];
        int res = 0;
        while (left <= right) {
            l_max = Math.max(l_max, height[left]);
            r_max = Math.max(r_max, height[right]);
            if (l_max < r_max) {
                res += l_max - height[left];
                left++;
            } else {
                res += r_max - height[right];
                right--;
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [接雨水](https://leetcode.cn/problems/trapping-rain-water/)
