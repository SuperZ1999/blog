---
title: "LeetCode 9"
date: 2023-01-02T20:32:36+08:00
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

#### 简单粗暴版

将数字翻转过来，然后判断与翻转前的数字是否相等

#### 巧妙解法

只翻转一半即可，见代码

### 代码

#### 简单粗暴版

```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        long res = 0, num = x;
        while (num != 0) {
            res = res * 10 + (num % 10);
            num /= 10;
        }
        return res == x;
    }
}
```

#### 巧妙解法

```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int num = 0;
        while (x > num) {
            num = num * 10 + (x % 10);
            x /= 10;
        }
        return num == x || num / 10 == x;
    }
}
```

### References

---

#### 1. [回文数](https://leetcode.cn/problems/palindrome-number/)
