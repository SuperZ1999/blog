---
title: "LeetCode 31"
date: 2023-01-06T21:53:37+08:00
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

因为是下一个排列，所以更改的元素尽量靠右，并且需要变大，那么我们可以从右往左遍历，找到右侧存在比自己大的元素的元素（找这种元素可以从左往右遍历，第一个比后面元素小的元素就是要找的元素），更改的时候需要将该元素右侧比该元素大的最小元素替换到该位置，然后后面的元素从大到小排列，以保证变大的幅度尽可能小

### 代码

```java
class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length, i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1);
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void reverse(int[] nums, int begin) {
        int left = begin, right = nums.length - 1;
        while (left < right) {
            swap(nums, left, right);
            left++;
            right--;
        }
    }
}
```

### References

---

#### 1. [下一个排列](https://leetcode.cn/problems/next-permutation/)
