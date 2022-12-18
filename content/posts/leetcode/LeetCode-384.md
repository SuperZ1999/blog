---
title: "LeetCode 384"
date: 2022-12-18T20:54:17+08:00
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

随机算法问题，使用洗牌算法即可，详见思想篇章

### 代码

```java
class Solution {
    private int[] nums;
    private Random random;

    public Solution(int[] nums) {
        this.nums = nums;
        this.random = new Random();
    }
    
    public int[] reset() {
        return nums;
    }
    
    public int[] shuffle() {
        int n = nums.length;
        int[] copy = Arrays.copyOf(nums, n);
        for (int i = 0; i < n; i++) {
            int r = random.nextInt(n - i) + i;
            int temp = copy[i];
            copy[i] = copy[r];
            copy[r] = temp;
        }
        return copy;
    }
}
```

### References

---

#### 1. [打乱数组](https://leetcode.cn/problems/shuffle-an-array/)
