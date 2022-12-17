---
title: "LeetCode 28"
date: 2022-12-18T00:00:17+08:00
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

标准KMP算法，套模板即可，详见思想篇章

### 代码

```java
class Solution {
    public int strStr(String haystack, String needle) {
        return new KMP(needle).search(haystack);
    }

    class KMP {
        private String pat;
        private int[][] dp;

        public KMP(String pat) {
            this.pat = pat;
            int M = pat.length();
            this.dp = new int[M][256];
            dp[0][pat.charAt(0)] = 1;
            int X = 0;
            for (int j = 1; j < M; j++) {
                for (int c = 0; c < 256; c++) {
                    dp[j][c] = dp[X][c];
                }
                dp[j][pat.charAt(j)] = j + 1;
                X = dp[X][pat.charAt(j)];
            }
        }

        public int search(String str) {
            int M = pat.length();
            int N = str.length();
            int j = 0;
            for (int i = 0; i < N; i++) {
                j = dp[j][str.charAt(i)];
                if (j == M) {
                    return i - M + 1;
                }
            }
            return -1;
        }
    }
}
```

### References

---

#### 1. [实现 strStr()](https://leetcode.cn/problems/implement-strstr/)
