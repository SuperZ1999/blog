---
title: "LeetCode 136"
date: 2022-12-18T23:20:45+08:00
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

由于一个数和它本身做异或运算结果为 0，即 `a ^ a = 0`；一个数和 0 做异或运算的结果为它本身，即 `a ^ 0 = a`。那么这道题将所有数异或就得到了结果，在这种场景下可以认为两个相同的数异或后就抵消了

### 代码

```java
class Solution {
    public int singleNumber(int[] nums) {
        int len = nums.length, result = 0;
        for (int i = 0; i < len; i++) {
            result ^= nums[i];
        }
        return result;
    }
}
```

### References

---

#### 1. [只出现一次的数字](https://leetcode.cn/problems/single-number/)
