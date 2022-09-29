---
title: "LeetCode 34"
date: 2022-09-25T00:24:53+08:00
tags: ["leetcode"]
draft: false
---

### 思路

进阶版二分查找，寻找target的左右边界，在进阶版二分查找的二分阶段根据左边界或右边界的特征，选择合适的二分条件即可，来两次二分查找，分别查找左边界或右边界即可，详见LeetCode-note

### 我的代码

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0) {
            return new int[]{-1, -1};
        }

        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        if (nums[left] != target) {
            return new int[]{-1, -1};
        }
        int[] ans = new int[2];
        ans[0] = left;

        left = 0; right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        ans[1] = left;

        return ans;
    }
}
```

### References

---

#### 1. [在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)
