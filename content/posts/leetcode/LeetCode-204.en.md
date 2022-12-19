---
title: "LeetCode 204"
date: 2022-12-19T20:00:33+08:00
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

经典素数筛选法，详见思想篇章

### 代码

```java
class Solution {
    public int countPrimes(int n) {
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);
        double sqrtn = Math.sqrt(n);
        for (int i = 2; i < sqrtn; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) {
                count++;
            }
        }
        return count;
    }
}
```

### References

---

#### 1. [计数质数](https://leetcode.cn/problems/count-primes/)
