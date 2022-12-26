---
title: "LeetCode 41"
date: 2022-12-26T19:35:57+08:00
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

原地哈希即可，将1-n的数字放在索引0-n-1里面，这样最后再遍历一遍，不满足这个规则的就是缺失的第一个正数

### 代码

```java
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length, i = 0;
        while (i < n) {
            if (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                swap(nums, i, nums[i] - 1);
            } else {
                i++;
            }
        }
        for (int j = 0; j < n; j++) {
            if (nums[j] != j + 1) {
                return j + 1;
            }
        }
        return n + 1;
    }

    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
```

### References

---

#### 1. [缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/)
