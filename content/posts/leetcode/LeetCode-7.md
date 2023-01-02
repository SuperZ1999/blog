---
title: "LeetCode 7"
date: 2023-01-02T15:03:48+08:00
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

每次取最后一位然后加到res上即可，需要注意这里的判断是否溢出：

```java
if (res > Integer.MAX_VALUE / 10 || res == Integer.MAX_VALUE / 10 && num > 7) {
    return 0;
}
if (res < Integer.MIN_VALUE / 10 || res == Integer.MIN_VALUE / 10 && num < -8) {
    return 0;
}
```

但判断是否溢出还可以优化，res每次更新后除10，然后跟上一次的res比较一下，如果不相等，就是溢出：

```java
int pre = res;
res = res * 10 + num;
if (res / 10 != pre) {
    return 0;
}
```

并且需要知道负数取余得到的结果还是负数

### 代码

#### 基本版

```java
class Solution {
    public int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int num = x % 10;
            if (res > Integer.MAX_VALUE / 10 || res == Integer.MAX_VALUE / 10 && num > 7) {
                return 0;
            }
            if (res < Integer.MIN_VALUE / 10 || res == Integer.MIN_VALUE / 10 && num < -8) {
                return 0;
            }
            res = res * 10 + num;
            x /= 10;
        }
        return res;
    }
}
```

#### 优化溢出判断

```java
class Solution {
    public int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int num = x % 10;
            int pre = res;
            res = res * 10 + num;
            if (res / 10 != pre) {
                return 0;
            }
            x /= 10;
        }
        return res;
    }
}
```

### References

---

#### 1. [整数反转](https://leetcode.cn/problems/reverse-integer/)
