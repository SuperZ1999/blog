---
title: "LeetCode 704"
date: 2022-09-24T16:18:38+08:00
tags: ["leetcode"]
draft: false
---

### 思路

经典二分查找，不解释

详见：<https://labuladong.gitee.io/algo/2/20/29/>

### 我的代码

```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid -1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            }
        }

        return -1;
    }
}
```

### References

---

#### 1. [二分查找](https://leetcode.cn/problems/binary-search/)
