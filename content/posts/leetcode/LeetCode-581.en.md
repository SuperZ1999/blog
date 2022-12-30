---
title: "LeetCode 581"
date: 2022-12-30T16:50:06+08:00
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

#### 排序+检测位置不对的元素

先复制数组，然后排序，再比较排序后的数组和原数组，看看哪些位置不对即可

#### O(N)时间复杂度

由于无序子数组中最小元素的正确位置可以决定左边界，最大元素的正确位置可以决定右边界，所以遍历两次确定这两个边界就可以了，详见代码

### 代码

#### 排序+检测位置不对的元素

```java
public int findUnsortedSubarray(int[] nums) {
    int[] sortNums = Arrays.copyOf(nums, nums.length);
    Arrays.sort(sortNums);
    int left = -1, right = -2;
    for (int i = 0; i < nums.length; i++) {
        if (sortNums[i] != nums[i]) {
            if (left == -1) {
                left = i;
                right = i;
            } else {
                right = i;
            }
        }
    }
    return right - left + 1;
}
```

#### O(N)时间复杂度

```java
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length, max = Integer.MIN_VALUE, right = -2;
        for (int i = 0; i < n; i++) {
            if (nums[i] < max) {
                right = i;
            } else {
                max = nums[i];
            }
        }
        int min = Integer.MAX_VALUE, left = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] > min) {
                left = i;
            } else {
                min = nums[i];
            }
        }
        return right - left + 1;
    }
}
```

### References

---

#### 1. [最短无序连续子数组](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/)
