---
title: "LeetCode 509"
date: 2022-12-08T22:42:39+08:00
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

状态转移方程很简单，注意一下直接递归会有重复子问题，所以可以使用数组备份一下（其实就是dp数组），又发现只会用到每个元素的前两个元素，所以可以把数组换成前两个元素

### 代码

```java
class Solution {
    public int fib(int n) {
        if (n == 0 || n == 1) {
            return n;
        }
        int dp_i_1 = 0, dp_i_2 = 1;
        for (int i = 2; i <= n; i++) {
            int dp_i_3 = dp_i_1 + dp_i_2;
            dp_i_1 = dp_i_2;
            dp_i_2 = dp_i_3;
        }
        return dp_i_2;
    }
}
```

### References

---

#### 1. [斐波那契数](https://leetcode.cn/problems/fibonacci-number/)
