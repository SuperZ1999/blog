---
title: "LeetCode 62"
date: 2023-02-23T23:24:07+08:00
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

#### 动态规划

没这必要

#### 数学组合

这里向下向右的步数是固定的，所以这里路径的个数等于C(向右的步数或向下的步数，总步数)，求组合详见思想篇章，注意这里必须从1和n开始乘，从1和m+n-2开始乘会溢出

### 代码

```java
class Solution {
    public int uniquePaths(int m, int n) {
        long res = 1;
        for (int i = n, j = 1; j < m; i++, j++) {
            res = res * i / j;
        }
        return (int) res;
    }
}
```

### References

---

#### 1. [不同路径](https://leetcode.cn/problems/unique-paths/)
