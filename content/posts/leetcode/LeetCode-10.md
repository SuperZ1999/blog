---
title: "LeetCode 10"
date: 2022-12-11T19:15:55+08:00
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

dp数组里存s[i...]和p[j...]是否匹配，状态转移方程需要根据s[i]和p[j]是否相等来选择，具体如下：

```java
if (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)) {
    if (p.charAt(j + 1) == '*') {
        dp[i][j] = dp[i][j + 2] || dp[i + 1][j];
    } else {
        dp[i][j] = dp[i + 1][j + 1];
    }
} else {
    if (p.charAt(j + 1) == '*') {
        dp[i][j] = dp[i][j + 2];
    } else {
        dp[i][j] = false;
    }
}
```

base case为：

```java
dp[m][n] = true;
for (int i = n - 2; i >= 0; i -= 2) {
    dp[m][i] = dp[m][i + 2] && (p.charAt(i + 1) == '*');
}
```

可以优化空间复杂度，详见：<https://mp.weixin.qq.com/s/rnaFK05IcFWvNN1ppNf2ug>

### 代码

```java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int n = p.length();
        s = s + "#";
        p = p + "#";
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[m][n] = true;
        for (int i = n - 2; i >= 0; i -= 2) {
            dp[m][i] = dp[m][i + 2] && (p.charAt(i + 1) == '*');
        }
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (p.charAt(j) == '*') {
                    continue;
                }
                if (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)) {
                    if (p.charAt(j + 1) == '*') {
                        dp[i][j] = dp[i][j + 2] || dp[i + 1][j];
                    } else {
                        dp[i][j] = dp[i + 1][j + 1];
                    }
                } else {
                    if (p.charAt(j + 1) == '*') {
                        dp[i][j] = dp[i][j + 2];
                    } else {
                        dp[i][j] = false;
                    }
                }
            }
        }
        return dp[0][0];
    }
}
```

### References

---

#### 1. [正则表达式匹配](https://leetcode.cn/problems/regular-expression-matching/)
