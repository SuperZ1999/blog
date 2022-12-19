---
title: "LeetCode 793"
date: 2022-12-19T16:42:53+08:00
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

这道题可以复用[LeetCode-172](https://blog.zhangmengyang.tk/posts/leetcode/leetcode-172/)的函数，从0-Long.MAX_VALUE之间寻找trailingZeroes(n) == k的值，由于trailingZeroes(n)是单调的，所以可以用二分查找确定左右边界（这点不容易想到），这样比穷举快多了，二分查找相关细节见思想篇章

### 代码

```java
class Solution {
    public int preimageSizeFZF(int k) {
        return (int) (rightBound(k) - leftBound(k) + 1);
    }

    private long leftBound(int target) {
        long left = 0, right = Long.MAX_VALUE;
        while (left < right) {
            long mid = left + (right - left) / 2;
            if (target <= trailingZeroes(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private long rightBound(int target) {
        long left = 0, right = Long.MAX_VALUE;
        while (left < right) {
            long mid = left + (right - left) / 2 + (right - left) % 2;
            if (target >= trailingZeroes(mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    private long trailingZeroes(long n) {
        long res = 0;
        while (n >= 5) {
            res += n / 5;
            n /= 5;
        }
        return res;
    }
}
```

### References

---

#### 1. [阶乘函数后 K 个零](https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/)
