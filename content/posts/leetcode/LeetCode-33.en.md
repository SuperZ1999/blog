---
title: "LeetCode 33"
date: 2023-01-07T12:10:37+08:00
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

利用二分查找的思路，每次选出一个中间元素，对于这个中间元素来说，左边和右边必有一个有序序列，那么我们可以分情况讨论，如果左边是有序序列，那么`target < nums[mid] && target >= nums[0]`的情况target一定在左边，否则在右边，以此类推直到找到target

### 代码

#### 官方解答

```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target == nums[mid]) {
                return mid;
            }
            if (nums[mid] >= nums[0]) {
                if (target < nums[mid] && target >= nums[0]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (target > nums[mid] && target < nums[0]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}
```

#### 我的解法

```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target == nums[mid]) {
                return mid;
            } else if (target > nums[mid]) {
                if (target >= nums[0]) {
                    if (nums[mid] < nums[0]) {
                        right = mid - 1;
                    } else {
                        left = mid + 1;
                    }
                } else {
                    left = mid + 1;
                }
            } else if (target < nums[mid]) {
                if (target >= nums[0]) {
                    right = mid - 1;
                } else {
                    if (nums[mid] < nums[0]) {
                        right = mid - 1;
                    } else {
                        left = mid + 1;
                    }
                }
            }
        }
        return -1;
    }
}
```

### References

---

#### 1. [搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)
