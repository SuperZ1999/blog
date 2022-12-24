---
title: "LeetCode 11"
date: 2022-12-23T14:01:43+08:00
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

利用双指针的思想，每次移动比较小的那个，同时维护左右指针之间的盛水最大值即可

### 代码

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int res = 0;
        while (left < right) {
            int area = Math.min(height[left], height[right]) * (right - left);
            res = Math.max(res, area);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)
