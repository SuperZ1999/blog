---
title: "LeetCode 461"
date: 2022-12-27T20:22:01+08:00
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

先将x和y异或，再运用x & (x - 1)去除x最右侧的1（即Brian Kernighan算法），即可统计1的数目

### 代码

```java
class Solution {
    public int hammingDistance(int x, int y) {
        int z = x ^ y, res = 0;
        while (z != 0) {
            z = z & (z - 1);
            res++;
        }
        return res;
    }
}
```

### References

---

