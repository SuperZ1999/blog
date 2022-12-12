---
title: "LeetCode 887"
date: 2022-12-12T22:55:21+08:00
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

比较复杂，详见：<https://leetcode.cn/problems/super-egg-drop/solutions/44427/ji-ben-dong-tai-gui-hua-jie-fa-by-labuladong/>

### 代码

#### 基本动态规划版(会超时)

```java
class Solution {
    private Map<String, Integer> memo = new HashMap<>();

    public int superEggDrop(int k, int n) {
        if (k == 1) {
            return n;
        }
        if (n == 0) {
            return 0;
        }
        if (memo.containsKey(k + "," + n)) {
            return memo.get(k + "," + n);
        }

        int res = Integer.MAX_VALUE;
        for (int i = 1; i <= n; i++) {
            res = Math.min(res, Math.max(superEggDrop(k, n - i), superEggDrop(k - 1, i - 1)) + 1);
        }
        memo.put(k + "," + n, res);
        return res;
    }
}
```

#### 基本动态规划+二分查找版

```java
class Solution {
    // 基本动态规划+二分查找版
    private Map<String, Integer> memo = new HashMap<>();

    public int superEggDrop(int k, int n) {
        if (k == 1) {
            return n;
        }
        if (n == 0) {
            return 0;
        }
        if (memo.containsKey(k + "," + n)) {
            return memo.get(k + "," + n);
        }

        int res = Integer.MAX_VALUE;
        int left = 1, right = n;
        while (left <= right) {
            int mid = (left + right) / 2;
            int broken = superEggDrop(k - 1, mid - 1);
            int notBroken = superEggDrop(k, n - mid);
            int midVal = broken - notBroken;
            if (0 > midVal) {
                left = mid + 1;
                res = Math.min(res, notBroken + 1);
            } else if (0 < midVal) {
                right = mid - 1;
                res = Math.min(res, broken + 1);
            } else {
                res = broken + 1;
                break;
            }
        }
        memo.put(k + "," + n, res);
        return res;
    }
}
```

#### 进阶动态规划版

```java
class Solution {
    // 进阶动态规划版
    public int superEggDrop(int k, int n) {
        int[][] dp = new int[k + 1][n + 1];
        int m = 0;
        while (dp[k][m] < n) {
            m++;
            for (int i = 1; i <= k; i++) {
                dp[i][m] = dp[i][m - 1] + 1 + dp[i - 1][m - 1];
            }
        }
        return m;
    }
}
```

### References

---

#### 1. [鸡蛋掉落](https://leetcode.cn/problems/super-egg-drop/)
