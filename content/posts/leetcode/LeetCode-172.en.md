---
title: "LeetCode 172"
date: 2022-12-19T14:25:57+08:00
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

其实求阶乘结果有几个零就是求阶乘式子里可以分解出来几个因数5，其实就是n/5 + n/25 + n/125 + ....

### 代码

```java
class Solution {
    public int trailingZeroes(int n) {
        int res = 0, divisor = 5;
        while (divisor <= n) {
            res += n / divisor;
            divisor *= 5;
        }
        return res;
    }
}
```

### References

---

#### 1. [阶乘后的零](https://leetcode.cn/problems/factorial-trailing-zeroes/)
