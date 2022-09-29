---
title: "LeetCode 303"
date: 2022-09-25T22:41:54+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用前缀和的思想轻松秒杀，需要注意在preSum中，第n + 1个元素存的是nums前n个元素的和，整体往后挪一位

### 我的代码

```java
class NumArray {
    int[] preSum;

    public NumArray(int[] nums) {
        preSum = new int[nums.length + 1];

        for (int i = 1; i < preSum.length; i++) {
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }
    }
    
    public int sumRange(int left, int right) {
        return preSum[right + 1] - preSum[left];
    }
}
```

### References

---

#### 1. [区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/)
