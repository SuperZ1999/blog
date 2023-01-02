---
title: "LeetCode 5"
date: 2022-09-24T15:30:02+08:00
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

两种思路：

#### 中心扩展法

遍历一遍数组，同时从中心向两边寻找回文串，并且保存最长的即可。

#### 动态规划

构建dp数组，数组的元素为[i...j]是否为回文串，状态转移方程为：

```java
if (s.charAt(i) == s.charAt(j) && (j - i < 2 || dp[i + 1][j - 1])) {
    dp[i][j] = true;
}
```

同时统计最长回文串即可，base case为j = i + 1和 j = i的情况，可以优化空间复杂度

#### 马拉车算法

感觉没什么用，没看，就是一个O(n)时间复杂度求最长回文串的一个算法

### 代码

#### 中心扩展法

```java
class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            // 从中心向两边寻找回文串
            String s1 = findPalindrome(s, i, i);
            String s2 = findPalindrome(s, i, i + 1);
            res = res.length() >= s1.length() ? res : s1;
            res = res.length() >= s2.length() ? res : s2;
        }
        return res;
    }

    private String findPalindrome(String s, int left, int right) {
        while (left >= 0 && right < s.length()
                && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return s.substring(left + 1, right);
    }
}
```

#### 动态规划

```java
class Solution {
    public String longestPalindrome(String s) {
        int n = s.length(), maxLen = 0, maxLeft = 0, maxRight = 0;
        boolean[][] dp = new boolean[n][n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || dp[i + 1][j - 1])) {
                    dp[i][j] = true;
                    if (j - i + 1 > maxLen) {
                        maxLeft = i;
                        maxRight = j;
                        maxLen = j - i + 1;
                    }
                }
            }
        }
        return s.substring(maxLeft, maxRight + 1);
    }
}
```

### References

---

#### 1. [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)
