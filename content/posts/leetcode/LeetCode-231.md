---
title: "LeetCode 231"
date: 2022-12-18T23:16:25+08:00
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

用 `n & (n-1)` 的技巧来判断n的二进制表示是不是只有一个1

### 代码

```java
class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        return (n & (n - 1)) == 0;
    }
}
```

### References

---

#### 1. [2 的幂](https://leetcode.cn/problems/power-of-two/)
