---
title: "LeetCode 6270"
date: 2022-12-25T13:36:07+08:00
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

逆向思维，利用滑动窗口的思想，从两头删去k+个abc，相当于中间的区间中abc的数目小于其总数减去k，这样就可以使用滑动窗口解决了，模板见思想篇章

### 代码

```java
class Solution {
    public int takeCharacters(String s, int k) {
        int ka = 0, kb = 0, kc = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a') {
                ka++;
            }
            if (c == 'b') {
                kb++;
            }
            if (c == 'c') {
                kc++;
            }
        }
        ka -= k; kb -= k; kc -= k;
        if (ka < 0 || kb < 0 || kc < 0) {
            return -1;
        }
        int left = 0, right = 0, res = Integer.MIN_VALUE;
        while (right < s.length()) {
            char c = s.charAt(right);
            right++;
            if (c == 'a') {
                ka--;
            }
            if (c == 'b') {
                kb--;
            }
            if (c == 'c') {
                kc--;
            }

            while (ka < 0 || kb < 0 || kc < 0) {
                char d = s.charAt(left);
                left++;
                if (d == 'a') {
                    ka++;
                }
                if (d == 'b') {
                    kb++;
                }
                if (d == 'c') {
                    kc++;
                }
            }
            res = Math.max(res, right - left);
        }
        return s.length() - res;
    }
}
```

### References

---

#### 1. [每种字符至少取 K 个](https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/)
