---
title: "LeetCode 75"
date: 2023-02-24T17:27:26+08:00
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

利用双指针的思想即可，左指针指向0的最后一个的后一个，右指针指向2的第一个的前一个，然后遍历数组同时维护左右指针即可，注意点：

- 除了刚开始的时候，左指针指向的不可能是0，因为如果是0，那么遍历的时候就肯定遍历到它了，那么就会放到左边，而不是出现在这里
- 交换右边的时候，i不能加一，因为交换的数字有可能是0或2，要重复判断

### 代码

```java
class Solution {
    public void sortColors(int[] nums) {
        int left = 0, right = nums.length - 1;
        for (int i = 0; i <= right; i++) {
            if (nums[i] == 0) {
                nums[i] = nums[left];
                nums[left] = 0;
                left++;
            }
            if (nums[i] == 2) {
                nums[i] = nums[right];
                nums[right] = 2;
                right--;
                i--;
            }
        }
    }
}
```

### References

---

#### 1. [颜色分类](https://leetcode.cn/problems/sort-colors/)
