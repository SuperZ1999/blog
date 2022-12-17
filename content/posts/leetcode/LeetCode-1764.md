---
title: "LeetCode 1764"
date: 2022-12-17T23:38:35+08:00
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

用双指针逐行比较即可，可以用KMP优化

### 代码

```java
class Solution {
    private boolean isMatch(int[] group, int[] nums, int start) {
        if (group.length > nums.length - start) {
            return false;
        }
        for (int i = 0; i < group.length; i++) {
            if (group[i] != nums[start + i]) {
                return false;
            }
        }
        return true;
    }

    public boolean canChoose(int[][] groups, int[] nums) {
        int i = 0, k = 0;
        while (i < groups.length && k < nums.length){
            if (isMatch(groups[i], nums, k)) {
                k += groups[i].length;
                i++;
            } else {
                k++;
            }
        }
        return i == groups.length;
    }
}
```

### References

---

#### 1. [通过连接另一个数组的子数组得到一个数组](https://leetcode.cn/problems/form-array-by-concatenating-subarrays-of-another-array/)
