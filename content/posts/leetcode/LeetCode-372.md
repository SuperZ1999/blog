---
title: "LeetCode 372"
date: 2022-12-19T20:38:10+08:00
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

幂可以转换为以下形式：

![img](https://labuladong.gitee.io/algo/images/superPower/formula1.png)

这样就可以运用递归了，至于模幂运算运用`(a * b) % k = ((a % k) * (b % k)) % k`即可，详见思想篇章

还可以运用高效求幂，详见思想

### 代码

#### 基本版

```java
class Solution {
    private int base = 1337;

    public int superPow(int a, int[] b) {
        return superPow(a, b, b.length);
    }

    private int superPow(int a, int[] b, int len) {
        if (len == 0) {
            return 1;
        }
        int last = b[len - 1];
        int p1 = myPow(a, last);
        int p2 = myPow(superPow(a, b, len - 1), 10);
        return (p1 * p2) % base;
    }

    private int myPow(int a, int b) {
        a %= base;
        int res = 1;
        while (b != 0) {
            res = (res * a) % base;
            b--;
        }
        return res;
    }
}
```

#### 高效版

```java
class Solution {
    private int base = 1337;

    public int superPow(int a, int[] b) {
        return superPow(a, b, b.length);
    }

    private int superPow(int a, int[] b, int len) {
        if (len == 0) {
            return 1;
        }
        int last = b[len - 1];
        int p1 = myPow(a, last);
        int p2 = myPow(superPow(a, b, len - 1), 10);
        return (p1 * p2) % base;
    }

    private int myPow(int a, int b) {
        if (b == 0) {
            return 1;
        }
        a %= base;

        if (b % 2 == 1) {
            return (a * myPow(a, b - 1)) % base;
        } else {
            int res = myPow(a, b / 2);
            return (res * res) % base;
        }
    }
}
```

### References

---

#### 1. [超级次方](https://leetcode.cn/problems/super-pow/)
