---
title: "LeetCode 268"
date: 2022-12-18T23:26:40+08:00
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

#### 常规思路

求[0...n]的前n项和然后减去nums的数之和，就得到了缺失的数组

#### 位运算思路

由于异或的性质，只要把所有的元素和索引做异或运算，成对儿的数字都会消为 0，只有这个落单的元素会剩下，注意需要先异或n

### 代码

#### 常规思路

```java
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        long except = (0 + n) * (n + 1) / 2;
        long sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return (int) (except - sum);
    }
}
```

#### 位运算思路

```java
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int res = n;
        for (int i = 0; i < n; i++) {
            res ^= i ^ nums[i];
        }
        return res;
    }
}
```

### References

---

#### 1. [丢失的数字](https://leetcode.cn/problems/missing-number/)
