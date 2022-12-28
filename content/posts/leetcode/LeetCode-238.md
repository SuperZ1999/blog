---
title: "LeetCode 238"
date: 2022-12-28T22:43:11+08:00
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

利用前缀和的思想，从左往右遍历一遍，从右往左遍历一遍同时记录该数组的左右乘积，每个元素的左乘积乘以右乘积就是答案，还可以优化空间复杂度，把返回数组res当成左乘积数组，同时用一个变量充当右乘积，详见代码

### 代码

#### 前缀和

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] L = new int[n], R = new int[n];
        L[0] = 1;
        for (int i = 1; i < n; i++) {
            L[i] = L[i - 1] * nums[i - 1];
        }
        R[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            R[i] = R[i + 1] * nums[i + 1];
        }
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = L[i] * R[i];
        }
        return res;
    }
}
```

#### 前缀和+空间复杂度优化

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        res[0] = 1;
        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }
        int R = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] = res[i] * R;
            R *= nums[i];
        }
        return res;
    }
}
```

### References

---

#### 1. [除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/)
