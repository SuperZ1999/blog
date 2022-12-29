---
title: "LeetCode 647"
date: 2022-12-29T12:00:58+08:00
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

三种思路：

#### 中心扩展法

遍历字符串，然后从中心扩展，同时统计回文串的数量

#### 动态规划

设置dp数组，dp\[i\]\[j\] = x代表[i...j]字符串是否是回文串，状态转移方程为：`dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 2 || dp[i + 1][j - 1])`，base case为下半个三角都是true，可以优化空间复杂度

#### 马拉车算法

没看太懂，感觉不太重要，大致来说就是中心扩展法的优化，可以在O(N)时间内完成中心扩展法这个流程，基本思想就是假如已知一个回文串，那么在这个回文串中左右对称的那两个字符，中心扩展的回文串是一样的（如果扩展的范围没有超过原回文串的范围）

### 代码

#### 中心扩展法

```java
class Solution {
    public int countSubstrings(String s) {
        int n = s.length(), res = 0;
        res += countSubstrings(s, 0, 0);
        for (int i = 1; i < n; i++) {
            res += countSubstrings(s, i, i);
            res += countSubstrings(s, i - 1, i);
        }
        return res;
    }

    private int countSubstrings(String s, int i, int j) {
        int res = 0;
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            res++;
            i--;
            j++;
        }
        return res;
    }
}
```

#### 动态规划

```java
class Solution {
    public int countSubstrings(String s) {
        int n = s.length(), res = 0;
        boolean[][] dp = new boolean[n][n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || dp[i + 1][j - 1])) {
                    dp[i][j] = true;
                    res++;
                }
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [回文子串](https://leetcode.cn/problems/palindromic-substrings/)
